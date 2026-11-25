#!/usr/bin/env python3
"""Gera as tabelas da Entrega 13 a partir das fichas e da consolidação."""

import argparse
import json
import re
from collections import Counter
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
FORMS = ROOT / "artifacts/entrega13"
DOC = ROOT / "docs/13_avaliacao_heuristica.md"
HEURISTICS = tuple(f"H{i}" for i in range(1, 11))
EVALUATORS = ("A01", "A02", "A03")


@dataclass
class Form:
    coverage: list[list[str]]
    violations: dict[str, list[str]]


def read_form(evaluator: str) -> Form:
    path, = FORMS.glob(f"inspecao_{evaluator}_*.md")
    source = path.read_text(encoding="utf-8")
    rows = [re.split(r"(?<!\\)\|", line)[1:-1] for line in source.splitlines() if line.startswith("|")]
    rows = [[cell.strip() for cell in row] for row in rows]
    coverage = [[row[0], *row[2:]] for row in rows if row[0] in HEURISTICS]
    if tuple(row[0] for row in coverage) != HEURISTICS:
        raise ValueError(f"Matriz H1–H10 incompleta em {path.name}")

    violations = {}
    for row in rows:
        if re.fullmatch(r"V\d{2}", row[0]):
            violation = row[0]
            if len(row) != 8 or violation in violations or int(row[5]) not in range(5):
                raise ValueError(f"Linha inválida em {path.name}: {violation}")
            row[4] = row[4].removeprefix("!").replace(
                "../../assets/13_heuristica/", "../assets/13_heuristica/"
            )
            violations[violation] = row

    return Form(coverage, violations)


def markdown_table(headers, rows, right_aligned=()):
    def line(cells):
        return "| " + " | ".join(map(str, cells)) + " |"

    return "\n".join([
        line(headers),
        line("---:" if i in right_aligned else "---" for i in range(len(headers))),
        *(line(row) for row in rows),
    ])


def ordinal_alpha(units: list[list[int]]) -> float:
    """Calcula o alfa ordinal de Krippendorff com número variável de notas por unidade."""
    if any(len(unit) < 2 for unit in units):
        raise ValueError("Cada unidade do alfa exige ao menos duas notas.")
    counts = Counter(rating for unit in units for rating in unit)
    total = sum(counts.values())
    if len(counts) < 2:
        raise ValueError("O alfa ordinal exige ao menos duas notas distintas.")

    # A distância é a diferença quadrática entre os pontos médios das
    # categorias na distribuição marginal das notas observadas.
    midpoints = {}
    cumulative = 0
    for rating, count in sorted(counts.items()):
        midpoints[rating] = cumulative + count / 2
        cumulative += count

    observed = sum(
        2 * (midpoints[a] - midpoints[b]) ** 2 / (len(unit) - 1)
        for unit in units for a, b in combinations(unit, 2)
    )
    expected = sum(
        2 * counts[a] * counts[b] * (midpoints[a] - midpoints[b]) ** 2 / (total - 1)
        for a, b in combinations(sorted(counts), 2)
    )
    return 1 - observed / expected


def consolidate(forms: dict[str, Form], findings: list[dict]):
    expected = {(e, v) for e, form in forms.items() for v in form.violations}
    covered = set()
    memberships = {}
    for index, finding in enumerate(findings, 1):
        hc = finding["id"]
        if hc != f"HC{index:02}":
            raise ValueError(f"ID fora da sequência: {hc}")
        ratings = {}
        for member in finding["membros"]:
            evaluator, violation = member["avaliador"], member["violacao"]
            if (evaluator, violation) not in expected or evaluator in ratings:
                raise ValueError(f"Referência inválida em {hc}: {evaluator} {violation}")
            score = int(forms[evaluator].violations[violation][5])
            ratings[evaluator] = (violation, score)
            covered.add((evaluator, violation))
        final = finding["severidade_final"]
        if not ratings or final not in range(5):
            raise ValueError(f"Membros ou severidade inválidos em {hc}")
        notes = {score for _, score in ratings.values()}
        if notes != {final} and not finding.get("justificativa_severidade"):
            raise ValueError(f"Falta justificar a severidade de {hc}")
        if max(notes) - min(notes) >= 2 and not finding.get("observacao_reinspecao"):
            raise ValueError(f"Falta a observação da reinspeção em {hc}")
        memberships[hc] = ratings
    if covered != expected:
        raise ValueError(f"Violações sem correspondência: {sorted(expected - covered)}")
    return memberships


def shared_ratings(memberships) -> list[list[int]]:
    """Reúne as notas individuais dos HCs encontrados por ao menos dois avaliadores."""
    return [[score for _, score in ratings.values()] for ratings in memberships.values() if len(ratings) >= 2]


def markers(name):
    return f"<!-- e13:{name}:inicio -->\n", f"\n<!-- e13:{name}:fim -->"


def replace_block(document, name, content):
    start, end = markers(name)
    if document.count(start) != 1 or document.count(end) != 1:
        raise ValueError(f"Marcadores duplicados ou ausentes para {name}")
    before, match, rest = document.partition(start)
    _, close, after = rest.partition(end)
    if not match or not close:
        raise ValueError(f"Marcadores fora de ordem para {name}")
    return before + start + content + end + after


def render(forms, findings, memberships):
    for evaluator, form in forms.items():
        suffix = evaluator.lower()
        yield f"cobertura-{suffix}", markdown_table(
            ["Heurística", "Telas e estados examinados", "Houve violação?", "IDs dos achados"],
            form.coverage,
        )
        yield f"violacoes-{suffix}", markdown_table(
            ["ID", "Heurística", "Tela e estado", "Problema observado", "Evidência",
             "Severidade", "Justificativa da severidade", "Recomendação"],
            form.violations.values(), (5,),
        )

    def consolidated_rows():
        for finding in findings:
            hc = finding["id"]
            ratings = memberships[hc]
            yield [
                f'<a id="{hc.lower()}"></a>{hc}',
                ", ".join(f"{v}({e})" for e, (v, _) in ratings.items()),
                ", ".join([f"**{finding['heuristica_principal']}**", *finding["heuristicas_secundarias"]]),
                f"{finding['tela']} · {finding['estado']}",
                finding["problema"],
                finding["severidade_final"],
                finding["prioridade"],
                finding["responsavel"],
            ]

    yield "consolidacao", markdown_table(
        ["ID consolidado", "Achados individuais", "Heurísticas", "Tela e estado",
         "Problema consolidado", "Severidade final", "Prioridade", "Responsável pela correção"],
        consolidated_rows(), (5,),
    )

    distribution = Counter((f["heuristica_principal"], f["severidade_final"]) for f in findings)
    totals = Counter(f["severidade_final"] for f in findings)
    if any(h not in HEURISTICS for h, _ in distribution):
        raise ValueError("Heurística principal inválida")
    rows = []
    for h in HEURISTICS:
        counts = [distribution[h, s] for s in range(5)]
        rows.append([h, *counts, sum(counts)])
    rows.append(["**Total**", *(f"**{totals[s]}**" for s in range(5)), f"**{len(findings)}**"])
    yield "distribuicao", markdown_table(
        ["Heurística principal", *(f"Sev. {s}" for s in range(5)), "Total"],
        rows, range(1, 7),
    )

    discovered = {e: {hc for hc, ratings in memberships.items() if e in ratings} for e in EVALUATORS}
    unique = [sum(len(memberships[hc]) == 1 for hc in discovered[e]) for e in EVALUATORS]
    discovery = markdown_table(
        ["Achado", *EVALUATORS],
        [
            *([f"[{hc}](#{hc.lower()})", *(ratings[e][0] if e in ratings else "—" for e in EVALUATORS)]
              for hc, ratings in memberships.items()),
            ["**HCs encontrados**", *(len(discovered[e]) for e in EVALUATORS)],
            ["**Contribuição exclusiva**", *unique],
        ],
    )
    overlap = markdown_table(
        ["Par de avaliadores", "HCs em comum", "Proporção do total do par"],
        ([f"{a} e {b}", len(discovered[a] & discovered[b]),
          f"{len(discovered[a] & discovered[b]) / len(discovered[a] | discovered[b]):.2f}".replace(".", ",")]
         for a, b in combinations(EVALUATORS, 2)),
        (1, 2),
    )
    yield "descoberta", discovery + "\n\n" + overlap

    units = shared_ratings(memberships)
    alpha = f"{ordinal_alpha(units):.4f}".replace(".", ",")
    yield "alfa", (
        f"O alfa ordinal de Krippendorff entre os avaliadores foi **{alpha}**, com "
        f"{sum(map(len, units))} notas individuais de {len(units)} HCs encontrados por pelo menos dois avaliadores."
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--escrever", action="store_true", help="atualiza a Entrega 13 no lugar")
    args = parser.parse_args()

    forms = {e: read_form(e) for e in EVALUATORS}
    findings = json.loads((FORMS / "consolidacao.json").read_text(encoding="utf-8"))["achados"]
    memberships = consolidate(forms, findings)
    blocks = dict(render(forms, findings, memberships))
    if not args.escrever:
        for name, content in blocks.items():
            start, end = markers(name)
            print(start + content + end, end="\n\n")
        return

    original = DOC.read_text(encoding="utf-8")
    updated = original
    for name, content in blocks.items():
        updated = replace_block(updated, name, content)
    if updated != original:
        with TemporaryDirectory(dir=DOC.parent) as directory:
            temporary = Path(directory) / DOC.name
            temporary.write_text(updated, encoding="utf-8")
            temporary.replace(DOC)


if __name__ == "__main__":
    main()
