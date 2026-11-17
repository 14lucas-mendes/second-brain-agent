Parecido com o Defeito 1: mesmo ciclo (reproduzir → hipótese → testar sem consertar → consertar com assert). Diferente: aqui o bug é estado compartilhado entre iterações (`ultima` fora do laço dos cards), não sobrescrita de lista.

# 1. Reproduzir 

**Entrada**

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

**Esperado (calculado à mão)**

Para cada card: `revisoes` = quantidade; `acertos` = quantos `"correct"`; `ultima` = maior data daquele card (ou `None` se não houver revisões).

- `card_a` → 3 revisões; acertos `correct` + `correct` + `incorrect` → 2; datas `2026-10-20`, `2026-10-27`, `2026-10-25` → maior = `2026-10-27`
- `card_b` → 2 revisões; acertos 2; datas `2026-10-26`, `2026-10-22` → maior = `2026-10-26`
- `card_c` → 0 revisões; acertos 0; sem datas → `ultima = None`

```python
{
    "card_a": {"revisoes": 3, "acertos": 2, "ultima": "2026-10-27"},
    "card_b": {"revisoes": 2, "acertos": 2, "ultima": "2026-10-26"},
    "card_c": {"revisoes": 0, "acertos": 0, "ultima": None},
}
```

**Obtido**

```python
{
    "card_a": {"revisoes": 3, "acertos": 2, "ultima": "2026-10-27"},
    "card_b": {"revisoes": 2, "acertos": 2, "ultima": "2026-10-27"},
    "card_c": {"revisoes": 0, "acertos": 0, "ultima": "2026-10-27"},
}
```

Diferença: `card_b.ultima` veio `2026-10-27` (esperado `2026-10-26`); `card_c.ultima` veio `2026-10-27` (esperado `None`). Só `card_a` bateu.

# 2. Hipótese (antes de qualquer print)

Acho que a causa é `ultima = None` estar **fora** do `for card in cards`, porque a variável sobrevive de um card para o outro: depois de `card_a` fica `"2026-10-27"` e esse valor “vaza” para `card_b` e `card_c`. Se eu estiver certo, quando eu imprimir `ultima` no início de cada card e no momento de gravar o resumo, vou ver: em `card_a` inicia `None` e termina `"2026-10-27"`; em `card_b` inicia já `"2026-10-27"` (não `None`) e termina `"2026-10-27"` em vez de `"2026-10-26"`; em `card_c` inicia `"2026-10-27"` e, sem revisões, grava essa data em vez de `None`.

Correção prevista: mover `ultima = None` para **dentro** do `for card in cards` (junto de `acertos = 0`), para cada card recomeçar do zero.

# 3. Testar sem consertar

Print dirigido (código com bug intacto: `ultima` **fora** do `for card in cards`):

```python
ultima = None
for card in cards:
    print(f"inicio card={card['card_id']!r} ultima={ultima!r}")
    acertos = 0
    for revisao in card["revisoes"]:
        if revisao["resultado"] == "correct":
            acertos += 1
        if ultima is None or revisao["data"] > ultima:
            ultima = revisao["data"]
        print(f"  revisao data={revisao['data']!r} ultima={ultima!r}")
    resumos[card["card_id"]] = {
        "revisoes": len(card["revisoes"]),
        "acertos": acertos,
        "ultima": ultima,
    }
    print(f"grava card={card['card_id']!r} ultima={ultima!r}")
```

**O que apareceu:**

```
inicio card='card_a' ultima=None
  revisao data='2026-10-20' ultima='2026-10-20'
  revisao data='2026-10-27' ultima='2026-10-27'
  revisao data='2026-10-25' ultima='2026-10-27'
grava card='card_a' ultima='2026-10-27'
inicio card='card_b' ultima='2026-10-27'
  revisao data='2026-10-26' ultima='2026-10-27'
  revisao data='2026-10-22' ultima='2026-10-27'
grava card='card_b' ultima='2026-10-27'
inicio card='card_c' ultima='2026-10-27'
grava card='card_c' ultima='2026-10-27'
```

Previsão bateu: `card_b` e `card_c` já começam com `ultima='2026-10-27'` (vazou de `card_a`). Causa confirmada — `ultima` compartilhada entre cards.

# 4. Consertar com teste que falha antes

## Assert antes da correção (falha)

```
AssertionError: esperado {'card_a': {'revisoes': 3, 'acertos': 2, 'ultima': '2026-10-27'}, 'card_b': {'revisoes': 2, 'acertos': 2, 'ultima': '2026-10-26'}, 'card_c': {'revisoes': 0, 'acertos': 0, 'ultima': None}}, obtido {'card_a': {'revisoes': 3, 'acertos': 2, 'ultima': '2026-10-27'}, 'card_b': {'revisoes': 2, 'acertos': 2, 'ultima': '2026-10-27'}, 'card_c': {'revisoes': 0, 'acertos': 0, 'ultima': '2026-10-27'}}
```

## Correção (só a causa)

```python
# antes — ultima fora do laço dos cards
ultima = None
for card in cards:
    acertos = 0
    ...

# depois — ultima reinicia a cada card
for card in cards:
    acertos = 0
    ultima = None
    ...
```

## Assert depois da correção (passa)

```
todos os testes passaram.
```
