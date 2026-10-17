
lista = [
    {"evidence_id": "ev_01", "topic_id": "topic_python"},
    {"evidence_id": "ev_02", "topic_id": "topic_python"},
    {"evidence_id": "ev_03", "topic_id": "topic_sql"},
    {"evidence_id": "ev_04", "topic_id": "topic_sql"},
    {"evidence_id": "ev_05", "topic_id": "topic_git"},
    {"evidence_id": "", "topic_id": "topic_javascript"}
]

topicos = ["topic_python", "topic_sql", "topic_git", "topic_javascript"]



def calcular_topicos(lista, topicos):
    result = {}
    for topico in topicos:
        result[topico] = 0
        for item in lista:
            if topico == item["topic_id"] and item["evidence_id"] != "":
                result[topico] += 1

    return result 
            


if __name__ == "__main__":
    obtido_1 = (calcular_topicos(lista, topicos))
    obtido_2 = calcular_topicos([{"evidence_id": "ev_05", "topic_id": "topic_git"},
    {"evidence_id": "", "topic_id": "topic_javascript"}], ["topic_git", "topic_javascript"])
    obtido_3 = calcular_topicos([], ["topic_python", "topic_sql"])
    obtido_4 = calcular_topicos([{"evidence_id": "ev_01", "topic_id": "topic_python"}], [])
    
    case_1 = {
        "topic_python": 2,
        "topic_sql": 2,
        "topic_git": 1,
        "topic_javascript": 0
    }
    case_2 = {"topic_git": 1,
        "topic_javascript": 0}
    case_3 = {"topic_python": 0, "topic_sql": 0}
    case_4 = {}

    assert obtido_1 == case_1, f"esperava {case_1}, obtive{obtido_1}"
    assert obtido_2 == case_2, f"esperava {case_2}, obtido {obtido_2}"
    assert obtido_3 == case_3, f"esperava {case_3}, obtido {obtido_3}"
    assert obtido_4 == case_4, f"esperava {case_4}, obtido {obtido_4}"


    print("Todos os testes passaram")


























"""
Meu assert 1: caso normal

lista_evidencia = [
    {"evidence_id": "ev_01", "topic_id": "topic_python"},
    {"evidence_id": "ev_02", "topic_id": "topic_python"},
    {"evidence_id": "ev_03", "topic_id": "topic_sql"},
    {"evidence_id": "ev_04", "topic_id": "topic_sql"},
    {"evidence_id": "ev_05", "topic_id": "topic_git"},
    {"evidence_id": "", "topic_id": "javascript"}
]

topicos = ["python", "sql", "git"]

esperado = {
    "python": 2,
    "sql": 2,
    "git": 1,
}
"""


"""
Meu assert 2: possui um topico sem evidencia

lista_evidencia = [
    {"evidence_id": "ev_01", "topic_id": "topic_python"},
    {"evidence_id": "ev_02", "topic_id": "topic_python"},
    {"evidence_id": "ev_03", "topic_id": "topic_sql"},
    {"evidence_id": "ev_04", "topic_id": "topic_sql"},
    {"evidence_id": "ev_05", "topic_id": "topic_git"}, 
]

topicos = [["python", "sql", "git", "javascript"]

esperado = {
    "python": 2,
    "sql": 2,
    "git": 1,
    "javascript": 0
}
"""




