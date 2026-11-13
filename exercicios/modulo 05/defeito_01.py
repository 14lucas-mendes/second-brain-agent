topicos = ["topic_python", "topic_sql", "topic_git"]

evidencias = [
    {"evidence_id": "ev_01", "topic_id": "topic_python"},
    {"evidence_id": "ev_02", "topic_id": "topic_git"},
    {"evidence_id": "ev_03", "topic_id": "topic_python"},
    {"evidence_id": "ev_04", "topic_id": "topic_react"},
]


def classificar_indice(evidencias, topicos):
    """Para cada topico, os IDs das evidencias dele, na ordem de evidencias."""
    result = {}
    for topico in topicos:
        result[topico] = []
    for evidencia in evidencias:
        topico = evidencia["topic_id"]
        if topico in result:
            result[topico] += [evidencia["evidence_id"]]
    return result


if __name__== "__main__":
    obtido = classificar_indice(evidencias, topicos)
    esperado = {"topic_python": ["ev_01", "ev_03"], "topic_sql": [], "topic_git": ["ev_02"]}

    assert obtido == esperado, f"esparava {esperado}, obtido {obtido}"

    print("Todos os testes passaram")
    
