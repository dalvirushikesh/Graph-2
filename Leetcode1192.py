# Time Complexity: O(V + E), where V = number of nodes, E = number of edges
# Space Complexity: O(V + E), for graph, discovery, lowest arrays and result list

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.graph = [[] for _ in range(n)]
        self.discovery = [-1] * n
        self.lowest = [0] * n
        self.time = 0
        self.result = []

        # Build graph
        for u, v in connections:
            self.graph[u].append(v)
            self.graph[v].append(u)

        # Start DFS from node 0 (assuming graph is connected)
        self.dfs(0, -1)
        return self.result

    def dfs(self, node: int, parent: int):
        self.discovery[node] = self.lowest[node] = self.time
        self.time += 1

        for neighbor in self.graph[node]:
            if neighbor == parent:
                continue
            if self.discovery[neighbor] == -1:  # not visited
                self.dfs(neighbor, node)
                # Bridge condition
                if self.lowest[neighbor] > self.discovery[node]:
                    self.result.append([node, neighbor])
                self.lowest[node] = min(self.lowest[node], self.lowest[neighbor])
            else:
                self.lowest[node] = min(self.lowest[node], self.discovery[neighbor])
