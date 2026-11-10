# Explicação do `busca_ordenacao.py` passo a passo

Relacionado: [[busca_ordenacao]] (enunciado) · `busca_ordenacao.py` (código)

Resumo: a função `ordena_data_cards` implementa o **selection sort** (ordenação por seleção). A ideia é simples: a cada rodada, procurar o card com a data mais antiga entre os que ainda não foram ordenados e colocá-lo na próxima posição livre do início da lista.

---

## 1. A ideia antes do código

Pense em 6 cartas espalhadas na mesa, cada uma com uma data. Você quer enfileirá-las da mais antiga para a mais nova. Um jeito humano de fazer isso:

1. Olhe **todas** as cartas e ache a mais antiga. Coloque-a na posição 0.
2. Olhe **todas as que sobraram** e ache a mais antiga. Coloque-a na posição 1.
3. Repita até sobrar uma carta só, que já estará no lugar certo.

Esse é o selection sort. O nome vem do fato de que, a cada rodada, você **seleciona** o menor elemento do que falta.

A ideia central, chamada de **invariante**, é esta: no começo da rodada `i`, as posições `0` até `i-1` já estão ordenadas e **definitivas**. Nada que aconteça depois vai mexer nelas. Toda a estrutura do código serve para manter essa promessa.

```
rodada i=2:   [ ordenado e fixo | ainda bagunçado ]
               pos 0, 1          pos 2 ... n-1
                                 ^ i: aqui vai entrar o menor da parte bagunçada
```

---

## 2. Leitura linha por linha

### O caso da lista vazia (linhas 10–12)

```python
def ordena_data_cards(lista_cards):
    if len(lista_cards) == 0:
        return ([], 0)
```

Se não há nada para ordenar, a função devolve logo a tupla `([], 0)`, como pede o enunciado.

Detalhe de debug: essa guarda nem é estritamente necessária. Sem ela, `n` seria 0, `range(-1)` não executaria nenhuma volta e a função devolveria `([], 0)` do mesmo jeito. Ela deixa a intenção explícita, o que é bom, mas vale saber que o algoritmo já trata esse caso sozinho. O caso de um card só também não precisa de `if`: com `n = 1`, `range(0)` não executa nada e o resultado sai com 0 comparações.

### A cópia (linhas 14–16)

```python
    cards_copia = lista_cards.copy()
    comparacoes = 0
    n = len(cards_copia)
```

- **`lista_cards.copy()`**: a regra 3 proíbe alterar a lista de entrada. Se você ordenasse `lista_cards` diretamente, quem chamou a função veria a lista dele bagunçada depois. A cópia cria uma **lista nova**, e as trocas acontecem nela.
- Atenção: essa cópia é **rasa**. A lista é nova, mas os dicionários dentro dela são **os mesmos objetos** da original. Isso basta aqui, porque o algoritmo só muda os cards de **posição** e nunca edita um card por dentro. Se você fizesse algo como `cards_copia[0]["due_at"] = "..."`, a lista original também mudaria.
- **`comparacoes = 0`**: é o contador que a regra 4 exige.
- **`n`**: guarda o tamanho da lista para não recalcular e para deixar os `range` mais legíveis.

### Laço externo: qual posição está sendo preenchida (linhas 18–19)

```python
    for i in range(n - 1):
        index_menor = i
```

- `i` é a **posição que está sendo preenchida** nesta rodada.
- **Por que `n - 1` e não `n`?** Quando as posições `0` a `n-2` estão corretas, sobra um único elemento na última posição, e ele só pode ser o maior. Uma rodada a mais compararia o elemento com nada.
- **`index_menor = i`**: no começo, você chuta que o menor da parte bagunçada é o primeiro dela. É o "campeão provisório".
- **Por que guardar o índice e não o card?** Porque no fim da rodada é preciso **trocar de posição**, e para isso é preciso saber *onde* o menor está. Com o card em mãos, você não saberia de onde tirá-lo.

### Laço interno: o torneio pelo menor (linhas 21–24)

```python
        for j in range(i + 1, n):
            comparacoes += 1
            if cards_copia[j]["due_at"] < cards_copia[index_menor]["due_at"]:
                index_menor = j
```

- **`j` começa em `i + 1`**: a posição `i` já é o campeão provisório, e tudo antes de `i` está fixo (o invariante). Comparar com essas posições seria desperdício.
- **`comparacoes += 1` vem antes do `if`**: cada volta do laço interno faz exatamente uma comparação de datas, seja o resultado verdadeiro ou falso. Por isso o contador fica fora da condição. Se estivesse dentro do `if`, contaria só as vezes em que achou um card menor, o que é outra métrica.
- **Comparar datas como texto funciona?** Funciona, porque o formato `AAAA-MM-DD` tem largura fixa e zeros à esquerda. A comparação de strings é feita caractere por caractere, da esquerda para a direita, então primeiro decide o ano, depois o mês, depois o dia. Exatamente a ordem cronológica. Se alguém escrevesse `"2026-11-3"` sem o zero, a comparação quebraria: `"2026-11-3" > "2026-11-12"`, porque o caractere `'3'` é maior que `'1'`.
- **`<` estrito**: troca de campeão só quando o desafiante é *realmente* menor. Em caso de empate, fica o primeiro encontrado.

### A troca: colocar o menor no lugar (linhas 25–27)

```python
        cards_copia[i], cards_copia[index_menor] = cards_copia[index_menor], cards_copia[i]

    return (cards_copia, comparacoes)
```

- Repare na indentação: a troca fica **dentro do `for i`** e **fora do `for j`**. Ela acontece uma vez por rodada, só depois que o torneio terminou. Se estivesse dentro do `for j`, trocaria no meio da busca e o algoritmo viraria outra coisa.
- A sintaxe `a, b = b, a` é a troca do Python. O lado direito é avaliado inteiro primeiro, montando uma tupla, e só depois é atribuído. Por isso não é preciso variável auxiliar.
- Se `index_menor == i`, a troca é com ele mesmo. É inofensiva, só não faz nada.
- O `return` fica fora dos dois laços e devolve a tupla `(lista, int)` pedida no enunciado.

---

## 3. Executando no "debugger" (caso normal)

Estado inicial de `cards_copia` (mostrando só o id e o dia de novembro):

```
pos:   0      1      2      3      4      5
     c1:12  c2:03  c3:20  c4:01  c5:15  c6:07
```

**Rodada i = 0** (campeão inicial: pos 0, dia 12)

```
j=1: 03 < 12? SIM → index_menor = 1   (comparacoes = 1)
j=2: 20 < 03? não                     (2)
j=3: 01 < 03? SIM → index_menor = 3   (3)
j=4: 15 < 01? não                     (4)
j=5: 07 < 01? não                     (5)
troca pos 0 ↔ pos 3
     c4:01 | c2:03  c3:20  c1:12  c5:15  c6:07
```

**Rodada i = 1** (campeão inicial: pos 1, dia 03)

```
j=2: 20 < 03? não   (6)
j=3: 12 < 03? não   (7)
j=4: 15 < 03? não   (8)
j=5: 07 < 03? não   (9)
troca pos 1 ↔ pos 1 (nada muda)
     c4:01  c2:03 | c3:20  c1:12  c5:15  c6:07
```

**Rodada i = 2** (campeão inicial: pos 2, dia 20)

```
j=3: 12 < 20? SIM → index_menor = 3   (10)
j=4: 15 < 12? não                     (11)
j=5: 07 < 12? SIM → index_menor = 5   (12)
troca pos 2 ↔ pos 5
     c4:01  c2:03  c6:07 | c1:12  c5:15  c3:20
```

**Rodada i = 3** (campeão inicial: pos 3, dia 12)

```
j=4: 15 < 12? não   (13)
j=5: 20 < 12? não   (14)
troca 3 ↔ 3 (nada muda)
```

**Rodada i = 4** (campeão inicial: pos 4, dia 15)

```
j=5: 20 < 15? não   (15)
troca 4 ↔ 4 (nada muda)
```

O laço termina aqui, porque `range(5)` vai só até 4. A posição 5 sobrou e já está certa.

```
resultado: c4:01  c2:03  c6:07  c1:12  c5:15  c3:20
comparacoes = 15
```

O resultado bate com a tabela do enunciado, e os 3 mais atrasados são `c4`, `c2` e `c6`.

---

## 4. Por que sempre dá 15 comparações?

O laço interno dá 5, 4, 3, 2 e 1 voltas em cada rodada. Isso **não depende dos dados**, só de `n`. O selection sort clássico não tem nenhuma "saída antecipada": mesmo que a lista já esteja ordenada, ele precisa conferir todo o resto para *ter certeza* de que achou o menor.

$$
(n-1) + (n-2) + \dots + 1 = \frac{n(n-1)}{2} = \frac{6 \cdot 5}{2} = 15
$$

Por isso os asserts com `ja_ordenada` e `inversa` também esperam 15. O que muda entre esses casos é o **número de trocas efetivas**: na lista já ordenada, todas as trocas são com o próprio elemento; na inversa, várias trocam de verdade. O selection sort é $O(n^2)$ em comparações em qualquer caso, mas faz no máximo $n-1$ trocas. Essa é a vantagem dele quando trocar elementos custa caro.

---

## 5. O programa principal e os testes

```python
if __name__ == "__main__":
```

Esse bloco só roda quando o arquivo é executado diretamente. Se outro arquivo fizer `import busca_ordenacao`, os testes não disparam.

Os testes cobrem cada tipo de caso:

- **Normal** (`cards`): confere a lógica geral.
- **Vazia** (`[]`): confere a guarda do início.
- **Um card** (`um`): confere que `range(0)` não faz nada e dá 0 comparações.
- **Já ordenada**: prova que o algoritmo não tem atalho e continua fazendo 15 comparações.
- **Inversa**: o caso com mais trocas reais.

O resultado é conferido contra `sorted(...)`, que serve de **oráculo**: uma resposta confiável para comparar com a sua. As comparações são conferidas contra números calculados à mão.

No fim, `obtido[:3]` fatia os 3 primeiros da lista ordenada do caso normal, que são os mais atrasados.

---

## 6. Pegadinha: empates

O selection sort **não é estável**. Se dois cards tiverem a mesma data, a troca pode inverter a ordem original entre eles. Exemplo:

```
[A:05, B:05, C:01]
i=0 → menor é C → troca pos 0 ↔ pos 2 → [C:01, B:05, A:05]
```

A vinha antes de B e agora está depois. Já o `sorted` do Python é estável e manteria A antes de B. Ou seja, se um dia houver datas repetidas nos testes, o assert `obtido == esperado` pode falhar **mesmo com a ordenação correta por data**. Hoje isso não acontece porque nenhuma data se repete.

---

## Resumo para o caderno

| Peça do código | Por que existe |
|---|---|
| `.copy()` | Não alterar a lista de quem chamou |
| `for i in range(n - 1)` | Posição sendo preenchida; a última se resolve sozinha |
| `index_menor = i` | Campeão provisório; guarda o índice para poder trocar depois |
| `for j in range(i + 1, n)` | Procura só na parte ainda bagunçada |
| `comparacoes += 1` fora do `if` | Toda comparação conta, verdadeira ou falsa |
| Troca fora do `for j` | Só troca depois que o torneio inteiro terminou |
| Strings `AAAA-MM-DD` | A ordem alfabética coincide com a cronológica |

**Exercício para fixar:** troque o `<` por `>` e preveja, antes de rodar, o que acontece com a ordem e com o número de comparações.
