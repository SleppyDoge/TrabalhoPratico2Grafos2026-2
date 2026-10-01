## Marco 3

## Propriedade e critério de reconhecimento

- **Propriedade**: Componentes fortemente conexas (CFCs)

- **Critério**: Um novo componente é identificado ao encontrar um vértice ainda não visitado; a DFS percorre todos os vértices alcançáveis e os associa ao mesmo componente.

Em cada componente identificado, é determinado o menor custo. Após isso, soma-se esses valores e multiplica pela quantidade de vértices que tem esse mínimo de gasto.

## Referências de algs4 e adaptações previstas

## Referências de algs4 e adaptações previstas

Para a estratégia do problema, serão utilizadas como referência algumas implementações disponíveis no `algs4-py`.

### `digraph.py`

A classe `Digraph` será utilizada como referência para representar o grafo direcionado do problema. Cada vértice representa um cruzamento da cidade e cada aresta representa uma rua de mão única.

A implementação já possui estruturas importantes para a estratégia, como a lista de adjacência, o método `add_edge(v, w)` para inserir arestas direcionadas e o método `reverse()`, responsável por gerar o grafo com todas as arestas invertidas.

A estrutura básica poderá ser reutilizada, sendo necessária principalmente a adaptação da leitura da entrada do problema, já que o formato utilizado pelo Codeforces é diferente do formato de entrada usado diretamente pelas implementações de referência.

### `depth_first_order.py`

A classe `DepthFirstOrder` será utilizada como referência para realizar buscas em profundidade e registrar a ordem de processamento dos vértices.

Para a estratégia escolhida, interessa principalmente a pós-ordem reversa obtida pelo método `reverse_post()`. Essa ordem é utilizada posteriormente pelo algoritmo de identificação das componentes fortemente conexas.

Não são previstas mudanças significativas no funcionamento da DFS. A implementação será usada principalmente como apoio para determinar a ordem em que os vértices deverão ser processados.

### `kosaraju_scc.py`

A classe `KosarajuSCC` será a principal referência algorítmica. Ela utiliza o algoritmo de Kosaraju para identificar as componentes fortemente conexas de um grafo direcionado.

A implementação mantém:

- `marked`, para registrar os vértices já visitados;
- `id`, para indicar a qual componente cada vértice pertence;
- `count`, para registrar a quantidade de componentes encontradas.

A identificação das componentes será mantida como base da solução. A principal adaptação será acrescentar o processamento dos custos dos vértices exigido pelo problema.

Depois que cada vértice possuir o identificador de sua componente, será necessário:

1. identificar o menor custo entre os vértices de cada componente;
2. contar quantos vértices daquela componente possuem esse menor custo;
3. somar os menores custos encontrados em todas as componentes;
4. multiplicar as quantidades de escolhas possíveis em cada componente;
5. aplicar o módulo `10^9 + 7` à quantidade final de maneiras.

Assim, o algoritmo de Kosaraju será responsável pela parte estrutural da solução, enquanto a adaptação acrescentará o tratamento dos custos necessário para produzir as duas informações exigidas na saída do problema.

## Rastreamento manual em uma instância pequena

.
.
.
.
.
.

## Estimativa de complexidade

Sejam `V` o número de vértices e `E` o número de arestas.

- **Tempo: `O(??)`.** ........

- **Memória total: `O(??)`.** ........

Esta é uma análise da estratégia. A adaptação efetiva das referências e a validação por execução serão registradas no marco 4.