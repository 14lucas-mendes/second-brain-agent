# Enunciado 004 — Decomposição

## A situação

O app tem uma lista de **sessões** ordenada por data. Precisa achar uma sessão a partir de uma data fixa, usando busca binária, e informar quantos passos a busca levou.

## Entrada

A função recebe:

- `sessoes`: lista de dicionários, cada um com `session_id` e `data` (`AAAA-MM-DD`)
- `data`: string no formato `AAAA-MM-DD`

A lista já vem ordenada por data.

Exemplo de entrada:

```python
sessoes = [
    {"session_id": "s01", "data": "2026-10-01"},
    {"session_id": "s02", "data": "2026-10-04"},
    {"session_id": "s03", "data": "2026-10-09"},
    {"session_id": "s04", "data": "2026-10-12"},
    {"session_id": "s05", "data": "2026-10-18"},
    {"session_id": "s06", "data": "2026-10-23"},
    {"session_id": "s07", "data": "2026-10-30"},
    {"session_id": "s08", "data": "2026-11-02"},
]
```

## Regras

1. Fazer uma **busca binária** (`O(log n)`) na lista de sessões pela data.
2. O meio de cada passo é `meio = (esquerda + direita) // 2`. Cada inspeção de um elemento conta **1 passo** (no binário, o do meio; no linear, o da vez).
3. Devolver uma tupla `(session_id, passos)`.
4. Lista vazia → `(None, 0)` (nenhuma inspeção).
5. Data **não encontrada** → `(None, passos)`, com os passos realmente dados.
6. Para as **mesmas datas**, comparar com uma **busca linear** (mesmo formato de tupla).
7. Escrever testes com `assert` usando os resultados esperados calculados **à mão**.

## Saída

Uma tupla `(session_id, passos)`.

- `session_id`: texto da sessão encontrada, ou `None`
- `passos`: `int` — quantas inspeções foram feitas

Formato: `tuple[str | None, int]`

## Exemplos (saída calculada à mão)

Índices da lista de entrada (8 itens, `esquerda = 0`, `direita = 7`):

| índice | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|--------|---|---|---|---|---|---|---|---|
| `session_id` | s01 | s02 | s03 | s04 | s05 | s06 | s07 | s08 |
| `data` | 2026-10-01 | 2026-10-04 | 2026-10-09 | 2026-10-12 | 2026-10-18 | 2026-10-23 | 2026-10-30 | 2026-11-02 |

### Caso normal: acha `s05` (`2026-10-18`)

1. meio `(0+7)//2 = 3` → `s04` `2026-10-12` — data é maior → `esquerda = 4`
2. meio `(4+7)//2 = 5` → `s06` `2026-10-23` — data é menor → `direita = 4`
3. meio `(4+4)//2 = 4` → `s05` `2026-10-18` — achou

```python
busca_binaria(sessoes, "2026-10-18")  # ("s05", 3)
busca_linear(sessoes, "2026-10-18")   # ("s05", 5)
```

### Caso-limite: lista vazia

Nenhuma inspeção (regra 4).

```python
busca_binaria([], "2026-10-18")  # (None, 0)
busca_linear([], "2026-10-18")   # (None, 0)
```

### Caso-limite: primeiro elemento (`s01`)

1. meio `3` → `s04` — data é menor → `direita = 2`
2. meio `(0+2)//2 = 1` → `s02` — data é menor → `direita = 0`
3. meio `(0+0)//2 = 0` → `s01` — achou

Linear para no 1º item. Aqui a linear gasta **menos** passos.

```python
busca_binaria(sessoes, "2026-10-01")  # ("s01", 3)
busca_linear(sessoes, "2026-10-01")   # ("s01", 1)
```

### Caso-limite: último elemento (`s08`)

1. meio `3` → `s04` — data é maior → `esquerda = 4`
2. meio `5` → `s06` — data é maior → `esquerda = 6`
3. meio `(6+7)//2 = 6` → `s07` — data é maior → `esquerda = 7`
4. meio `(7+7)//2 = 7` → `s08` — achou

Linear percorre os 8. Aqui a binária gasta **menos** passos.

```python
busca_binaria(sessoes, "2026-11-02")  # ("s08", 4)
busca_linear(sessoes, "2026-11-02")   # ("s08", 8)
```

### Caso-limite: acerta no primeiro meio (`s04`)

O primeiro meio já é o alvo: 1 passo.

```python
busca_binaria(sessoes, "2026-10-12")  # ("s04", 1)
busca_linear(sessoes, "2026-10-12")   # ("s04", 4)
```

### Caso-limite: data inexistente no meio (`2026-10-15`)

1. meio `3` → `s04` `2026-10-12` — maior → `esquerda = 4`
2. meio `5` → `s06` `2026-10-23` — menor → `direita = 4`
3. meio `4` → `s05` `2026-10-18` — menor → `direita = 3`
4. `esquerda = 4` > `direita = 3` → para (regra 5)

Linear olha os 8 e não acha.

```python
busca_binaria(sessoes, "2026-10-15")  # (None, 3)
busca_linear(sessoes, "2026-10-15")   # (None, 8)
```

### Caso-limite: data antes da primeira (`2026-09-01`)

Mesmos 3 meios de `s01` (`s04` → `s02` → `s01`), mas a data é menor que `s01` → intervalo esvazia.

```python
busca_binaria(sessoes, "2026-09-01")  # (None, 3)
busca_linear(sessoes, "2026-09-01")   # (None, 8)
```

### Caso-limite: data depois da última (`2026-12-01`)

Mesmos 4 meios de `s08` (`s04` → `s06` → `s07` → `s08`), mas a data é maior que `s08` → intervalo esvazia.

```python
busca_binaria(sessoes, "2026-12-01")  # (None, 4)
busca_linear(sessoes, "2026-12-01")   # (None, 8)
```

### Caso-limite: um único elemento, data existe

```python
uma = [{"session_id": "s01", "data": "2026-10-01"}]

busca_binaria(uma, "2026-10-01")  # ("s01", 1)
busca_linear(uma, "2026-10-01")   # ("s01", 1)
```

### Caso-limite: um único elemento, data não existe

Inspeciona o único item e não acha (não é lista vazia: há 1 passo).

```python
uma = [{"session_id": "s01", "data": "2026-10-01"}]

busca_binaria(uma, "2026-10-18")  # (None, 1)
busca_linear(uma, "2026-10-18")   # (None, 1)
```

## Comparação binária × linear (mesmas datas, lista de 8)

| data | binária | linear |
|------|---------|--------|
| `2026-10-18` (normal) | `("s05", 3)` | `("s05", 5)` |
| `2026-10-01` (primeiro) | `("s01", 3)` | `("s01", 1)` |
| `2026-11-02` (último) | `("s08", 4)` | `("s08", 8)` |
| `2026-10-12` (primeiro meio) | `("s04", 1)` | `("s04", 4)` |
| `2026-10-15` (não existe) | `(None, 3)` | `(None, 8)` |
| lista vazia | `(None, 0)` | `(None, 0)` |

## Pseudocódigo em português

### Busca binária (`busca_data`)

```
função busca_data(lista, data):
    passos ← 0
    se tamanho(lista) = 0:
        devolver (None, passos)

    baixo ← 0
    alto ← tamanho(lista) - 1

    enquanto baixo ≤ alto:
        meio ← (baixo + alto) // 2
        chute ← lista[meio]["data"]

        se chute = data:
            passos ← passos + 1
            devolver (lista[meio]["session_id"], passos)

        se chute > data:
            passos ← passos + 1
            alto ← meio - 1

        se chute < data:
            passos ← passos + 1
            baixo ← meio + 1

    devolver (None, passos)
```

### Busca linear (`busca_linear`)

```
função busca_linear(lista, data):
    passos ← 0
    se tamanho(lista) = 0:
        devolver (None, passos)

    para cada item em lista:
        passos ← passos + 1
        se item["data"] = data:
            devolver (item["session_id"], passos)

    devolver (None, passos)
```

### Comparação no console

```
para cada data na tabela de comparação:
    (id_bin, passos_bin) ← busca_data(sessoes, data)
    (id_lin, passos_lin) ← busca_linear(sessoes, data)
    imprimir data, passos_bin, id_bin, passos_lin, id_lin
```
