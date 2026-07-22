class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [dict(),dict()]
        for u, v in redEdges:
            graph[0].setdefault(u,[]).append(v)
        for u, v in blueEdges:
            graph[1].setdefault(u,[]).append(v)
        ans = [-1]*n
        q = deque([(0, 0, 0),(0, 1, 0)])
        visit = set()

        while q:
            node,color,dist = q.popleft()
            if ans[node] == -1:
                ans[node] = dist
            for nxt in graph[1 - color].get(node,[]):
                if (nxt, 1 -color)not in visit:
                    visit.add((nxt, 1-color))
                    q.append((nxt, 1-color,dist+1))
        return ans
