# Enunciado — Índice 3: card → resumo do histórico

## A situação

O app precisa mostrar, para cada card, um resumo das revisões, e também destacar o card com mais acertos.

## Entrada

A função recebe:

- `cards`: lista de dicionários
  - cada card tem `card_id` (texto) e `revisoes` (lista)
  - cada revisão tem `data` (texto `YYYY-MM-DD`) e `resultado` (`"correct"` ou `"incorrect"`)

Exemplo de entrada:

```python
cards = [
    {"card_id": "card_a", "revisoes": [
        {"data": "2026-10-20", "resultado": "correct"},
        {"data": "2026-10-27", "resultado": "correct"},
        {"data": "2026-10-25", "resultado": "incorrect"},
    ]},
    {"card_id": "card_b", "revisoes": [
        {"data": "2026-10-26", "resultado": "correct"},
        {"data": "2026-10-22", "resultado": "correct"},
    ]},
    {"card_id": "card_c", "revisoes": []},
]
```

## Regra

1. Por card: contar quantas revisões, quantos acertos (`"correct"`) e a data da última revisão.
2. “Última” = a **maior data**, não a que está no fim da lista (as revisões podem vir fora de ordem).
3. Card sem revisões (`[]`): `0` revisões, `0` acertos e `ultima = None`.
4. Além do resumo, apontar o `card_id` com mais acertos.
5. Empate de acertos: fica o que aparece **primeiro** em `cards`.
6. Se não houver nenhum card (`cards = []`): `mais_acertos = None` (e `resumos` vazio).
7. Gravar o resultado num `indice.json` e verificar o arquivo **relido** contra o esperado calculado à mão.
8. No código, um comentário justifica a escolha do formato de saída.

## Saída

Um dicionário com duas chaves:

- `resumos`: mapa `card_id` → `{"revisoes": int, "acertos": int, "ultima": str | None}`
- `mais_acertos`: `card_id` (str) ou `None`

Formato:

```python
{
    "resumos": {
        "card_a": {"revisoes": n, "acertos": n, "ultima": "YYYY-MM-DD" ou None},
        # ... um item por card
    },
    "mais_acertos": "card_id" ou None,
}
```

Justificativa da estrutura (regra 8): `resumos` responde “como está cada card?”; `mais_acertos` responde “quem lidera em acertos?”. Um único dict guarda as duas respostas do enunciado. Dict em `resumos` permite achar um card pelo id; `None` em `ultima` / `mais_acertos` cobre os casos sem data ou sem cards.

## Exemplos (saída calculada à mão)

### Caso normal

Entrada: a do bloco acima.

- `card_a`: 3 revisões, 2 acertos, maior data `2026-10-27` (não a 3ª da lista)
- `card_b`: 2 revisões, 2 acertos, maior data `2026-10-26` (não `2026-10-22`)
- `card_c`: lista vazia → `0`, `0`, `None`
- Empate 2–2 entre `a` e `b` → `mais_acertos = "card_a"` (primeiro na lista)

```python
{
    "resumos": {
        "card_a": {"revisoes": 3, "acertos": 2, "ultima": "2026-10-27"},
        "card_b": {"revisoes": 2, "acertos": 2, "ultima": "2026-10-26"},
        "card_c": {"revisoes": 0, "acertos": 0, "ultima": None},
    },
    "mais_acertos": "card_a",
}
```

### Caso-limite: `cards` vazia

```python
cards = []
```

Saída esperada:

```python
{
    "resumos": {},
    "mais_acertos": None,
}
```

(Regra 6: sem cards, o vencedor é `None`.)

### Caso-limite: um card só, com `revisoes` vazia

```python
cards = [
    {"card_id": "card_a", "revisoes": []},
]
```

Saída esperada:

```python
{
    "resumos": {
        "card_a": {"revisoes": 0, "acertos": 0, "ultima": None},
    },
    "mais_acertos": "card_a",
}
```

(Regra 3 no resumo; regra 4/6: há card, então `mais_acertos` **não** é `None` — é esse id, mesmo com 0 acertos.)

### Caso-limite: empate de acertos

Mesmos números do caso normal (`card_a` e `card_b` com 2 acertos).

Saída esperada: igual ao caso normal — `mais_acertos = "card_a"` (regra 5: primeiro na lista).

## Plano em português

1. Se `cards` estiver vazia, devolver de imediato `{"resumos": {}, "mais_acertos": None}`.
2. Criar `resumos = {}`, `mais_acertos = None` e `melhor_acertos = -1`.  
   *(O `-1` garante que o primeiro card, mesmo com 0 acertos, passa a líder.)*
3. Percorrer cada `card` em `cards` (na ordem da lista).
4. Para o card atual:
   - `n_revisoes = len(card["revisoes"])`
   - `acertos = 0` e `ultima = None`
   - Percorrer cada item em `card["revisoes"]`:
     - se `resultado == "correct"`, somar 1 em `acertos`
     - se `ultima` é `None` ou `data` é maior que `ultima`, atualizar `ultima` com essa `data`  
       *(maior data = última revisão; lista vazia deixa `ultima` em `None`)*
   - Guardar em `resumos[card["card_id"]]` o dict  
     `{"revisoes": n_revisoes, "acertos": acertos, "ultima": ultima}`
5. Atualizar o líder: se `acertos > melhor_acertos`, então  
   `melhor_acertos = acertos` e `mais_acertos = card["card_id"]`.  
   *(Usar `>`, não `>=`: empate mantém o que apareceu primeiro.)*
6. Depois do laço, devolver `{"resumos": resumos, "mais_acertos": mais_acertos}`.
7. No código, comentar por que este formato de saída foi escolhido (regra 8).
8. Gravar esse resultado em `indice.json` (ex.: com `json.dump`).
9. Reler o arquivo (ex.: `json.load`) e comparar com o esperado do caso normal calculado à mão.  
   *(Se a leitura bater com o esperado, a gravação está correta; senão, falhar com assert/mensagem.)*
10. Opcional: repetir asserts em memória para os outros exemplos (lista vazia, card só, empate).

## Checagem regras × exemplos × plano

| Regra | Exemplos | Plano |
|-------|----------|--------|
| 1–2 — contar + maior data | Caso normal: `card_a` ultima `27`, não a 3ª da lista | Passo 4 atualiza `ultima` pelo max da data |
| 3 — revisões vazias | Card só com `[]` → 0, 0, `None` | Passo 4: len 0, loop não roda, `ultima` fica `None` |
| 4–5 — mais acertos / empate | Normal e empate → `card_a` | Passo 5 só troca com `>` |
| 6 — `cards` vazia | `resumos {}`, `mais_acertos None` | Passo 1 |
| 7 — gravar `indice.json` e reler | Esperado do caso normal (à mão) | Passos 8–9: dump → load → comparar |
| 8 — justificar formato | Secção Saída | Passo 7 (comentário no código) |
