#!/usr/bin/env python3
"""Extract only the annotated demo cuts from an existing local SoccerNet dataset."""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MEDIA = ROOT / "assets/06_prototipos/media"


def probe(path):
    return json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)
    ]))


def run(*args):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *map(str, args)], check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset", type=Path, help="Existing SoccerNet directory, such as TCC benchmark/downloads")
    parser.add_argument("--compare", action="store_true", help="Also extract the same Suárez cut at CRF 26 outside the deployed assets")
    args = parser.parse_args()
    manifest_path = MEDIA / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    sources = {s["id"]: s for s in manifest["sources"]}
    enc = manifest["encoding"]

    for source in sources.values():
        labels_path = args.dataset / source["labelsFile"]
        if hashlib.sha256(labels_path.read_bytes()).hexdigest() != source["labelsSha256"]:
            raise ValueError(f"Source annotations changed: {labels_path}")
        source["_annotations"] = json.loads(labels_path.read_text())["annotations"]
        data = probe(args.dataset / source["file"])
        video = next(s for s in data["streams"] if s["codec_type"] == "video")
        if (video["width"], video["height"], video["codec_name"]) != (398, 224, "h264"):
            raise ValueError(f"Unexpected source encoding: {source['file']}")

    for clip in manifest["clips"]:
        source = sources[clip["sourceId"]]
        if clip["annotation"] not in source["_annotations"]:
            raise ValueError(f"Annotation not found: {clip['id']}")
        event = int(clip["annotation"]["position"]) / 1000 + source["annotationToVideoOffsetSeconds"]
        start, end = clip["cutStartSeconds"], clip["cutEndSeconds"]
        if not 0 <= start < event < end <= source["durationSeconds"]:
            raise ValueError(f"Invalid cut: {clip['id']}")
        clip["eventSourceSeconds"] = event
        clip["eventClipSeconds"] = round(event - start, 3)
        clip["durationSeconds"] = end - start
        output = MEDIA / Path(clip["src"]).name

        def encode(destination, crf):
            run("-ss", start, "-i", args.dataset / source["file"], "-t", end - start,
                "-map", "0:v:0", "-map", "0:a:0", "-c:v", enc["videoCodec"],
                "-crf", crf, "-preset", enc["preset"], "-pix_fmt", enc["pixelFormat"],
                "-g", enc["keyframeInterval"], "-c:a", enc["audioCodec"],
                "-b:a", enc["audioBitrate"], "-movflags", enc["movflags"], destination)

        encode(output, enc["crf"])
        actual = probe(output)
        if abs(float(actual["format"]["duration"]) - (end - start)) > 0.05:
            raise ValueError(f"Unexpected output duration: {output}")
        clip["sizeBytes"] = output.stat().st_size
        clip["sha256"] = hashlib.sha256(output.read_bytes()).hexdigest()
        poster = MEDIA / Path(clip["poster"]).name
        run("-ss", clip["posterClipSeconds"], "-i", output, "-frames:v", 1, "-q:v", 3, poster)
        clip["posterSizeBytes"] = poster.stat().st_size
        print(f"{clip['id']}: {end - start:g} s, {clip['sizeBytes']:,} bytes, event at {clip['eventClipSeconds']:g} s")
        if args.compare and clip["id"] == "suarez":
            comparison = ROOT / "artifacts/media-review/suarez-crf26.mp4"
            comparison.parent.mkdir(parents=True, exist_ok=True)
            encode(comparison, 26)
            print(f"CRF 26 sample: {comparison.stat().st_size:,} bytes")

    for source in sources.values():
        del source["_annotations"]
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
