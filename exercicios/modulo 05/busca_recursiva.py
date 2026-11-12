licoes = [
    {"lesson_id": "l01", "concluida_em": "2026-09-07"},
    {"lesson_id": "l03", "concluida_em": "2026-09-12"},
    {"lesson_id": "l04", "concluida_em": "2026-09-17"},
    {"lesson_id": "l02", "concluida_em": "2026-10-06"},
    {"lesson_id": "l15", "concluida_em": "2026-10-23"},
    {"lesson_id": "l16", "concluida_em": "2026-10-31"},
    {"lesson_id": "l17", "concluida_em": "2026-11-20"},
]


def busca_licao(licoes, data, esquerda=0, direita=None):
    # Casos-base: (1) esquerda > direita → trecho vazio, data não está na lista → None;
    # (2) chute == data → achou → devolve o lesson_id.
    # O problema fica menor porque cada chamada descarta o meio e uma das metades
    # (direita = meio - 1 ou esquerda = meio + 1), então o trecho encolhe pelo menos 1
    # e cai pela metade até chegar a um caso-base.
    if direita is None:
        direita = len(licoes) - 1

    if esquerda > direita:
        return None

    meio = (esquerda + direita) // 2
    chute = licoes[meio]["concluida_em"]

    if chute == data:
        return licoes[meio]["lesson_id"]

    if chute > data:
        return busca_licao(licoes, data, esquerda, meio - 1)
    else:
        return busca_licao(licoes, data, meio + 1, direita)


if __name__ == "__main__":
    licoes_original = [dict(card) for card in licoes]

    uma = [{"lesson_id": "l01", "concluida_em": "2026-09-07"}]

    obtido = busca_licao(licoes, "2026-10-06")
    assert obtido == "l02", f"esperava 'l02', obtido {obtido}"

    obtido_1 = busca_licao(licoes, "2026-09-07")
    assert obtido_1 == "l01", f"esperava 'l01', obtido {obtido_1}"

    obtido_2 = busca_licao(licoes, "2026-11-20")
    assert obtido_2 == "l17", f"esperava 'l17', obtido {obtido_2}"

    obtido_3 = busca_licao(licoes, "2026-09-01")
    assert obtido_3 is None, f"esperava None, obtido {obtido_3}"

    obtido_4 = busca_licao(licoes, "2026-10-15")
    assert obtido_4 is None, f"esperava None, obtido {obtido_4}"

    obtido_5 = busca_licao(licoes, "2026-12-01")
    assert obtido_5 is None, f"esperava None, obtido {obtido_5}"

    obtido_6 = busca_licao([], "2026-10-06")
    assert obtido_6 is None, f"esperava None, obtido {obtido_6}"

    obtido_7 = busca_licao(uma, "2026-09-07")
    assert obtido_7 == "l01", f"esperava 'l01', obtido {obtido_7}"

    obtido_8 = busca_licao(uma, "2026-10-06")
    assert obtido_8 is None, f"esperava None, obtido {obtido_8}"

    assert licoes == licoes_original, "a lista original foi alterada"

    print("Todos os testes passaram")
