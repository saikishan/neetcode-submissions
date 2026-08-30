class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) > n-1:
            return False

        parent = [-1] * n
        compoents = n
        def root(i):
            if parent[i] == -1:
                return i
            parent[i] = root(parent[i])
            return parent[i]

        for u, v in edges:
            parentU, parentV = root(u), root(v)
            if parentU == parentV:
                return False
            
            parent[parentU] = parentV
            compoents -= 1
        
        return compoents == 1
            
            
