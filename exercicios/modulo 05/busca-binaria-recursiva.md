# Enunciado 006 — Decomposição

## A situação

O app tem uma lista de **lições concluídas**, ordenada pela data de conclusão. Precisa encontrar a lição concluída numa data específica usando **busca binária recursiva**: a função olha o meio do trecho e chama a si mesma só com a metade onde a data ainda pode estar.

## Entrada

A função recebe:

- `licoes`: lista de dicionários, cada um com `lesson_id` e `concluida_em` (`AAAA-MM-DD`)
- `data`: string no formato `AAAA-MM-DD`
- `esquerda` e `direita`: índices que delimitam o trecho da lista ainda em jogo. Na primeira chamada valem `0` e `len(licoes) - 1`, por isso podem ter valor padrão (`esquerda=0`, `direita=None`)

A lista já vem ordenada da data mais antiga para a mais nova e **não tem datas repetidas**.

Exemplo de entrada:

```python
licoes = [
    {"lesson_id": "l01", "concluida_em": "2026-09-07"},
    {"lesson_id": "l03", "concluida_em": "2026-09-12"},
    {"lesson_id": "l04", "concluida_em": "2026-09-17"},
    {"lesson_id": "l02", "concluida_em": "2026-10-06"},
    {"lesson_id": "l15", "concluida_em": "2026-10-23"},
    {"lesson_id": "l16", "concluida_em": "2026-10-31"},
    {"lesson_id": "l17", "concluida_em": "2026-11-20"},
]
```

Repare que a lista está ordenada por **data**, não por `lesson_id`. O `l02` está na posição 3.

## Regras

1. Fazer uma **busca binária recursiva**: olhar o meio do trecho e chamar a própria função com a metade onde a data pode estar.
2. **Proibido** usar `while` ou `for` dentro da função. A repetição vem só da recursão.
3. O meio de cada chamada é `meio = (esquerda + direita) // 2`.
4. Data encontrada → devolver o `lesson_id` da lição.
5. Data não encontrada → devolver `None`.
6. Lista vazia → `None`.
7. **Não mutar** a lista recebida. Trabalhar com os índices `esquerda`/`direita` em vez de fatiar ou alterar a lista.
8. Um **comentário no código** explica qual é o caso-base (ou os casos-base) e por que o problema fica menor a cada chamada.
9. Testes com `assert` e esperados calculados **à mão**, um por caso:
   - a primeira lição;
   - a última;
   - uma do meio;
   - uma data antes de todas;
   - uma data entre duas;
   - uma data depois de todas;
   - a lista vazia;
   - uma lista com uma lição só.

## Saída

O `lesson_id` da lição encontrada, ou `None`.

- `lesson_id`: texto da lição concluída naquela data
- `None`: nenhuma lição foi concluída naquela data

Formato: `str | None`

## Casos-base e por que o problema diminui

Casos-base (a função para de chamar a si mesma):

1. `esquerda > direita` → o trecho ficou **vazio**, então a data não está na lista → `None`. A lista vazia cai aqui logo na primeira chamada (`esquerda = 0`, `direita = -1`).
2. `licoes[meio]["concluida_em"] == data` → **achou** → devolve o `lesson_id`.

Por que o problema fica menor: o tamanho do trecho é `direita - esquerda + 1`. A cada chamada recursiva o `meio` é descartado junto com uma das metades (`direita = meio - 1` ou `esquerda = meio + 1`). O trecho encolhe **pelo menos 1** e, na prática, **cai pela metade**. Por isso ele sempre chega a um dos casos-base, em no máximo ~`log2(n) + 1` chamadas.

## Exemplos (saída calculada à mão)

Índices da lista de entrada (7 itens, `esquerda = 0`, `direita = 6`):

| índice | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|--------|---|---|---|---|---|---|---|
| `lesson_id` | l01 | l03 | l04 | l02 | l15 | l16 | l17 |
| `concluida_em` | 2026-09-07 | 2026-09-12 | 2026-09-17 | 2026-10-06 | 2026-10-23 | 2026-10-31 | 2026-11-20 |

Notação dos traços: `(esquerda, direita)` é o trecho de cada chamada.

### Caso: uma do meio (`2026-10-06`)

1. `(0, 6)` → meio `(0+6)//2 = 3` → `l02` `2026-10-06` — achou (caso-base 2)

Uma única chamada.

```python
busca_licao(licoes, "2026-10-06")  # "l02"
```

### Caso-limite: primeira lição (`2026-09-07`)

1. `(0, 6)` → meio `3` → `2026-10-06` — data é menor → chama `(0, 2)`
2. `(0, 2)` → meio `(0+2)//2 = 1` → `2026-09-12` — data é menor → chama `(0, 0)`
3. `(0, 0)` → meio `0` → `l01` `2026-09-07` — achou

```python
busca_licao(licoes, "2026-09-07")  # "l01"
```

### Caso-limite: última lição (`2026-11-20`)

1. `(0, 6)` → meio `3` → `2026-10-06` — data é maior → chama `(4, 6)`
2. `(4, 6)` → meio `(4+6)//2 = 5` → `2026-10-31` — data é maior → chama `(6, 6)`
3. `(6, 6)` → meio `6` → `l17` `2026-11-20` — achou

```python
busca_licao(licoes, "2026-11-20")  # "l17"
```

### Caso-limite: data antes de todas (`2026-09-01`)

1. `(0, 6)` → meio `3` → `2026-10-06` — menor → chama `(0, 2)`
2. `(0, 2)` → meio `1` → `2026-09-12` — menor → chama `(0, 0)`
3. `(0, 0)` → meio `0` → `2026-09-07` — menor → chama `(0, -1)`
4. `(0, -1)` → `esquerda > direita` → trecho vazio (caso-base 1)

```python
busca_licao(licoes, "2026-09-01")  # None
```

### Caso-limite: data entre duas (`2026-10-15`, entre `l02` e `l15`)

1. `(0, 6)` → meio `3` → `2026-10-06` — maior → chama `(4, 6)`
2. `(4, 6)` → meio `5` → `2026-10-31` — menor → chama `(4, 4)`
3. `(4, 4)` → meio `4` → `2026-10-23` — menor → chama `(4, 3)`
4. `(4, 3)` → `esquerda > direita` → trecho vazio

```python
busca_licao(licoes, "2026-10-15")  # None
```

### Caso-limite: data depois de todas (`2026-12-01`)

1. `(0, 6)` → meio `3` → `2026-10-06` — maior → chama `(4, 6)`
2. `(4, 6)` → meio `5` → `2026-10-31` — maior → chama `(6, 6)`
3. `(6, 6)` → meio `6` → `2026-11-20` — maior → chama `(7, 6)`
4. `(7, 6)` → `esquerda > direita` → trecho vazio

```python
busca_licao(licoes, "2026-12-01")  # None
```

### Caso-limite: lista vazia

`(0, -1)` → `esquerda > direita` já na primeira chamada (regra 6).

```python
busca_licao([], "2026-10-06")  # None
```

### Caso-limite: uma lição só, data existe

1. `(0, 0)` → meio `0` → `l01` `2026-09-07` — achou

```python
uma = [{"lesson_id": "l01", "concluida_em": "2026-09-07"}]

busca_licao(uma, "2026-09-07")  # "l01"
```

### Caso-limite: uma lição só, data não existe

1. `(0, 0)` → meio `0` → `2026-09-07` — data é maior → chama `(1, 0)`
2. `(1, 0)` → `esquerda > direita` → trecho vazio

```python
uma = [{"lesson_id": "l01", "concluida_em": "2026-09-07"}]

busca_licao(uma, "2026-10-06")  # None
```

## Resumo dos esperados

| caso | data | esperado | chamadas |
|------|------|----------|----------|
| uma do meio | `2026-10-06` | `"l02"` | 1 |
| primeira | `2026-09-07` | `"l01"` | 3 |
| última | `2026-11-20` | `"l17"` | 3 |
| antes de todas | `2026-09-01` | `None` | 4 |
| entre duas | `2026-10-15` | `None` | 4 |
| depois de todas | `2026-12-01` | `None` | 4 |
| lista vazia | `2026-10-06` | `None` | 1 |
| uma lição, existe | `2026-09-07` | `"l01"` | 1 |
| uma lição, não existe | `2026-10-06` | `None` | 2 |

A coluna "chamadas" é só para conferir o raciocínio. A função não precisa devolver esse número.

## Pseudocódigo em português

```
função busca_licao(licoes, data, esquerda = 0, direita = nada):
    se direita = nada:
        direita ← tamanho(licoes) - 1

    # caso-base 1: trecho vazio → a data não está na lista
    se esquerda > direita:
        devolver None

    meio ← (esquerda + direita) // 2
    chute ← licoes[meio]["concluida_em"]

    # caso-base 2: achou
    se chute = data:
        devolver licoes[meio]["lesson_id"]

    # passo recursivo: descarta o meio e a metade onde a data não pode estar
    se chute > data:
        devolver busca_licao(licoes, data, esquerda, meio - 1)
    senão:
        devolver busca_licao(licoes, data, meio + 1, direita)
```

No programa principal: rodar um `assert` por caso da tabela acima e, para provar a regra 7, guardar uma cópia da lista antes dos testes e conferir no fim que `licoes` continua igual a ela.
