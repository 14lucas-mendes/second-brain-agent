
sessoes = [
    {"session_id": "s01", "data": "2026-10-01"},
    {"session_id": "s02", "data": "2026-10-04"},
    {"session_id": "s03", "data": "2026-10-09"},
    {"session_id": "s04", "data": "2026-10-12"},
    {"session_id": "s05", "data": "2026-10-18"},
    {"session_id": "s06", "data": "2026-10-23"},
    {"session_id": "s07", "data": "2026-10-30"},
    {"session_id": "s08", "data": "2026-11-02"},
]



def busca_data(lista, data):
    passos = 0
    if len(lista) == 0:
        return (None, passos)
    
    baixo = 0
    alto = len(lista) - 1

    # A busca binária exige lista ordenada. Comparar com o elemento do meio
    # descarta a metade impossível: alvo menor fica à esquerda, maior à direita.
    # Em lista não ordenada, a busca linear é a adequada.
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]["data"]

        if chute == data:
            passos += 1
            return (lista[meio]["session_id"], passos)
        if chute > data:
            passos += 1
            alto = meio - 1
        if chute < data:
            passos += 1
            baixo = meio + 1

    return (None, passos)


def busca_linear(lista, data):
    passos = 0
    if len(lista) == 0:
        return (None, passos)

    for item in lista:
        passos += 1
        if item["data"] == data:
            return (item["session_id"], passos)

    return (None, passos)


if __name__ == "__main__":
    uma = [{"session_id": "s01", "data": "2026-10-01"}]

    obtido = busca_data(sessoes, "2026-10-18")
    esperado = ("s05", 3)
    assert obtido == esperado, f"esperava {esperado}, obtido {obtido}"

    obtido_1 = busca_data([], "2026-10-18")
    esperado_1 = (None, 0)
    assert obtido_1 == esperado_1, f"esperava {esperado_1}, obtido {obtido_1}"

    obtido_2 = busca_data(sessoes, "2026-10-01")
    esperado_2 = ("s01", 3)
    assert obtido_2 == esperado_2, f"esperava {esperado_2}, obtido {obtido_2}"

    obtido_3 = busca_data(sessoes, "2026-11-02")
    esperado_3 = ("s08", 4)
    assert obtido_3 == esperado_3, f"esperava {esperado_3}, obtido {obtido_3}"

    obtido_4 = busca_data(sessoes, "2026-10-12")
    esperado_4 = ("s04", 1)
    assert obtido_4 == esperado_4, f"esperava {esperado_4}, obtido {obtido_4}"

    obtido_5 = busca_data(sessoes, "2026-10-15")
    esperado_5 = (None, 3)
    assert obtido_5 == esperado_5, f"esperava {esperado_5}, obtido {obtido_5}"

    obtido_6 = busca_data(sessoes, "2026-09-01")
    esperado_6 = (None, 3)
    assert obtido_6 == esperado_6, f"esperava {esperado_6}, obtido {obtido_6}"

    obtido_7 = busca_data(sessoes, "2026-12-01")
    esperado_7 = (None, 4)
    assert obtido_7 == esperado_7, f"esperava {esperado_7}, obtido {obtido_7}"

    obtido_8 = busca_data(uma, "2026-10-01")
    esperado_8 = ("s01", 1)
    assert obtido_8 == esperado_8, f"esperava {esperado_8}, obtido {obtido_8}"

    obtido_9 = busca_data(uma, "2026-10-18")
    esperado_9 = (None, 1)
    assert obtido_9 == esperado_9, f"esperava {esperado_9}, obtido {obtido_9}"

    assert busca_linear(sessoes, "2026-10-18") == ("s05", 5)
    assert busca_linear([], "2026-10-18") == (None, 0)
    assert busca_linear(sessoes, "2026-10-01") == ("s01", 1)
    assert busca_linear(sessoes, "2026-11-02") == ("s08", 8)
    assert busca_linear(sessoes, "2026-10-12") == ("s04", 4)
    assert busca_linear(sessoes, "2026-10-15") == (None, 8)
    assert busca_linear(sessoes, "2026-09-01") == (None, 8)
    assert busca_linear(sessoes, "2026-12-01") == (None, 8)
    assert busca_linear(uma, "2026-10-01") == ("s01", 1)
    assert busca_linear(uma, "2026-10-18") == (None, 1)

    print("Todos os testes passaram")
    print()
    print("Comparacao de passos - binaria x linear")
    datas_comparacao = [
        "2026-10-18",
        "2026-10-01",
        "2026-11-02",
        "2026-10-12",
        "2026-10-15",
    ]
    for data in datas_comparacao:
        id_bin, passos_bin = busca_data(sessoes, data)
        id_lin, passos_lin = busca_linear(sessoes, data)
        print(
            f"{data}: binaria={passos_bin} passo(s) -> {id_bin}; "
            f"linear={passos_lin} passo(s) -> {id_lin}"
        )

    id_bin, passos_bin = busca_data([], "2026-10-18")
    id_lin, passos_lin = busca_linear([], "2026-10-18")
    print(
        f"lista vazia: binaria={passos_bin} passo(s) -> {id_bin}; "
        f"linear={passos_lin} passo(s) -> {id_lin}"
    )