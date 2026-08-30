class UnionFind:
    def __init__(self,n):
        self.parent = [-1] * n
        self.components = n

    def __len__(self):
        return self.components

    def find(self, i):
        if self.parent[i] == -1:
        	return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, u, v):
    	u = self.find(u)
    	v = self.find(v)
    	if u != v:
    		self.parent[u] = v
    		self.components -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

    	uf = UnionFind(n)
    	for u, v in edges:
    		uf.union(u,v)

    	return len(uf)
        