class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            stack = [node]
            visited[node] = True
            vertices = 0
            degree_sum = 0

            while stack:
                curr = stack.pop()
                vertices += 1
                degree_sum += len(graph[curr])

                for nei in graph[curr]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)

            return vertices, degree_sum

        for i in range(n):
            if not visited[i]:
                vertices, degree_sum = dfs(i)
                edges_count = degree_sum // 2

                if edges_count == vertices * (vertices - 1) // 2:
                    ans += 1

        return ans