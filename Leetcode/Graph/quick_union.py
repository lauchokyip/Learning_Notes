# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root_arr = [i for i in range (size)]

    def find(self, child):
        root = self.root_arr[child]
        while(child != root):
            new_child = root
            new_root = self.root_arr[new_child]
            
            child = new_child
            root = new_root
        return root
		
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root_arr[root_y] = root_x 
            

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
# 1-2-5-6-7 3-8-9-4
uf.union(2,4)
print(uf.connected(2,9)) # true
