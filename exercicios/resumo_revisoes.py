import json

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
    # resumos (dict por card_id) + mais_acertos: as duas respostas do enunciado
    # num só valor; dict permite achar o card pelo id; None cobre sem data / sem cards.
    if len(cards) == 0:
        return {
            "resumos": {},
            "mais_acertos": None,
        }

    resumos = {}
    mais_acertos = None
    melhor_acertos = -1

    for card in cards:
        n_revisoes = len(card["revisoes"])
        acertos = 0
        ultima = None

        for revisao in card["revisoes"]:
            if revisao["resultado"] == "correct":
                acertos += 1
            if ultima is None or revisao["data"] > ultima:
                ultima = revisao["data"]

        resumos[card["card_id"]] = {
            "revisoes": n_revisoes,
            "acertos": acertos,
            "ultima": ultima,
        }

        if acertos > melhor_acertos:
            melhor_acertos = acertos
            mais_acertos = card["card_id"]

    return {"resumos": resumos, "mais_acertos": mais_acertos}


if __name__ == "__main__":
    esperado = {
        "resumos": {
            "card_a": {"revisoes": 3, "acertos": 2, "ultima": "2026-10-27"},
            "card_b": {"revisoes": 2, "acertos": 2, "ultima": "2026-10-26"},
            "card_c": {"revisoes": 0, "acertos": 0, "ultima": None},
        },
        "mais_acertos": "card_a",
    }

    obtido = resumo_revisoes(cards)
    assert obtido == esperado, f"esperava {esperado}, obtido {obtido}"

    # Grava o dict em texto JSON; "w" = escrever (cria/substitui o ficheiro)
    with open("indice.json", "w", encoding="utf-8") as arquivo:
        json.dump(obtido, arquivo, ensure_ascii=False, indent=2)


    # Lê de volta o mesmo ficheiro; "r" = ler
    with open("indice.json", "r", encoding="utf-8") as arquivo: 
        relido = json.load(arquivo)

    assert relido == esperado, f"indice.json relido diverge: esperava {esperado}, obtido {relido}"

    obtido_vazio = resumo_revisoes([])
    esperado_vazio = {"resumos": {}, "mais_acertos": None}
    assert obtido_vazio == esperado_vazio, f"esperava {esperado_vazio}, obtido {obtido_vazio}"

    obtido_um = resumo_revisoes([{"card_id": "card_a", "revisoes": []}])
    esperado_um = {
        "resumos": {
            "card_a": {"revisoes": 0, "acertos": 0, "ultima": None},
        },
        "mais_acertos": "card_a",
    }
    assert obtido_um == esperado_um, f"esperava {esperado_um}, obtido {obtido_um}"

    print("Todos os testes passaram")
    print("indice.json gravado")
