from lib2to3.pytree import Node
import random 

class Node:
    def __init__(self, val) -> None:
        self.left = None
        self.right = None
        self.val = val
    
    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left == None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right == None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val, end=" ")
        if self.right:
            self.right.print_tree()
        
def verify_sort(nums:list, bts_res: list) -> bool:
    return sorted(nums) == bts_res

def height(root):
    if root == None:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))