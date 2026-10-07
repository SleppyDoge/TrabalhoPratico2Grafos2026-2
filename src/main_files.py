# Imports
import sys
import math
from collections import deque


# Modified classes/functions

# Node & LinkIterator
class Node:

    def __init__(self, item, next_node):
        self.item = item
        self.next = next_node


class LinkIterator:

    def __init__(self, current):
        self.current = current

    def __next__(self):
        if self.current is None:
            raise StopIteration()
        else:
            item = self.current.item
            self.current = self.current.next
            return item

# Bag
class Bag:

    def __init__(self):
        self.first = None
        self.n = 0

    def __str__(self):
        return " ".join(str(i) for i in self)

    def __iter__(self):
        return LinkIterator(self.first)

    def size(self):
        return self.n

    def is_empty(self):
        return self.first is None

    def add(self, item):
        oldfirst = self.first
        self.first = Node(item, oldfirst)
        self.n += 1

# Digraph
class Digraph:

    def __init__(self, v=0, **kwargs):
        self.V = v
        self.E = 0
        self.adj = [Bag() for _ in range(self.V)]

        if 'file' in kwargs:
            # init a digraph by a file input
            in_file = kwargs['file']
            self.V = int(in_file.readline())
            self.adj = [Bag() for _ in range(self.V)]
            E = int(in_file.readline())
            for i in range(E):
                v, w = in_file.readline().split()
                self.add_edge(int(v), int(w))

    def __str__(self):
        s = "%d vertices, %d edges\n" % (self.V, self.E)
        s += "\n".join("%d: %s" % (v, " ".join(str(w)
                                               for w in self.adj[v])) for v in range(self.V))
        return s

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].add(w)
        self.E += 1

    def degree(self, v):
        return self.adj[v].size()

    def max_degree(self):
        max_deg = 0
        for v in range(self.V):
            max_deg = max(max_deg, self.degree(v))
        return max_deg

    def number_of_self_loops(self):
        count = 0
        for v in range(self.V):
            for w in self.adj[v]:
                if w == v:
                    count += 1
        return count

    def reverse(self):
        R = Digraph(self.V)
        v = 0
        while v < self.V:
            for w in self.adj[v]:
                R.add_edge(w, v)
            v += 1
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

    def dfs(self, G, v):
        self.pre.append(v)
        self.marked[v] = True

        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)
        self.post.append(v)

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

        order = DepthFirstOrder(G.reverse())
        for v in order.reverse_post():
            if not self.marked[v]:
                self.dfs(G, v)
                self.count += 1

    def dfs(self, G, v):
        self.marked[v] = True
        self.id[v] = self.count
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)

    def strongly_connected(self, v, w):
        return self.id[v] == self.id[w]



# Data input - sys filepath safety
def get_filepath() -> str:
    if len(sys.argv) != 2:
        raise FileNotFoundError(
            "The execution of the program requires input of the filepath with the input data"
        )
    return sys.argv[1]


# Data input - read
def data_input() -> list[int]:
    filepath = get_filepath()
    raw_data = None
    with open(filepath, "r") as arquivo:
        raw_data = list(map(lambda x: int(x), arquivo.read().split()))
    return raw_data


def data_parsing(raw_data: list[int]) -> dict:
    return {
        "vertices_size": raw_data[0],
        "costs": raw_data[1 : raw_data[0] + 1],
        "edge_size": raw_data[raw_data[0] + 1],
        "edges": list(
            zip(
                list(map(lambda x: x-1, raw_data[raw_data[0] + 2 :: 2])),
                list(map(lambda x: x-1, raw_data[raw_data[0] + 2 + 1:: 2]))
                )
        ),
    }


# Processing
# Main
def main():
    # Setting the rem constant
    REM_VALUE = (10 ** 9) + 7
    
    # Get data
    raw_data = data_input()
    parsed_data = data_parsing(raw_data)

    # Create Graph
    digraph = Digraph(parsed_data["vertices_size"])
    for u, v in parsed_data["edges"]:
        digraph.add_edge(v, u)
    
    #Kosaraju
    scc = KosarajuSCC(digraph)
    
    #Get components
    m = scc.count
    print(m, "strong components")
    components = []
    for i in range(m):
        components.append([])
    for v in range(digraph.V):
        components[scc.id[v]].append(v)

    # Debug for Vitor and Renato
    # print(components)
    
    # Get mapped costs:
    costs = []
    i = 0
    for comp in components:
        costs.append([])
        for v in comp:
            costs[i].append(parsed_data["costs"][v])
        i += 1
  
    # Debug for Vitor and Renato
    # print(costs)
    # print(parsed_data["costs"])
    
    # Get min costs and repetitions
    min_cost = []
    min_rep = []
    i = 0
    for comp in costs:
        min_cost.append(min(comp))
        rep = 0
        for cost in comp:
            if cost == min_cost[i]: rep += 1
        min_rep.append(rep)
        i += 1
    
    # Debug for Vitor and Renato
    # print(min_cost)
    # print(min_rep)
        
    # Make the answer
    answer_min_cost = sum(min_cost)
    answer_possibilities = math.prod(min_rep) % REM_VALUE

    # Output result
    print(answer_min_cost, answer_possibilities, sep=" ")

# Run
if __name__ == "__main__":
    main()
