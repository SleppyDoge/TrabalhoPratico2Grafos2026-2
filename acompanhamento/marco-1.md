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

### Vértices

### Arestas

### Classificação do Grafo

## DFS/BFS

## Instância Pequena

