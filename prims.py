import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))  # Undirected graph

    def prim_mst(self):
        pq = [(0, 0)]  # Priority queue to store vertices with their minimum edge weights
        key = [float('inf')] * self.V  # Key values used to pick minimum weight edge
        parent = [(-1, -1)] * self.V  # Store MST edges
        in_mst = [False] * self.V  # Track if vertex is included in MST

        # Start with vertex 0
        key[0] = 0

        while pq:
            weight, u = heapq.heappop(pq)

            # Include vertex u in MST
            in_mst[u] = True

            # Iterate through all adjacent vertices of u
            for v, w in self.adj[u]:
                # If v is not yet in MST and the weight of (u, v) is smaller than current key of v
                if not in_mst[v] and w < key[v]:
                    key[v] = w
                    parent[v] = (u, w)
                    heapq.heappush(pq, (key[v], v))

        # Construct MST edges from parent array
        result = [parent[i] for i in range(1, self.V)]
        return result

if __name__ == "__main__":
    V = 5  # Number of vertices
    g = Graph(V)

    # Add edges and their weights
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    mst = g.prim_mst()

    print("Edges in the Minimum Spanning Tree (MST):")
    for edge in mst:
        print(edge[0], "-", edge[1])
