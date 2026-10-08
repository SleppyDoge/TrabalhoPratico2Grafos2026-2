# Marco 4 — Implementação final e conclusão

## Solução final

A solução final foi consolidada em Python para o problema **Codeforces 427C — Checkposts**.

A estratégia utiliza o algoritmo de **Kosaraju** para identificar as componentes fortemente conexas (SCCs) do dígrafo. Depois que cada vértice recebe o identificador de sua componente, os custos são processados para determinar, em cada SCC:

- o menor custo entre seus vértices;
- a quantidade de vértices que possuem esse menor custo.

A resposta final é obtida pela soma dos menores custos de todas as SCCs e pela multiplicação das quantidades de escolhas de custo mínimo de cada componente, aplicando o módulo `10^9 + 7`.

A complexidade assintótica da estratégia permanece `O(V + E)`.

---

## Classes e módulos reutilizados e modificados

A implementação final foi baseada nas referências disponibilizadas em `algs4-py`. As principais classes adaptadas foram `Digraph`, `DepthFirstOrder` e `KosarajuSCC`.

### `Digraph`

A classe `Digraph` foi reutilizada como base para representar o grafo direcionado do problema.

Foram preservadas as responsabilidades principais:

- armazenar a quantidade de vértices e arestas;
- manter a lista de adjacência;
- inserir arestas direcionadas;
- construir o grafo reverso necessário ao algoritmo de Kosaraju.

#### Modificações realizadas

Na implementação de referência, a lista de adjacência utilizava `Bag`, que por sua vez dependia de estruturas como `Node` e `LinkIterator`.

Na solução final, essas estruturas foram removidas e substituídas por listas nativas do Python:

```python
self.adj = [[] for _ in range(self.V)]
```

A inserção de uma aresta passou a ser realizada diretamente com:

```python
self.adj[v].append(w)
```

A mudança reduz a quantidade de objetos intermediários utilizados na representação do grafo e torna o acesso aos vizinhos mais direto.

Métodos que não eram necessários para a solução final também foram removidos, mantendo apenas as operações efetivamente utilizadas pelo problema.

---

### `DepthFirstOrder`

A classe `DepthFirstOrder` foi reutilizada como referência para realizar a busca em profundidade responsável por produzir a ordem utilizada pelo algoritmo de Kosaraju.

Foram mantidas as estruturas:

- `marked`, para registrar os vértices visitados;
- `pre`, para registrar a pré-ordem;
- `post`, para registrar a pós-ordem;
- `reverse_post()`, para fornecer a pós-ordem reversa.

#### Modificações realizadas

A implementação original utilizava DFS recursiva.

Na versão final, a DFS foi transformada em **iterativa**, utilizando uma pilha explícita. Cada elemento da pilha registra:

```text
(vértice, próximo vizinho a ser analisado)
```

Essa estrutura permite preservar corretamente a ordem de finalização dos vértices sem depender da pilha de chamadas recursivas do Python.

A alteração foi necessária principalmente para reduzir o risco de erros em grafos grandes e diminuir o custo prático da implementação.

---

### `KosarajuSCC`

A classe `KosarajuSCC` foi reutilizada como principal referência para a identificação das componentes fortemente conexas.

Foram mantidas as estruturas:

- `marked`, para registrar os vértices já visitados;
- `id`, para armazenar a componente fortemente conexa de cada vértice;
- `count`, para controlar a quantidade de SCCs identificadas.

Também foi mantida a estratégia estrutural de Kosaraju:

1. construir o grafo reverso;
2. executar `DepthFirstOrder` no grafo reverso;
3. obter a pós-ordem reversa;
4. percorrer o grafo original nessa ordem;
5. iniciar uma nova DFS sempre que um vértice ainda não marcado for encontrado;
6. atribuir o mesmo `id` aos vértices identificados na mesma SCC.

#### Modificações realizadas

A DFS utilizada para identificar cada SCC também foi transformada de recursiva para **iterativa**, utilizando uma pilha explícita.

Durante a busca, todos os vértices alcançados recebem o identificador correspondente à componente atual:

```python
self.id[v] = self.count
```

A lógica do algoritmo foi preservada, mas a forma de execução da busca foi adaptada para lidar melhor com entradas grandes em Python.

---

## Adaptações específicas para o problema

Além das alterações nas classes de referência, foram realizadas adaptações específicas para produzir a resposta exigida pelo problema.

### Processamento direto dos custos por SCC

Na versão inicial, eram criadas estruturas intermediárias para armazenar:

- os vértices de cada componente (`components`);
- os custos dos vértices de cada componente (`costs`);
- os menores custos;
- as quantidades de repetições dos menores custos.

Na versão final, `components` e `costs` foram eliminados.

Após a identificação das SCCs, cada vértice é processado diretamente utilizando seu `id`:

```text
vértice -> id da SCC -> custo -> atualização do mínimo
```

Para cada componente são mantidas somente duas estruturas:

```python
min_cost
min_rep
```

onde:

- `min_cost[i]` representa o menor custo da SCC `i`;
- `min_rep[i]` representa quantos vértices daquela SCC possuem esse custo mínimo.

Isso reduz a quantidade de estruturas intermediárias e evita passagens desnecessárias pelos mesmos dados.

---

### Leitura da entrada

A entrada passou a ser lida por:

```python
sys.stdin.buffer.read()
```

Essa forma de leitura reduz o custo de entrada em casos grandes.

---

### Cálculo da quantidade de possibilidades

A multiplicação da quantidade de escolhas mínimas de cada SCC passou a aplicar o módulo durante o próprio cálculo:

```python
answer_possibilities = (
    answer_possibilities * repetitions
) % REM_VALUE
```

Assim, os valores intermediários permanecem limitados pelo módulo `10^9 + 7`.

---

## Complexidade da solução final

Sejam:

- `V` o número de vértices;
- `E` o número de arestas.

O algoritmo de Kosaraju percorre o grafo e o grafo reverso utilizando buscas em profundidade.

A complexidade de tempo permanece:

```text
O(V + E)
```

O processamento dos custos percorre os vértices uma única vez e acrescenta apenas `O(V)`, sem alterar a complexidade assintótica total.

A representação do grafo por listas de adjacência utiliza:

```text
O(V + E)
```

de memória.

As estruturas auxiliares, como `marked`, `id`, as pilhas das DFSs, a pós-ordem, `min_cost` e `min_rep`, utilizam memória proporcional ao número de vértices.

Portanto:

```text
Memória auxiliar: O(V)
Memória total: O(V + E)
```

---

## Validação da solução

A implementação final foi testada com os casos armazenados na pasta `dados/`, mantendo as saídas esperadas.

A solução também foi submetida ao **Codeforces 427C — Checkposts** e obteve:

```text
Verdict: Accepted
Tempo: 890 ms
Memória: 101000 KB
```

Antes das otimizações, a implementação apresentava problema de execução em um caso grande. Após as adaptações realizadas, a solução foi aceita pelo juiz oficial.

---

## Conclusão

A solução final preservou a estratégia baseada em componentes fortemente conexas e no algoritmo de Kosaraju, mas adaptou as implementações de referência para atender às necessidades práticas do problema em Python.

As principais modificações ocorreram na representação do grafo, nas buscas em profundidade e no processamento dos custos por componente.

Com essas adaptações, a solução manteve a complexidade `O(V + E)` e passou a executar dentro dos limites exigidos pelo problema.
