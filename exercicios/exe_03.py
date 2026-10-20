cards = [
    {"card_id": "card_01", "status": "learning", "due_at": "2026-10-18"},
    {"card_id": "card_02", "status": "new", "due_at": "2026-10-15"},
    {"card_id": "card_03", "status": "review", "due_at": "2026-10-20"},
    {"card_id": "card_04", "status": "learning", "due_at": "2026-10-22"},
    {"card_id": "card_05", "status": "new", "due_at": "2026-10-12"},
    {"card_id": "card_06", "status": "review", "due_at": "2026-10-25"},
]


def contar_vencidos_por_status(cards, hoje):
    result = {"new": 0, "learning": 0, "review": 0}
    for card in cards:
        vencido = card["due_at"] == None or card["due_at"] <= hoje
        if vencido and card["status"] in result:
            result[card["status"]] += 1
        print(card["card_id"], card["status"], card["due_at"], vencido, result)
    return result


if __name__ == "__main__":
    obtido = contar_vencidos_por_status(cards, "2026-10-20")
    esperado = {"new": 2, "learning": 1, "review": 1}
    assert obtido == esperado, f"esperava {esperado}, obtido {obtido}"

    obtido_1 = contar_vencidos_por_status(
        [{"card_id": "card_03", "status": "review", "due_at": "2026-10-20"}],
        "2026-10-20",
    )
    esperado_1 = {"new": 0, "learning": 0, "review": 1}
    assert obtido_1 == esperado_1, f"esperava {esperado_1}, obtido {obtido_1}"

    obtido_2 = contar_vencidos_por_status(
        [{"card_id": "card_04", "status": "learning", "due_at": "2026-10-22"}],
        "2026-10-20",
    )
    esperado_2 = {"new": 0, "learning": 0, "review": 0}
    assert obtido_2 == esperado_2, f"esperava {esperado_2}, obtido {obtido_2}"

    obtido_3 = contar_vencidos_por_status(
        [{"card_id": "card_07", "status": "new", "due_at": None}],
        "2026-10-20",
    )
    esperado_3 = {"new": 1, "learning": 0, "review": 0}
    assert obtido_3 == esperado_3, f"esperava {esperado_3}, obtido {obtido_3}"

    obtido_4 = contar_vencidos_por_status([], "2026-10-20")
    esperado_4 = {"new": 0, "learning": 0, "review": 0}
    assert obtido_4 == esperado_4, f"esperava {esperado_4}, obtido {obtido_4}"

    print("Todos os testes passaram")
