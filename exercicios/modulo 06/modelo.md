# 1. Entrada

```python
dados_cards = [
    {"card_id": "c1", "topic_id": "topic_python", "due_at": "2026-11-18", "review_count": 3, "last_result": "correct"},
    {"card_id": "c2", "topic_id": "topic_git", "due_at": "2026-11-19"},
    {"card_id": "c3", "topic_id": "topic_sql", "due_at": "2026-11-25", "review_count": 1, "last_result": "partial"},
]
```

Data de referência para “está vencido?”: `"2026-11-19"`.

---

# 2. Regras

**Regra 1 — ficha do Card.** Dataclass `Card` com cinco campos tipados: `card_id`, `topic_id` e `due_at` obrigatórios; `review_count` começa em `0`; `last_result` fica `None` quando ninguém informa. O `c2` vem sem os dois opcionais e mesmo assim vira objeto com os defaults.

**Regra 2 — “está vencido?”.** Método no `Card`: numa data X, o card já venceu se `due_at` é **anterior ou igual** a X. Ex.: vence em `"2026-12-01"` → em `"2026-12-01"` está vencido; em `"2026-11-30"` não.

**Regra 3 — converter os dicionários.** Função recebe `dados_cards` e devolve uma **lista** com três objetos `Card`, na ordem c1, c2, c3.

**Regra 4 — ficha da Sessao.** Dataclass `Sessao` com quatro campos: `session_id` e `started_at` obrigatórios; `ended_at` pode faltar (`None` = ainda em andamento); `lesson_ids` começa vazia.

**Regra 5 — “está aberta?”.** Método na `Sessao`: está aberta quando não tem `ended_at` (`None`).

**Regra 6 — cada sessão com a sua lista.** Duas sessões criadas sem informar `lesson_ids`; ao acrescentar uma lição só na primeira, a lista da segunda continua vazia (`default_factory`).

**Regra 7 — os testes.** Asserts conferem tudo, com esperado calculado à mão antes:
- os três objetos que a conversão devolve;
- quais cards estão vencidos em `"2026-11-19"` (um no caso da data igual);
- dois cards com os mesmos dados dão `True` no `==`;
- uma sessão aberta e uma fechada;
- o teste da regra 6.

---

# 3. Saída

- Lista de três `Card` (c1, c2, c3), com defaults no c2.
- Respostas booleanas de `vencido` / `esta_aberta`.
- Igualdade entre cards iguais.
- Listas de lições isoladas por sessão.
- Asserts passando.

---

# 4. Esperados (calculados à mão)

## Conversão (regra 3)

- `c1` → `card_id="c1"`, `topic_id="topic_python"`, `due_at="2026-11-18"`, `review_count=3`, `last_result="correct"`
- `c2` → `card_id="c2"`, `topic_id="topic_git"`, `due_at="2026-11-19"`, `review_count=0`, `last_result=None` (defaults)
- `c3` → `card_id="c3"`, `topic_id="topic_sql"`, `due_at="2026-11-25"`, `review_count=1`, `last_result="partial"`

## Vencidos em `"2026-11-19"` (regra 2)

- `c1`: `"2026-11-18" <= "2026-11-19"` → **True** (anterior)
- `c2`: `"2026-11-19" <= "2026-11-19"` → **True** (igual — caso da borda)
- `c3`: `"2026-11-25" <= "2026-11-19"` → **False** (ainda não venceu)

## Igualdade

- Dois `Card` montados com os mesmos dados → `==` é **True** (dataclass compara campo a campo).

## Sessões (regras 5 e 6)

- Sessão sem `ended_at` → `esta_aberta()` **True**
- Sessão com `ended_at` preenchido → `esta_aberta()` **False**
- Duas sessões novas; `lesson_ids.append(...)` só na primeira → primeira tem a lição; segunda continua `[]`

---

# 5. Plano (em português)

1. Declarar `Card` e `Sessao` com tipos e defaults das regras 1 e 4; lista de lições com `field(default_factory=list)`.
2. Implementar `vencido` com `due_at <= data` e `esta_aberta` com `ended_at is None`.
3. Converter `dados_cards` em lista de `Card` (`Card(**item)`), na ordem.
4. Calcular à mão os esperados da seção 4.
5. Escrever os asserts da regra 7 e rodar até todos passarem.

---

# 6. Asserts (regra 7)

```python
cards = converter_dicionarios(dados_cards)

# três objetos da conversão
assert len(cards) == 3
assert cards[0] == Card("c1", "topic_python", "2026-11-18", 3, "correct")
assert cards[1] == Card("c2", "topic_git", "2026-11-19")  # defaults 0 e None
assert cards[2] == Card("c3", "topic_sql", "2026-11-25", 1, "partial")

# vencidos em 2026-11-19 (c2 = data igual)
assert cards[0].vencido("2026-11-19") is True
assert cards[1].vencido("2026-11-19") is True
assert cards[2].vencido("2026-11-19") is False

# dois cards iguais → True no ==
assert Card("c1", "topic_python", "2026-11-18", 3, "correct") == Card("c1", "topic_python", "2026-11-18", 3, "correct")

# sessão aberta e fechada
aberta = Sessao("s1", "2026-11-19")
fechada = Sessao("s2", "2026-11-19", ended_at="2026-11-19")
assert aberta.esta_aberta() is True
assert fechada.esta_aberta() is False

# regra 6 — listas isoladas
s_a = Sessao("sa", "2026-11-19")
s_b = Sessao("sb", "2026-11-19")
s_a.lesson_ids.append("lesson_1")
assert s_a.lesson_ids == ["lesson_1"]
assert s_b.lesson_ids == []
```
