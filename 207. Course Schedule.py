class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {}
        for src, dst in prerequisites:
            if src not in premap:
                premap[src] = []
            if dst not in premap:
                premap[dst] = []
            premap[src].append(dst)
        
        visit = set()
        def dfs(node):
        
            if node in visit:
                return False
            if not len(premap[node]):
                return True
            visit.add(node)
            for n in premap[node]:
                if not dfs(n): return False
            visit.remove(node)
            premap[node]=[]
            return True
        for n in premap:
            if not dfs(n): return False
        return True