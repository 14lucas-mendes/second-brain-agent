
lista_status = [
    {"weak_point_id": "weak_01", "topic_id": "topic_python", "status": "active"},
    {"weak_point_id": "weak_02", "topic_id": "topic_python", "status": "active"},
    {"weak_point_id": "weak_03", "topic_id": "topic_sql", "status": "active"},
    {"weak_point_id": "weak_04", "topic_id": "topic_sql", "status": "resolved"},
    {"weak_point_id": "weak_05", "topic_id": "topic_git", "status": "active"},
    {"weak_point_id": "weak_06", "topic_id": "topic_javascript", "status": ""},
]


def verifica_status(lista, status):
    result = {}
    for item in lista:
        if status == "":
            return {}
        if item["status"] == status and item["weak_point_id"] != "" and item["topic_id"] != "":
            result[item["weak_point_id"]] = item["topic_id"]
        
    return result



if __name__ == "__main__":
    obtido = verifica_status(lista_status, "active")
    obtido_1 = verifica_status([{"weak_point_id": "weak_01", "topic_id": "topic_python", "status": "active"},
    {"weak_point_id": "weak_02", "topic_id": "topic_python", "status": "active"}], "active")
    obtido_2 = verifica_status([{"weak_point_id": "weak_04", "topic_id": "topic_sql", "status": "resolved"}], "resolved")
    obtido_3 = verifica_status([{"weak_point_id": "weak_06", "topic_id": "topic_javascript", "status": ""}], "active")
    obtido_4 = verifica_status([{"weak_point_id": "weak_02", "topic_id": "topic_python", "status": "active"}], "")
    obtido_5 = verifica_status([], "active")
    obtido_6 = verifica_status([{"weak_point_id": "", "topic_id": "topic_python", "status": "active"},
    {"weak_point_id": "weak_02", "topic_id": "topic_python", "status": "active"}], "active")
    obtido_7 = verifica_status([ {"weak_point_id": "weak_01", "topic_id": "topic_python", "status": "active"},
    {"weak_point_id": "weak_02", "topic_id": "", "status": "active"}], "active")




    esperado = {"weak_01": "topic_python", "weak_02": "topic_python", "weak_03": "topic_sql", "weak_05": "topic_git"}
    esperado_1 = {"weak_01": "topic_python", "weak_02": "topic_python"}
    esperado_2 = {"weak_04": "topic_sql"}
    esperado_3 = {}
    esperado_4 = {}
    esperado_5 = {}
    esperado_6 = {"weak_02":"topic_python"}
    esperado_7 = {"weak_01":"topic_python"}
    

    assert obtido == esperado, f"esperava {esperado}, recebido {obtido}"
    assert obtido_1 == esperado_1, f"esperava {esperado_1}, recebido {obtido_1}"
    assert obtido_2 == esperado_2, f"esperava {esperado_2}, recebido {obtido_2}"
    assert obtido_3 == esperado_3, f"esperava {esperado_3}, recebido {obtido_3}"
    assert obtido_4 == esperado_4, f"esperava {esperado_4}, recebdio {obtido_4}"
    assert obtido_5 == esperado_5, f"esperava {esperado_5}, recebdio {obtido_5}"
    assert obtido_6 == esperado_6, f"esperava {esperado_6}, recebdio {obtido_6}"
    assert obtido_7 == esperado_7, f"esperava {esperado_7}, recebdio {obtido_7}"

    print(obtido)
    print(obtido_1)
    print(obtido_2)
    print(obtido_3)
    print(obtido_4)
    print(obtido_5)
    print(obtido_6)
    print(obtido_7)
    print("Todos os testes passaram!")
    
