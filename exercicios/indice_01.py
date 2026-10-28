topicos = ["topic_python", "topic_sql", "topic_git"]

evidencias = [
    {"evidence_id": "ev_01", "topic_id": "topic_python"},
    {"evidence_id": "ev_02", "topic_id": "topic_git"},
    {"evidence_id": "ev_03", "topic_id": "topic_python"},
    {"evidence_id": "ev_04", "topic_id": "topic_react"},
]


def classificar_indice(evidencias, topicos):
    result = {}
    for topico in topicos:
        result[topico] = []

    # Escolhi dicionario com lista por que assim eu olho o topico e ja vejo a lista dele.
    # A lista guarda a ordem das evidencias e aceita zero ou varias por topico.
    if len(evidencias) == 0:
        return result
    
    for evidencia in evidencias:
        if evidencia["topic_id"] in result:
            result[evidencia["topic_id"]].append(evidencia["evidence_id"])
    

    return result


if __name__ == "__main__":
    obtido = classificar_indice(evidencias, topicos)
    esperado = {
        "topic_python": ["ev_01", "ev_03"],
        "topic_sql": [],
        "topic_git": ["ev_02"],
    }
    assert obtido == esperado, f"esperava {esperado}, obtido {obtido}"

    obtido_1 = classificar_indice(
        [{"evidence_id": "ev_01", "topic_id": "topic_python"}],
        [],
    )
    esperado_1 = {}
    assert obtido_1 == esperado_1, f"esperava {esperado_1}, obtido {obtido_1}"

    obtido_2 = classificar_indice(
        [],
        ["topic_python", "topic_git"],
    )
    esperado_2 = {
        "topic_python": [],
        "topic_git": [],
    }
    assert obtido_2 == esperado_2, f"esperava {esperado_2}, obtido {obtido_2}"

    obtido_3 = classificar_indice([], [])
    esperado_3 = {}
    assert obtido_3 == esperado_3, f"esperava {esperado_3}, obtido {obtido_3}"

    obtido_4 = classificar_indice(
        [
            {"evidence_id": "ev_03", "topic_id": "topic_python"},
            {"evidence_id": "ev_01", "topic_id": "topic_python"},
        ],
        ["topic_python"],
    )
    esperado_4 = {
        "topic_python": ["ev_03", "ev_01"],
    }
    assert obtido_4 == esperado_4, f"esperava {esperado_4}, obtido {obtido_4}"

    print("Todos os testes passaram")