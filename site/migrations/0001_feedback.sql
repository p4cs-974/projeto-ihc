CREATE TABLE feedback (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  criado_em TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
  versao TEXT NOT NULL,
  respostas TEXT NOT NULL CHECK (json_valid(respostas))
);
