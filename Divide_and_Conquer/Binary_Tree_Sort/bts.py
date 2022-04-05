###### Binary Tree Sort Algorithm ###### #* Done
##### To run, call 'python3 bts.py' in terminal
##### If you want to use my numbers, call 'python3 bts.py < input_nums' in terminal
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
    
def binary_tree_sort():
    nums = []
    user_input = None
    root = None
    root_val = None

    count = 0
    while user_input != -1:
        user_input = int(input("Enter number, enter -1 to end: "))
        if count == 0:
            root_val = user_input  
        nums.append(user_input)
        count += 1
    nums.pop(-1) # pops last index, since its value is -1

    count = 0
    for i in nums:
        if count == 0:
            root = Node(root_val)
        else:
            root.insert(i)
        count += 1

    print("\n")
    print(f"Root = {root_val}")
    print(f"Numbers you entered {nums}")
    print(f"Inorder Traversal: ", end=" ")
    root.print_tree()
    print(f"\nHeight: {height(root)}")
    return False