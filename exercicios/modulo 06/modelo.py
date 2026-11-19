from dataclasses import dataclass, field

dados_cards = [
    {"card_id": "c1", "topic_id": "topic_python", "due_at": "2026-11-18", "review_count": 3, "last_result": "correct"},
    {"card_id": "c2", "topic_id": "topic_git", "due_at": "2026-11-19"},
    {"card_id": "c3", "topic_id": "topic_sql", "due_at": "2026-11-25", "review_count": 1, "last_result": "partial"},
]


@dataclass
class Card:
    card_id: str
    topic_id: str
    due_at: str
    review_count: int = 0
    last_result: str | None = None

    def vencido(self, data: str) -> bool:
        return self.due_at <= data


def converter_dicionarios(lista):
    cards = []
    for item in lista:
        cards.append(Card(**item))

    return cards


@dataclass
class Sessao:
    session_id: str
    started_at: str
    ended_at: str | None = None
    lesson_ids: list[str] = field(default_factory=list)

    def esta_aberta(self) -> bool:
        return self.ended_at is None


if __name__ == "__main__":
    cards = converter_dicionarios(dados_cards)

    # três objetos da conversão
    assert len(cards) == 3
    assert cards[0] == Card("c1", "topic_python", "2026-11-18", 3, "correct")
    assert cards[1] == Card("c2", "topic_git", "2026-11-19")  # defaults 0 e None
    assert cards[2] == Card("c3", "topic_sql", "2026-11-25", 1, "partial")

    # vencidos em 2026-11-19 (c2 = data igual)
    assert cards[0].vencido("2026-11-19") is True
    assert cards[1].vencido("2026-11-19") is True
    assert cards[2].vencido("2026-11-19") is False

    # dois cards iguais → True no ==
    assert Card("c1", "topic_python", "2026-11-18", 3, "correct") == Card(
        "c1", "topic_python", "2026-11-18", 3, "correct"
    )

    # sessão aberta e fechada
    aberta = Sessao("s1", "2026-11-19")
    fechada = Sessao("s2", "2026-11-19", ended_at="2026-11-19")
    assert aberta.esta_aberta() is True
    assert fechada.esta_aberta() is False

    # regra 6 — listas isoladas
    s_a = Sessao("sa", "2026-11-19")
    s_b = Sessao("sb", "2026-11-19")
    s_a.lesson_ids.append("lesson_1")
    assert s_a.lesson_ids == ["lesson_1"]
    assert s_b.lesson_ids == []

    print("Todos os testes passaram")