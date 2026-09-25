# Marco 2

## Construção do Grafo

### Compreensão de entrada

```txt
5
2 8 0 6 0
6
1 4
1 3
2 4
3 4
4 5
5 1
```

A primeira linha representa o **número de vértices** presentes no grafo, nesse caso, 5 vértices. Após ela existem 5 valores (referentes aos 5 vértices) que representam os custos associados a construção de um checkpoint em cada vértice, sendo esses os valores representados no grafo.

Então, na construção dos dados para a resolução do problema, os valores presentes na lista de adjacência representam um "identificador do vértice", enquanto os valores de custos serão armazenados em uma lista de mesmo tamanho da quantidade de vértices.

A terceira linha representa o número de arestas presentes, seguida por essa quantidade de linhas indicando as conexões entre os vértices.

### Construção Gradual da Representação do Grafo

Nessa seção, será realizada a construção simultânea da Representação Gráfica do Grafo, assim como a Lista de Adjacência associada.

#### Passo 1: Criação/Declaração dos vértices

Na entrada da instânica, nota-se 5 vértices, sendo caracterizados pelos valores de 1 até 5. Então, para a representação gráfica inicial temos:

```mermaid
flowchart LR 
  A((1))
  B((2))
  C((3))
  D((4))
  E((5))
```

Além disso, para a representação da Lista de Adjacência, como ainda não há nenhuma aresta presente, temos:

|Vértice|Vértices Adjacêntes|
|:-:|:-- |
|1||
|2||
|3||
|4||
|5||

#### Passo 2: Armazenamento dos valores de custo

No armazenamento dos valores de custo para a solução do problema será utilizada uma lista, mas para facilitar a compreensão do grafo os vértices terão entre parentêses o custo. Logo:

```py
custos = [2, 8, 0, 6, 0]
```

```mermaid
flowchart LR 
  A(("1(2)"))
  B(("2(8)"))
  C(("3(0)"))
  D(("4(6)"))
  E(("5(0)"))
```

#### Passo 3: Ligação Vértice _1_ e _4_

Para a ligação entre vértices 1 e 4, assumindo um grafo não-direcionado, temos:

**Representação Gráfica:** Ligando os vértices 1 e 4.

```mermaid
flowchart LR 
  A(("1(2)"))
  B(("2(8)"))
  C(("3(0)"))
  D(("4(6)"))
  E(("5(0)"))

  A --- D
```

**Lista de Adjacência:** Adicionando 4 na lista de vértices adjacêntes do 1 e o vértice 1 na lista do 4.

|Vértice|Vértices Adjacêntes|
|:-:|:--|
|1|4|
|2||
|3||
|4|1|
|5||

#### Passo 4: Ligação Vértice _1_ e _3_

Para a ligação entre vértices 1 e 3, assumindo um grafo não-direcionado, temos:

**Representação Gráfica:** Ligando os vértices 1 e 3.

```mermaid
flowchart LR 
  A(("1(2)"))
  B(("2(8)"))
  C(("3(0)"))
  D(("4(6)"))
  E(("5(0)"))

  A --- D
  A --- C
```

**Lista de Adjacência:** Adicionando 3 na lista de vértices adjacêntes do 1 e o vértice 1 na lista do 3.

|Vértice|Vértices Adjacêntes|
|:-:|:--|
|1|4, 3|
|2||
|3|1|
|4|1|
|5||

#### Passo 5: Ligação Vértice _2_ e _4_

Para a ligação entre vértices 2 e 4, assumindo um grafo não-direcionado, temos:

**Representação Gráfica:** Ligando os vértices 2 e 4.

```mermaid
flowchart LR 
  A(("1(2)"))
  B(("2(8)"))
  C(("3(0)"))
  D(("4(6)"))
  E(("5(0)"))

  A --- D
  A --- C
  B --- D
```

**Lista de Adjacência:** Adicionando 4 na lista de vértices adjacêntes do 2 e o vértice 2 na lista do 4.

|Vértice|Vértices Adjacêntes|
|:-:|:--|
|1|4, 3|
|2|4|
|3|1|
|4|1, 2|
|5||

#### Passo 6: Ligação Vértice _3_ e _4_

Para a ligação entre vértices 3 e 4, assumindo um grafo não-direcionado, temos:

**Representação Gráfica:** Ligando os vértices 3 e 4.

```mermaid
flowchart LR 
  A(("1(2)"))
  B(("2(8)"))
  C(("3(0)"))
  D(("4(6)"))
  E(("5(0)"))

  A --- D
  A --- C
  B --- D
  C --- D
```

**Lista de Adjacência:** Adicionando 4 na lista de vértices adjacêntes do 3 e o vértice 3 na lista do 4.

|Vértice|Vértices Adjacêntes|
|:-:|:--|
|1|4, 3|
|2|4|
|3|1, 4|
|4|1, 2, 3|
|5||

#### Passo 7: Ligação Vértice _4_ e _5_

Para a ligação entre vértices 4 e 5, assumindo um grafo não-direcionado, temos:

**Representação Gráfica:** Ligando os vértices 4 e 5.

```mermaid
flowchart LR 
  A(("1(2)"))
  B(("2(8)"))
  C(("3(0)"))
  D(("4(6)"))
  E(("5(0)"))

  A --- D
  A --- C
  B --- D
  C --- D
  D --- E
```

**Lista de Adjacência:** Adicionando 5 na lista de vértices adjacêntes do 4 e o vértice 4 na lista do 5.

|Vértice|Vértices Adjacêntes|
|:-:|:--|
|1|4, 3|
|2|4|
|3|1, 4|
|4|1, 2, 3, 5|
|5|4|

#### Passo 8: Ligação Vértice _5_ e _1_

Para a ligação entre vértices 5 e 1, assumindo um grafo não-direcionado, temos:

**Representação Gráfica:** Ligando os vértices 5 e 1.

```mermaid
flowchart LR 
  A(("1(2)"))
  B(("2(8)"))
  C(("3(0)"))
  D(("4(6)"))
  E(("5(0)"))

  A --- D
  A --- C
  B --- D
  C --- D
  D --- E
  E --- A
```

**Lista de Adjacência:** Adicionando 1 na lista de vértices adjacêntes do 5 e o vértice 5 na lista do 1.

|Vértice|Vértices Adjacêntes|
|:-:|:--|
|1|4, 3, 5|
|2|4|
|3|1, 4|
|4|1, 2, 3, 5|
|5|4, 1|

### Grafo e Lista de Adjacência

Com isso, temos a representação final do **grafo** e da **lista de adjacência**:

**Grafo**:

```mermaid
flowchart LR 
  A(("1(2)"))
  B(("2(8)"))
  C(("3(0)"))
  D(("4(6)"))
  E(("5(0)"))

  A --- D
  A --- C
  B --- D
  C --- D
  D --- E
  E --- A
```

**Lista de Adjacência**:

|Vértice|Vértices Adjacêntes|
|:-:|:--|
|1|4, 3, 5|
|2|4|
|3|1, 4|
|4|1, 2, 3, 5|
|5|4, 1|


## DFS e Identificação das Componentes Conexas


### Estruturas de Dados Utilizadas

Para o algoritmo de identificação de componentes conexas, além da lista de adjacência já construída, são usadas:
 
- **Lista de adjacência** `adj[]`: já construída nos Passos 1-8 (grafo não-direcionado).
- **Vetor `visitado[]`** (tamanho `n`): marca se cada vértice já foi visitado pela DFS, evitando revisitas e loops infinitos.
- **Vetor `componente[]`** (tamanho `n`): guarda o identificador da componente à qual cada vértice pertence. É o resultado principal do algoritmo.
- **Pilha de recursão (implícita)**: a própria DFS recursiva usa a pilha de chamadas da linguagem para "voltar" a um vértice anterior quando todos os vizinhos do vértice atual já foram explorados.
- **Contador `numComponentes`**: inicia em 0 e é incrementado toda vez que a DFS é iniciada a partir de um vértice ainda não visitado, no laço externo do algoritmo.

### Rastreamento da DFS Recursiva

Laço externo: percorre os vértices de 1 a 5; ao encontrar um vértice não visitado, inicia uma nova DFS e um novo id de componente.
 
Usando a lista de adjacência final (Passo 8):
 
| Vértice | Adjacentes |
|:-:|:--|
|1|4, 3, 5|
|2|4|
|3|1, 4|
|4|1, 2, 3, 5|
|5|4, 1|
 
**Início:** vértice 1 não visitado → `componente[1] = 1`, `numComponentes = 1`.
 
| Chamada | Ação | `visitado` após ação |
|:--|:--|:--|
| DFS(1) | marca 1 visitado; vizinhos [4, 3, 5] | {1} |
| → DFS(4) | 1º vizinho de 1; marca 4 visitado; vizinhos [1, 2, 3, 5] | {1, 4} |
| → → DFS(2) | 1 já visitado ignorado; vai a 2; marca 2 visitado; vizinhos [4]; 4 já visitado → **termina 2** | {1, 4, 2} |
| → volta a 4 | próximo vizinho: 3 | — |
| → → DFS(3) | marca 3 visitado; vizinhos [1, 4], ambos já visitados → **termina 3** | {1, 4, 2, 3} |
| → volta a 4 | próximo vizinho: 5 | — |
| → → DFS(5) | marca 5 visitado; vizinhos [4, 1], ambos já visitados → **termina 5** | {1, 4, 2, 3, 5} |
| → sem mais vizinhos → **termina 4** | | |
| volta a 1 | próximos vizinhos 3 e 5 já visitados → **termina 1** | |
 
Todos os 5 vértices foram alcançados por essa única chamada de DFS(1), então todos recebem `componente = 1`. O laço externo verifica os vértices restantes (2, 3, 4, 5) e encontra todos já visitados — nenhuma nova DFS é disparada.
 
```mermaid
flowchart LR 
  A(("1(2)"))
  B(("2(8)"))
  C(("3(0)"))
  D(("4(6)"))
  E(("5(0)"))
 
  A --- D
  A --- C
  B --- D
  C --- D
  D --- E
  E --- A
 
  classDef comp1 fill:#2d68ad,stroke:#2d68ad,stroke-width:1px,color:#fff
  class A,B,C,D,E comp1
```
 
### Identificação das Componentes Conexas
 
A lógica é: um laço externo percorre todos os vértices de 1 a `n`; sempre que encontra um vértice ainda não marcado em `visitado[]`, isso significa que ele pertence a uma componente ainda não descoberta. O algoritmo então incrementa `numComponentes` e dispara uma DFS a partir desse vértice, marcando **todos os vértices alcançáveis** por arestas (diretamente ou por caminhos) com esse mesmo id em `componente[]`. Como o grafo é não-direcionado, "alcançável" é uma relação simétrica: se `u` alcança `v`, `v` também alcança `u` — por isso cada DFS captura a componente inteira de uma vez, sem sobreposição com as demais.
 
No exemplo, como o vértice 4 tem grau alto (conectado a 1, 2, 3 e 5), a primeira DFS (a partir do vértice 1) já alcança todos os outros vértices. Resultado:
 
| Componente | Vértices |
|:-:|:--|
| C1 | {1, 2, 3, 4, 5} |
 
`numComponentes = 1` — o grafo é totalmente conexo.

### Complexidade de Tempo e Espaço
 
**Tempo — O(n + m):**
 
- O laço externo percorre os `n` vértices, e cada iteração faz apenas uma checagem O(1) (`if (!visitado[v])`), custando **O(n)** ao todo, sem contar as DFS disparadas.
- Dentro da DFS, cada vértice é marcado como visitado **exatamente uma vez** (a checagem `visitado[]` no início da função impede reprocessamento), custando **O(n)** no total para todos os vértices.
- Cada vértice, ao ser visitado, percorre sua lista de adjacência inteira. Como o grafo é não-direcionado, cada aresta aparece duas vezes na estrutura (uma em `adj[u]`, outra em `adj[v]`), totalizando `2m` entradas examinadas ao longo de toda a execução — **O(m)**.
Somando: **O(n) + O(m) = O(n + m)**. Esse é o melhor tempo possível, já que apenas ler a entrada (todos os vértices e arestas) já custa O(n + m).
 
**Espaço — O(n + m):**
 
| Estrutura | Tamanho | Motivo |
|:--|:-:|:--|
| Lista de adjacência `adj[]` | O(n + m) | `n` listas contendo juntas `2m` referências a vizinhos |
| `visitado[]` | O(n) | um booleano por vértice |
| `componente[]` | O(n) | um inteiro por vértice |
| Pilha de recursão da DFS | O(n) no pior caso | profundidade limitada pelo maior caminho simples percorrido sem retroceder; no pior caso (grafo em forma de corrente) chega a O(n) |
 
Somando tudo, o espaço total é **O(n + m)**, dominado pela lista de adjacência.
 
### Custo das Consultas de Conectividade
 
O custo deve ser analisado em duas fases:
 
**Fase 1 — pré-processamento (uma única vez):** executar o algoritmo de componentes conexas por completo, custando **O(n + m)**, preenchendo o vetor `componente[]`.
 
**Fase 2 — cada consulta "u e v estão conectados?" após o pré-processamento:**
 
```
mesmaComponente(u, v) = (componente[u] == componente[v])
```
 
Uma simples comparação de dois inteiros já calculados: **O(1)** por consulta, independentemente do tamanho do grafo.
 
**Comparação com a alternativa ingênua:** sem pré-processamento, responder "u alcança v?" exigiria uma nova BFS/DFS a partir de `u` a cada pergunta, custando O(n + m) **por consulta**. Para `q` perguntas, isso daria O(q · (n + m)) no total.
 
Com o pré-processamento, o custo total para `q` perguntas é:
 
```
O(n + m)   ← feito uma vez, no início
   +
O(q)       ← O(1) por pergunta, vezes q perguntas
```
 
ou seja, **O(n + m + q)** no total, em vez de **O(q · (n + m))** — o que justifica manter `componente[]` como estrutura auxiliar.

## Análise Matemática do Grafo

Para esta análise, considera-se o grafo adaptado para **simples e não direcionado**, conforme exigido no Marco 2.

A partir da entrada escolhida, temos as seguintes arestas:

```text
1 - 4
1 - 3
2 - 4
3 - 4
4 - 5
5 - 1
```

O grafo é conexo, pois existe um caminho entre qualquer par de vértices. Dessa forma, há apenas uma componente conexa:

```text
C1 = {1, 2, 3, 4, 5}
```

### Distâncias entre os Vértices

A distância entre dois vértices corresponde ao comprimento do caminho mais curto entre eles.

As menores distâncias entre os vértices são:

| Vértice de origem | Distância até 1 | Distância até 2 | Distância até 3 | Distância até 4 | Distância até 5 |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | 0 | 2 | 1 | 1 | 1 |
| 2 | 2 | 0 | 2 | 1 | 2 |
| 3 | 1 | 2 | 0 | 1 | 2 |
| 4 | 1 | 1 | 1 | 0 | 1 |
| 5 | 1 | 2 | 2 | 1 | 0 |

### Excentricidades

A excentricidade de um vértice corresponde à maior, entre as menores distâncias desse vértice até os demais vértices da componente.

#### Vértice 1

As distâncias de 1 até os demais vértices são:

```text
d(1,2) = 2
d(1,3) = 1
d(1,4) = 1
d(1,5) = 1
```

Assim:

```text
exc(1) = max{2,1,1,1} = 2
```

#### Vértice 2

As distâncias de 2 até os demais vértices são:

```text
d(2,1) = 2
d(2,3) = 2
d(2,4) = 1
d(2,5) = 2
```

Assim:

```text
exc(2) = max{2,2,1,2} = 2
```

#### Vértice 3

As distâncias de 3 até os demais vértices são:

```text
d(3,1) = 1
d(3,2) = 2
d(3,4) = 1
d(3,5) = 2
```

Assim:

```text
exc(3) = max{1,2,1,2} = 2
```

#### Vértice 4

As distâncias de 4 até os demais vértices são:

```text
d(4,1) = 1
d(4,2) = 1
d(4,3) = 1
d(4,5) = 1
```

Assim:

```text
exc(4) = max{1,1,1,1} = 1
```

#### Vértice 5

As distâncias de 5 até os demais vértices são:

```text
d(5,1) = 1
d(5,2) = 2
d(5,3) = 2
d(5,4) = 1
```

Assim:

```text
exc(5) = max{1,2,2,1} = 2
```

Portanto, as excentricidades dos vértices são:

```text
exc(1) = 2
exc(2) = 2
exc(3) = 2
exc(4) = 1
exc(5) = 2
```

### Raio da Componente

O raio corresponde à menor excentricidade entre os vértices da componente.

```text
raio(C1) = min{2,2,2,1,2}
raio(C1) = 1
```

### Diâmetro da Componente

O diâmetro corresponde à maior excentricidade entre os vértices da componente.

```text
diâmetro(C1) = max{2,2,2,1,2}
diâmetro(C1) = 2
```

### Vértices Centrais

Um vértice é considerado central quando sua excentricidade é igual ao raio da componente.

Como:

```text
raio(C1) = 1
```

e apenas o vértice 4 possui excentricidade igual a 1:

```text
exc(4) = 1
```

o vértice central da componente é:

```text
4
```

### Centro da Componente

O centro de uma componente é o conjunto formado por todos os seus vértices centrais.

Logo:

```text
centro(C1) = {4}
```

### Resumo da Análise

| Propriedade | Resultado |
|---|---|
| Componente conexa | `{1,2,3,4,5}` |
| `exc(1)` | 2 |
| `exc(2)` | 2 |
| `exc(3)` | 2 |
| `exc(4)` | 1 |
| `exc(5)` | 2 |
| Raio | 1 |
| Diâmetro | 2 |
| Vértice central | 4 |
| Centro | `{4}` |
