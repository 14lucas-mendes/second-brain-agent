from datetime import date

cards = [
    {"card_id": "card_a", "due_at": "2026-10-05"},
    {"card_id": "card_b", "due_at": "2026-10-12"},
    {"card_id": "card_c", "due_at": "2026-10-09"},
    {"card_id": "card_d", "due_at": "2026-09-20"},
    {"card_id": "card_e", "due_at": ""},
]


def contar_vencidos(cards, hoje):
    if len(cards) == 0:
        return 0
    contador = 0
    for card in cards:
        if card["due_at"] == None or card["due_at"] <= hoje:
            contador += 1
    
    return contador

hoje = date.today().isoformat()


if __name__ == "__main__":
    resultado = contar_vencidos(cards, hoje)

    assert contar_vencidos([{"card_id": "card_a", "due_at": "2026-10-05"}], '2026-10-09') == 1
    assert contar_vencidos([{"card_id": "card_b", "due_at": "2026-10-12"}], '2026-10-09') == 0
    assert contar_vencidos([{"card_id": "card_c", "due_at": "2026-10-09"}], '2026-10-09') == 1
    assert contar_vencidos([{"card_id": "card_d", "due_at": "2026-09-20"}], '2026-10-09') == 1
    assert contar_vencidos([{"card_id": "card_d", "due_at": None}], '2026-10-09') == 1
    assert contar_vencidos([], '2026-10-09') == 0

    print(resultado)
    print("Todos os testes passarm.")






