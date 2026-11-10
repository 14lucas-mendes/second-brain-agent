# Enunciado 005 — Decomposição

## A situação

O app tem uma lista de **cards vencidos**. Precisa ordená-los pela data (da mais antiga para a mais nova) com **ordenação por seleção**, sem mutar a lista original, e informar quantas comparações entre datas o algoritmo fez. O programa ainda mostra os `card_id` dos **3 cards mais atrasados**.

## Entrada

A função recebe:

- `cards`: lista de dicionários, cada um com `card_id` e `due_at` (`AAAA-MM-DD`)

A lista já contém só cards vencidos (não precisa filtrar por “hoje”).

Exemplo de entrada:

```python
cards = [
    {"card_id": "c1", "due_at": "2026-11-12"},
    {"card_id": "c2", "due_at": "2026-11-03"},
    {"card_id": "c3", "due_at": "2026-11-20"},
    {"card_id": "c4", "due_at": "2026-11-01"},
    {"card_id": "c5", "due_at": "2026-11-15"},
    {"card_id": "c6", "due_at": "2026-11-07"},
]
```

## Regras

1. Ordenar com **selection sort** escrita por você. Proibido: `sorted`, `.sort()`, `min`.
2. Critério: `due_at` da data **mais antiga** para a **mais nova**.
3. **Não mutar** a lista de entrada (como `sorted`). Trabalhar em uma cópia e devolver a cópia ordenada.
4. Contar **1 comparação** cada vez que duas datas forem comparadas entre si.
5. Lista vazia → `([], 0)`.
6. Um único card → `([card], 0)`.
7. Depois da ordenação, o programa imprime os `card_id` dos **3 cards mais atrasados** (os 3 primeiros da lista ordenada).
8. Testes com `assert`:
   - resultado da ordenação conferido contra `sorted(cards, key=...)`;
   - esperados de `comparacoes` calculados **à mão**;
   - um assert por caso, incluindo limites: lista vazia, um card só, lista já ordenada, lista em ordem inversa, e o caso normal.

## Saída

Uma tupla `(lista_ordenada, comparacoes)`.

- `lista_ordenada`: nova lista de cards, do `due_at` mais antigo ao mais recente
- `comparacoes`: `int` — quantas vezes duas datas foram comparadas

Formato: `tuple[list[dict], int]`

## Exemplos (saída calculada à mão)

No selection sort clássico (sempre percorre o restante da lista à procura do menor), com `n` itens o número de comparações é sempre:

`1 + 2 + ... + (n - 1) = n * (n - 1) / 2`

Independentemente da ordem inicial.

### Caso normal (`n = 6` → `15` comparações)

Ordem crescente por `due_at`:

| posição | 0 | 1 | 2 | 3 | 4 | 5 |
|---------|---|---|---|---|---|---|
| `card_id` | c4 | c2 | c6 | c1 | c5 | c3 |
| `due_at` | 2026-11-01 | 2026-11-03 | 2026-11-07 | 2026-11-12 | 2026-11-15 | 2026-11-20 |

```python
ordenar_por_selecao(cards)
# lista_ordenada == sorted(cards, key=lambda c: c["due_at"])
# comparacoes == 15
```

Os 3 mais atrasados (imprimir): `c4`, `c2`, `c6`.

### Caso-limite: lista vazia

```python
ordenar_por_selecao([])  # ([], 0)
```

### Caso-limite: um único card

```python
um = [{"card_id": "c1", "due_at": "2026-11-12"}]
ordenar_por_selecao(um)  # ([{"card_id": "c1", "due_at": "2026-11-12"}], 0)
```

### Caso-limite: lista já ordenada (`n = 6` → `15` comparações)

```python
ja_ordenada = [
    {"card_id": "c4", "due_at": "2026-11-01"},
    {"card_id": "c2", "due_at": "2026-11-03"},
    {"card_id": "c6", "due_at": "2026-11-07"},
    {"card_id": "c1", "due_at": "2026-11-12"},
    {"card_id": "c5", "due_at": "2026-11-15"},
    {"card_id": "c3", "due_at": "2026-11-20"},
]

ordenar_por_selecao(ja_ordenada)
# lista_ordenada == sorted(ja_ordenada, key=lambda c: c["due_at"])
# comparacoes == 15
```

### Caso-limite: lista em ordem inversa (`n = 6` → `15` comparações)

```python
inversa = [
    {"card_id": "c3", "due_at": "2026-11-20"},
    {"card_id": "c5", "due_at": "2026-11-15"},
    {"card_id": "c1", "due_at": "2026-11-12"},
    {"card_id": "c6", "due_at": "2026-11-07"},
    {"card_id": "c2", "due_at": "2026-11-03"},
    {"card_id": "c4", "due_at": "2026-11-01"},
]

ordenar_por_selecao(inversa)
# lista_ordenada == sorted(inversa, key=lambda c: c["due_at"])
# comparacoes == 15
```

## Pseudocódigo em português

```
função ordenar_por_selecao(cards):
    se tamanho(cards) = 0:
        devolver ([], 0)

    copia ← cópia rasa de cards
    comparacoes ← 0
    n ← tamanho(copia)

    para i de 0 até n - 2:
        indice_menor ← i
        para j de i + 1 até n - 1:
            comparacoes ← comparacoes + 1
            se copia[j]["due_at"] < copia[indice_menor]["due_at"]:
                indice_menor ← j
        trocar copia[i] com copia[indice_menor]

    devolver (copia, comparacoes)
```

No programa principal: chamar a função, rodar os asserts, imprimir os `card_id` dos 3 primeiros da lista ordenada.
