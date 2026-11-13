# 1. Reproduzir

**Entrada**

```python
topicos = ["topic_python", "topic_sql", "topic_git"]

evidencias = [
    {"evidence_id": "ev_01", "topic_id": "topic_python"},
    {"evidence_id": "ev_02", "topic_id": "topic_git"},
    {"evidence_id": "ev_03", "topic_id": "topic_python"},
    {"evidence_id": "ev_04", "topic_id": "topic_react"},
]
```

**Esperado (calculado à mão)**

- `topic_python` → `ev_01`, depois `ev_03` (ordem de `evidencias`)
- `topic_sql` → lista vazia (nenhuma evidência)
- `topic_git` → `ev_02`
- `ev_04` / `topic_react` fora de `topicos` → ignorado

```python
{"topic_python": ["ev_01", "ev_03"], "topic_sql": [], "topic_git": ["ev_02"]}
```

**Obtido**

```python
{"topic_python": ["ev_03"], "topic_sql": [], "topic_git": ["ev_02"]}
```

Diferença: em `topic_python` falta `ev_01`; só sobrou `ev_03`.

---

# 2. Hipótese (antes de qualquer print)

Acho que a causa é a atribuição `result[topico] = [evidencia["evidence_id"]]` na linha 19, porque ela **substitui** a lista inteira em vez de **acrescentar** o id. Se eu estiver certo, quando eu imprimir `result[topico]` antes e depois dessa linha, vou ver, no segundo `topic_python` (`ev_03`): `antes=['ev_01']` e `depois=['ev_03']` — ou seja, `ev_01` some.

---

# 3. Testar sem consertar

Print dirigido (código com bug intacto):

```python
if topico in result:
    print(f"antes={result[topico]!r} evidencia={evidencia['evidence_id']!r}")
    result[topico] = [evidencia["evidence_id"]]
    print(f"depois={result[topico]!r}")
```

**O que apareceu:**

```
antes=[] evidencia='ev_01'
depois=['ev_01']
antes=[] evidencia='ev_02'
depois=['ev_02']
antes=['ev_01'] evidencia='ev_03'
depois=['ev_03']
result final: {'topic_python': ['ev_03'], 'topic_sql': [], 'topic_git': ['ev_02']}
```

Previsão bateu: no terceiro passo, `antes=['ev_01']` virou `depois=['ev_03']`. Causa confirmada — sobrescrita.

---

# 4. Consertar com teste que falha antes

## Assert antes da correção (falha)

```
AssertionError: esparava {'topic_python': ['ev_01', 'ev_03'], 'topic_sql': [], 'topic_git': ['ev_02']}, obtido {'topic_python': ['ev_03'], 'topic_sql': [], 'topic_git': ['ev_02']}
```

## Correção (só a causa)

```python
# antes
result[topico] = [evidencia["evidence_id"]]

# depois
result[topico] += [evidencia["evidence_id"]]
# (ou: result[topico].append(evidencia["evidence_id"]))
```

## Assert depois da correção (passa)

```
Todos os testes passaram
```
