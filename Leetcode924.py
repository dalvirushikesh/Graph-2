#Time - O(n^2)
#Space - O(n)
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        
        # Disjoint Set Union (Union-Find)
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
        
        # Step 1: Build connected components using union-find
        for i in range(n):
            for j in range(i + 1, n):
                if graph[i][j]:
                    union(i, j)

        # Step 2: Count size of each component
        size = [0] * n
        for i in range(n):
            root = find(i)
            size[root] += 1

        # Step 3: Count number of infected nodes in each component
        infected_count = [0] * n
        for node in initial:
            root = find(node)
            infected_count[root] += 1

        # Step 4: Choose node to remove
        result = float('inf')
        max_saved = -1
        
        for node in initial:
            root = find(node)
            if infected_count[root] == 1:
                if size[root] > max_saved or (size[root] == max_saved and node < result):
                    max_saved = size[root]
                    result = node
        
        # Step 5: If no node uniquely infects a component, return the smallest index
        if result == float('inf'):
            return min(initial)
        return result
