# Enunciado 001 — Decomposição

## A situação

O app tem uma lista de **tópicos** e uma lista de **evidências**. Cada evidência diz a que tópico ela pertence.

## Entrada

A função recebe:

- `topicos`: lista de strings (IDs dos tópicos)
- `evidencias`: lista de dicionários, cada um com `evidence_id` e `topic_id`

Exemplo de entrada:

```python
topicos = ["topic_python", "topic_sql", "topic_git"]

evidencias = [
    {"evidence_id": "ev_01", "topic_id": "topic_python"},
    {"evidence_id": "ev_02", "topic_id": "topic_git"},
    {"evidence_id": "ev_03", "topic_id": "topic_python"},
    {"evidence_id": "ev_04", "topic_id": "topic_react"},
]
```

## Regra

Montar, **uma vez só**, uma estrutura índice (tópico → lista de IDs de evidências) para responder rápido “quais evidências tem este tópico?”, cumprindo:

1. **Todos os tópicos** de `topicos` aparecem na resposta, mesmo sem evidência.
2. Os IDs de cada tópico aparecem **na mesma ordem** em que estão em `evidencias`.
3. Evidência cujo `topic_id` **não está** em `topicos` **não entra** na resposta.
4. No código (depois), um comentário justifica a escolha de cada estrutura.

## Saída

Um dicionário em que a chave é o tópico e o valor é a lista de `evidence_id` daquele tópico (na ordem de `evidencias`).

Formato: `dict[str, list[str]]`

Justificativa da estrutura (para a regra 4, no código): dicionário permite olhar o tópico e já ver a lista; lista por valor preserva a ordem da regra 2 e aceita zero ou várias evidências.

## Exemplos (saída calculada à mão)

### Caso normal

Entrada: a do bloco acima.

- `ev_01` e `ev_03` → `topic_python` (ordem de `evidencias`)
- `ev_02` → `topic_git`
- `topic_sql` não tem evidência, mas está em `topicos` → lista vazia (regra 1)
- `ev_04` → `topic_react`, que **não** está em `topicos` → descartado (regra 3)

```python
{
    "topic_python": ["ev_01", "ev_03"],
    "topic_sql": [],
    "topic_git": ["ev_02"],
}
```

### Caso-limite: evidência aponta para tópico fora de `topicos`

Já coberto no caso normal (`ev_04` / `topic_react`). A saída **não** inclui `topic_react`.

### Caso-limite: `topicos` vazia

```python
topicos = []
evidencias = [
    {"evidence_id": "ev_01", "topic_id": "topic_python"},
]
```

Saída esperada: `{}`  
(Não há tópicos a listar; qualquer evidência seria de tópico fora de `topicos` — regras 1 e 3.)

### Caso-limite: `evidencias` vazia (com tópicos)

```python
topicos = ["topic_python", "topic_git"]
evidencias = []
```

Saída esperada:

```python
{
    "topic_python": [],
    "topic_git": [],
}
```

(Regra 1: os tópicos continuam na resposta, só sem IDs.)

### Caso-limite: as duas listas vazias

```python
topicos = []
evidencias = []
```

Saída esperada: `{}`

### Caso-limite: várias evidências no mesmo tópico (ordem)

```python
topicos = ["topic_python"]
evidencias = [
    {"evidence_id": "ev_03", "topic_id": "topic_python"},
    {"evidence_id": "ev_01", "topic_id": "topic_python"},
]
```

Saída esperada:

```python
{
    "topic_python": ["ev_03", "ev_01"],
}
```

(Regra 2: ordem de `evidencias`, não ordem alfabética dos IDs.)

## Plano em português

1. Se `topicos` estiver vazia, retornar `{}` de imediato.  
   *(Não retornar `{}` só porque `evidencias` está vazia — isso quebraria a regra 1.)*
2. Criar um dicionário resultado percorrendo `topicos` na ordem dada, com cada tópico mapeado para uma lista vazia.  
   *(Garante a regra 1 desde o início.)*
3. Percorrer `evidencias` **na ordem em que aparecem**.
4. Para cada evidência, ler `topic_id` e `evidence_id`.  
   - Se `topic_id` **estiver** no dicionário resultado, acrescentar `evidence_id` no fim da lista desse tópico (regra 2).  
   - Se `topic_id` **não estiver** no dicionário, ignorar a evidência (regra 3).
5. Devolver o dicionário resultado.
6. No código, comentar por que o dicionário (e a lista por valor) foi a estrutura escolhida (regra 4).

## Checagem regras × exemplos × plano

| Regra | Exemplos | Plano |
|-------|----------|--------|
| 1 — todo tópico aparece | Caso normal tem `topic_sql: []`; evidências vazias ainda devolvem os tópicos | Passo 2 inicializa todos; passo 1 **não** zera só por evidências vazias |
| 2 — ordem de `evidencias` | Caso da ordem `ev_03` antes de `ev_01` | Passo 3–4 percorre evidências na ordem e faz `append` |
| 3 — fora de `topicos` some | `ev_04` / `topic_react` não entra | Passo 4 ignora `topic_id` ausente no resultado |

**Correções em relação à versão anterior do README:** o caso “normal” incluía `topic_react` (viola regra 3) e omitia tópico sem evidência (viola regra 1); “evidências vazias → `[]`” também violava a regra 1; o plano devolvia vazio se *qualquer* lista estivesse vazia — isso foi corrigido.