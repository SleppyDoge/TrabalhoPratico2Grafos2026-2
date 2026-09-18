# Marco 1

## Resumo do Problema

O problema se passa em uma cidade com n cruzamentos, que são ligados por m estradas de mão única. Como prefeito, é necessário garantir a segurança de todos os cruzamentos. Para isso, devem ser construídos postos policiais em alguns dos cruzamentos. Um posto em um cruzamento pode proteger outro caso seja possível ir de um ao outro e voltar, ou caso estejam no mesmo cruzamento.

Como os custos para construir os postos variam de acordo com o cruzamento, o objetivo é encontrar o menor custo possível para garantir a segurança de todos os cruzamentos e, entre as soluções de menor custo, determinar a quantidade de formas que utilizam o menor número possível de postos.

### Entrada

A primeira linha contém um inteiro, *n* *(1 ≤ n ≤ $10^5$)* - o número de cruzamentos da cidade.

A segunda linha contém *n* inteiros *a1, a2, ..., an*, onde `ai` representa o custo para construir um posto policial no cruzamento *i*. Os custos são não negativos e não excedem $10^9$.

A terceira linha contém um inteiro, *m* *(0 ≤ m ≤ 3 · $10^5$)* - o número de estradas de mão única da cidade.

As próximas *m* linhas contêm as estradas no formato `ui vi` *(1 ≤ ui, vi ≤ n, ui ≠ vi)*, onde `ui` e `vi` representam os cruzamentos conectados por uma estrada de mão única que vai de `ui` para `vi`. Não existem duas estradas entre os mesmos cruzamentos na mesma direção.

Caso-exemplo:

```text
3
1 2 3
3
1 2
2 3
3 2
```
Essa entrada significa que:

- Existem 3 cruzamentos na cidade.

- Os custos para construir os postos são:

    - 1º cruzamento: custo 1

    - 2º cruzamento: custo 2

    - 3º cruzamento: custo 3

- Existem 3 estradas de mão única.

- A cidade possui as seguintes conexões:

    - 1º → 2º cruzamento

    - 2º → 3º cruzamento

    - 3º → 2º cruzamento

### Saídas

A saída deverá conter **dois inteiros** separados por um espaço:

- O primeiro representa o **menor custo possível** para garantir a segurança de todos os cruzamentos.
- O segundo representa o **número de formas** de obter essa segurança com o custo mínimo, considerando o menor número possível de postos policiais e o cálculo do módulo **$10^9 + 7$**.

### Restrições

- Cada estrada conecta dois cruzamentos distintos e possui apenas uma direção.

- Um posto policial pode proteger um cruzamento se for possível ir até ele e retornar ao cruzamento do posto, ou se ambos forem o mesmo cruzamento.

- Como já foi dito no tópico de saídas, o número de formas de obter essa segurança só será aceito se considerar:
    - o custo mínimo estabelecido no primeiro inteiro da saída;
    - o menor número possível de postos policiais;
    - cálculo do módulo $10^9 + 7$.

## Modelagem do Grafo

### Vértices e Arestas

No problema, as junções representam os vértices do grafo. Cada vértice possui um custo associado à construção de um checkpoint policial.

As arestas representam vias de mão única entre as junções. Portanto, são arestas direcionadas que conectam dois vértices.

### Classificação do Grafo

- Como as vias possuem sentido único, o grafo é classificado como um **dígrafo** (grafo direcionado).
- O grafo é **não ponderado**, pois os custos estão associados aos vértices, e não às arestas.
- O grafo **não é necessariamente conexo**, pois podem existir grupos de vértices sem caminhos entre si.
- O grafo permite arestas em sentidos opostos entre dois vértices — por exemplo, u → v e v → u. Porém, não pode haver mais de uma aresta com a mesma direção entre o mesmo par de vértices.

## Resultado de Aprendizagem aferido

## DFS/BFS

Um ponto que consideraremos crucial para a solução desse problema é a identificação de ciclos dos vértices, pois isso indica que quaisquer junções nesse ciclo podem ser utilizadas como checkpoints. Entre ambos os métodos para pesquisa de grafos, consideramos que a capacidade do DFS de percorrer o máximo possível - possívelmente retornando para o vértice de partida - é a melhor abordagem para a solução do problema.

## Instância Pequena

```txt
3
1 2 3
3
1 2
2 3
3 2
```

**Representação da Instância**
````mermaid
flowchart LR
    A((1))
    B((2))
    C((3))

    A ---> B
    B ---> C
    C ---> B

    classDef normal fill:#2d68ad,stroke:#2d68ad,stroke-width:1px, 
    classDef police fill:#dd0c19,stroke:#dd0c19, stroke-width: 1px

    class A,B police
    class C normal
````

Os números presentes nos vértices indicam o custo associado a criação de um checkpoint na junção. Como não existe nenhum vértice que pode percorrer o vértice 1 de retornar, obrigatoriamente deve existir um checkpoint nele.

As junções 2 e 3 formam um ciclo e, sendo assim, um checkpoint em qualquer um deles consegue simultaneamente proteger o vértice e o membro do ciclo. Como desejamos custo mínimo, escolhe-se estabelecer um checkpoint no vértice 2.

Sendo assim, o custo mínimo é *1 + 2 = 3* e, como não é possível gerar nenhuma outra configuração que possua o mesmo custo, então há apenas 1 configuração possível. Logo:

> 3 1

