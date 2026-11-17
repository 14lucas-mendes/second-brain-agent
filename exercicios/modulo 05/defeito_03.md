Parecido com os Defeitos 1 e 2: mesmo ciclo (reproduzir → hipótese → testar sem consertar → consertar com assert). Diferente: lá o bug era localização ou atribuição de variável (sobrescrita de lista / `ultima` fora do laço); aqui o erro está no operador lógico — `or` em vez de `and`, então bastava um lado da condição ser verdadeiro (curto-circuito) para contar como acerto sem pista.

# 1. Reproduzir 

**Entrada**

```python
tentativas = [
    {"topic_id": "topic_python", "outcome": "correct", "support_level": 0},
    {"topic_id": "topic_python", "outcome": "partial", "support_level": 0},
    {"topic_id": "topic_git", "outcome": "incorrect", "support_level": 0},
    {"topic_id": "topic_git", "outcome": "correct", "support_level": 2},
    {"topic_id": "topic_python", "outcome": "correct", "support_level": 2},
    {"topic_id": "topic_sql", "outcome": "correct", "support_level": 0},
]
```

**Esperado (calculado à mão)**

Para cada tópico: `tentativas` = quantidade; `acertos_sem_pista` = `outcome == "correct"` e `support_level == 0`; `taxa` = `round(acertos_sem_pista * 100 / tentativas)`.

- `topic_python` → 3 tentativas; acertos sem pista: só a 1ª (`correct`+0); a `partial` e a `correct`+2 não contam → 1; `round(1*100/3)` = 33
- `topic_git` → 2 tentativas; `incorrect`+0 e `correct`+2 → acertos sem pista 0; `round(0*100/2)` = 0
- `topic_sql` → 1 tentativa; `correct`+0 → 1; `round(1*100/1)` = 100

```python
{
    "topic_python": {"tentativas": 3, "acertos_sem_pista": 1, "taxa": 33},
    "topic_git": {"tentativas": 2, "acertos_sem_pista": 0, "taxa": 0},
    "topic_sql": {"tentativas": 1, "acertos_sem_pista": 1, "taxa": 100},
}
```
**Obtido**

```python
{
    "topic_python": {"tentativas": 3, "acertos_sem_pista": 3, "taxa": 100},
    "topic_git": {"tentativas": 2, "acertos_sem_pista": 2, "taxa": 100},
    "topic_sql": {"tentativas": 1, "acertos_sem_pista": 1, "taxa": 100},
}
```

Diferença: `topic_python` veio com `acertos_sem_pista` 3 e taxa 100 (esperado 1 e 33); `topic_git` veio com 2 e 100 (esperado 0 e 0). Só `topic_sql` bateu.

# 2. Hipótese (antes de qualquer print)

Acho que a causa é o `or` na condição `if t["outcome"] == "correct" or t["support_level"] == 0`, porque um acerto sem pista exige as **duas** condições verdadeiras (`correct` **e** `support_level == 0`), e com `or` basta uma delas. Assim entram no contador a `partial`+0, a `incorrect`+0 e as `correct` com pista. Se eu estiver certo, quando eu imprimir `outcome`, `support_level` e se a condição disparou para cada tentativa, vou ver: em `topic_python` as 3 linhas incrementam (esperado só a 1ª); em `topic_git` as 2 incrementam (esperado nenhuma); em `topic_sql` a única incrementa (ok).

Correção prevista: trocar `or` por `and`.

# 3. Testar sem consertar

Print dirigido (código com bug intacto: `or` na condição):

```python
for t in tentativas:
    dispara = t["outcome"] == "correct" or t["support_level"] == 0
    print(f"topico={t['topic_id']!r} outcome={t['outcome']!r} support={t['support_level']!r} dispara={dispara}")
```

**O que apareceu:**

```
topico='topic_python' outcome='correct' support=0 dispara=True
topico='topic_python' outcome='partial' support=0 dispara=True
topico='topic_git' outcome='incorrect' support=0 dispara=True
topico='topic_git' outcome='correct' support=2 dispara=True
topico='topic_python' outcome='correct' support=2 dispara=True
topico='topic_sql' outcome='correct' support=0 dispara=True
```

Previsão bateu: as 6 tentativas disparam `True` com o `or`. Só a 1ª e a 6ª deveriam contar. Causa confirmada — operador errado.

# 4. Consertar com teste que falha antes

## Assert antes da correção (falha)

```
AssertionError: esperado {'topic_python': {'tentativas': 3, 'acertos_sem_pista': 1, 'taxa': 33}, 'topic_git': {'tentativas': 2, 'acertos_sem_pista': 0, 'taxa': 0}, 'topic_sql': {'tentativas': 1, 'acertos_sem_pista': 1, 'taxa': 100}}, obtido {'topic_python': {'tentativas': 3, 'acertos_sem_pista': 3, 'taxa': 100}, 'topic_git': {'tentativas': 2, 'acertos_sem_pista': 2, 'taxa': 100}, 'topic_sql': {'tentativas': 1, 'acertos_sem_pista': 1, 'taxa': 100}}
```

## Correção (só a causa)

```python
# antes
if t["outcome"] == "correct" or t["support_level"] == 0:

# depois
if t["outcome"] == "correct" and t["support_level"] == 0:
```

## Assert depois da correção (passa)

```
Todos os testes passaram
```

