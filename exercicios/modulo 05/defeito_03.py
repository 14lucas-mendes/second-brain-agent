tentativas = [
    {"topic_id": "topic_python", "outcome": "correct", "support_level": 0},
    {"topic_id": "topic_python", "outcome": "partial", "support_level": 0},
    {"topic_id": "topic_git", "outcome": "incorrect", "support_level": 0},
    {"topic_id": "topic_git", "outcome": "correct", "support_level": 2},
    {"topic_id": "topic_python", "outcome": "correct", "support_level": 2},
    {"topic_id": "topic_sql", "outcome": "correct", "support_level": 0},
]


def taxa_sem_pista(tentativas):
    """Por topico: tentativas, acertos sem pista e a taxa (%) arredondada."""
    resumo = {}
    for t in tentativas:
        topico = t["topic_id"]
        if topico not in resumo:
            resumo[topico] = {"tentativas": 0, "acertos_sem_pista": 0}
        resumo[topico]["tentativas"] += 1
        if t["outcome"] == "correct" and t["support_level"] == 0:
            resumo[topico]["acertos_sem_pista"] += 1
    for topico, r in resumo.items():
        r["taxa"] = round(r["acertos_sem_pista"] * 100 / r["tentativas"])
    return resumo


for topico, r in taxa_sem_pista(tentativas).items():
    print(topico, r)


if __name__ == "__main__":
    obtido = taxa_sem_pista(tentativas)
    
    esperado = {"topic_python": {"tentativas": 3, "acertos_sem_pista": 1, "taxa": 33}, "topic_git": {"tentativas": 2, "acertos_sem_pista": 0, "taxa": 0}, "topic_sql": {"tentativas": 1, "acertos_sem_pista": 1, "taxa": 100}}


    assert obtido == esperado, f"esperado {esperado}, obtido {obtido}"

    print("Todos os testes passaram")