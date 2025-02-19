class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, v):
        left = True if v < self.value else False
        if left:
            print(f"Inserting to the left because {v} < self value = {self.value}")
            if self.left != None:
                self.left.insert(v) 
            else:
                self.left = TreeNode(v)
        else:
            print(f"Inserting to the right because {v} >= self value = {self.value}")
            if self.right != None:
                self.right.insert(v) 
            else:
                self.right = TreeNode(v)
class Tree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)
    def insert(self, v):
        self.root.insert(v)
t = Tree(27)
l = [19, 36, 42, 16]
for i in l:
    t.insert(i)
