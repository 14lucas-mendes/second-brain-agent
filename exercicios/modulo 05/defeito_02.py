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


def resumo_revisoes(cards):
    """Para cada card: revisoes, acertos e a data da ultima revisao (a maior)."""
    resumos = {}
    
    for card in cards:
        acertos = 0
        ultima = None
        for revisao in card["revisoes"]:
            if revisao["resultado"] == "correct":
                acertos += 1
            if ultima is None or revisao["data"] > ultima:
                ultima = revisao["data"]
        resumos[card["card_id"]] = {
            "revisoes": len(card["revisoes"]),
            "acertos": acertos,
            "ultima": ultima,
        }
    return resumos

if __name__ == "__main__":
    obtido = resumo_revisoes(cards)

    esperado = {'card_a': {'revisoes': 3, 'acertos': 2, 'ultima': '2026-10-27'}, 'card_b': {'revisoes': 2, 'acertos': 2, 'ultima': '2026-10-26'}, 'card_c': {'revisoes': 0, 'acertos': 0, 'ultima': None}}

    assert obtido == esperado, f"esperado {esperado}, obtido {obtido}"

    print("todos os testes passaram.")