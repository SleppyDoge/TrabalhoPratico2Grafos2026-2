# Imports
import sys
from collections import deque


# Modified classes/functions
# Removed Node, LinkIterator and Bag
# Changes in Digraph, DepthFirstOrder, KosarajuSCC and main


# Digraph
class Digraph:

    def __init__(self, v=0):
        self.V = v
        self.E = 0
        self.adj = [[] for _ in range(self.V)]

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.E += 1

    def degree(self, v):
        return len(self.adj[v])

    def reverse(self):
        R = Digraph(self.V)

        for v in range(self.V):
            for w in self.adj[v]:
                R.add_edge(w, v)

        return R


# DepthFirstOrder
class DepthFirstOrder:

    def __init__(self, G):
        self.marked = [False for _ in range(G.V)]
        self.pre = deque()
        self.post = deque()

        for w in range(G.V):
            if not self.marked[w]:
                self.dfs(G, w)

    def dfs(self, G, start):
        stack = [(start, 0)]
        self.marked[start] = True
        self.pre.append(start)

        while stack:
            v, i = stack[-1]

            if i < len(G.adj[v]):
                w = G.adj[v][i]

                # Next time we return to v,
                # continue with the next neighbor
                stack[-1] = (v, i + 1)

                if not self.marked[w]:
                    self.marked[w] = True
                    self.pre.append(w)
                    stack.append((w, 0))

            else:
                # All neighbors of v have been processed
                self.post.append(v)
                stack.pop()

    def reverse_post(self):
        return reversed(self.post)

    def reversePost(self):
        return self.reverse_post()


# Kosaraju
class KosarajuSCC:

    def __init__(self, G):
        self.marked = [False for _ in range(G.V)]
        self.id = [0 for _ in range(G.V)]
        self.count = 0

        # First phase:
        # reverse graph + reverse postorder
        order = DepthFirstOrder(G.reverse())

        # Second phase:
        # DFS on original graph following that order
        for v in order.reverse_post():
            if not self.marked[v]:
                self.dfs(G, v)
                self.count += 1

    def dfs(self, G, start):
        stack = [start]
        self.marked[start] = True

        while stack:
            v = stack.pop()

            # All vertices reached in this DFS
            # belong to the same SCC
            self.id[v] = self.count

            for w in G.adj[v]:
                if not self.marked[w]:
                    self.marked[w] = True
                    stack.append(w)

    def strongly_connected(self, v, w):
        return self.id[v] == self.id[w]


# Data input
def data_input():
    return list(map(int, sys.stdin.buffer.read().split()))


def data_parsing(raw_data: list[int]) -> dict:
    n = raw_data[0]

    return {
        "vertices_size": n,
        "costs": raw_data[1:n + 1],
        "edge_size": raw_data[n + 1],
        "edges": list(
            zip(
                map(lambda x: x - 1, raw_data[n + 2::2]),
                map(lambda x: x - 1, raw_data[n + 3::2])
            )
        ),
    }


# Main
def main():
    REM_VALUE = (10 ** 9) + 7

    # Get data
    raw_data = data_input()
    parsed_data = data_parsing(raw_data)

    # Create original directed graph
    digraph = Digraph(parsed_data["vertices_size"])

    for u, v in parsed_data["edges"]:
        digraph.add_edge(u, v)

    # Identify strongly connected components
    scc = KosarajuSCC(digraph)

    # Number of SCCs
    m = scc.count

    # Minimum cost of each SCC
    min_cost = [float("inf")] * m

    # Number of vertices with minimum cost in each SCC
    min_rep = [0] * m

    # Process each vertex directly,
    # without creating components and costs lists
    for v in range(digraph.V):
        comp_id = scc.id[v]
        cost = parsed_data["costs"][v]

        if cost < min_cost[comp_id]:
            min_cost[comp_id] = cost
            min_rep[comp_id] = 1

        elif cost == min_cost[comp_id]:
            min_rep[comp_id] += 1

    # Sum minimum costs
    answer_min_cost = sum(min_cost)

    # Multiply possibilities while applying modulo
    answer_possibilities = 1

    for repetitions in min_rep:
        answer_possibilities = (
            answer_possibilities * repetitions
        ) % REM_VALUE

    # Output
    print(answer_min_cost, answer_possibilities)


# Run
if __name__ == "__main__":
    main()