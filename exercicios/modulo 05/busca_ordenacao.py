cards = [
    {"card_id": "c1", "due_at": "2026-11-12"},
    {"card_id": "c2", "due_at": "2026-11-03"},
    {"card_id": "c3", "due_at": "2026-11-20"},
    {"card_id": "c4", "due_at": "2026-11-01"},
    {"card_id": "c5", "due_at": "2026-11-15"},
    {"card_id": "c6", "due_at": "2026-11-07"},
]

def ordena_data_cards(lista_cards):
    if len(lista_cards) == 0:
        return ([], 0)

    cards_copia = lista_cards.copy()
    comparacoes = 0
    n = len(cards_copia)

    for i in range(n - 1):
        index_menor = i

        for j in range(i + 1, n):
            comparacoes += 1
            if cards_copia[j]["due_at"] < cards_copia[index_menor]["due_at"]:
                index_menor = j
        cards_copia[i], cards_copia[index_menor] = cards_copia[index_menor], cards_copia[i]
    
    return (cards_copia, comparacoes)




if __name__ == "__main__":
    um = [{"card_id": "c1", "due_at": "2026-11-12"}]

    ja_ordenada = [
        {"card_id": "c4", "due_at": "2026-11-01"},
        {"card_id": "c2", "due_at": "2026-11-03"},
        {"card_id": "c6", "due_at": "2026-11-07"},
        {"card_id": "c1", "due_at": "2026-11-12"},
        {"card_id": "c5", "due_at": "2026-11-15"},
        {"card_id": "c3", "due_at": "2026-11-20"},
    ]

    inversa = [
        {"card_id": "c3", "due_at": "2026-11-20"},
        {"card_id": "c5", "due_at": "2026-11-15"},
        {"card_id": "c1", "due_at": "2026-11-12"},
        {"card_id": "c6", "due_at": "2026-11-07"},
        {"card_id": "c2", "due_at": "2026-11-03"},
        {"card_id": "c4", "due_at": "2026-11-01"},
    ]

    obtido, comparacoes = ordena_data_cards(cards)
    esperado = sorted(cards, key=lambda c: c["due_at"])
    assert obtido == esperado, f"esperava {esperado}, obtido {obtido}"
    assert comparacoes == 15, f"esperava 15, obtido {comparacoes}"

    obtido_1, comparacoes_1 = ordena_data_cards([])
    esperado_1 = []
    assert obtido_1 == esperado_1, f"esperava {esperado_1}, obtido {obtido_1}"
    assert comparacoes_1 == 0, f"esperava 0, obtido {comparacoes_1}"

    obtido_2, comparacoes_2 = ordena_data_cards(um)
    esperado_2 = [{"card_id": "c1", "due_at": "2026-11-12"}]
    assert obtido_2 == esperado_2, f"esperava {esperado_2}, obtido {obtido_2}"
    assert comparacoes_2 == 0, f"esperava 0, obtido {comparacoes_2}"

    obtido_3, comparacoes_3 = ordena_data_cards(ja_ordenada)
    esperado_3 = sorted(ja_ordenada, key=lambda c: c["due_at"])
    assert obtido_3 == esperado_3, f"esperava {esperado_3}, obtido {obtido_3}"
    assert comparacoes_3 == 15, f"esperava 15, obtido {comparacoes_3}"

    obtido_4, comparacoes_4 = ordena_data_cards(inversa)
    esperado_4 = sorted(inversa, key=lambda c: c["due_at"])
    assert obtido_4 == esperado_4, f"esperava {esperado_4}, obtido {obtido_4}"
    assert comparacoes_4 == 15, f"esperava 15, obtido {comparacoes_4}"

    print("Todos os testes passaram")
    print()
    print("3 cards mais atrasados:")
    for card in obtido[:3]:
        print(card["card_id"])

