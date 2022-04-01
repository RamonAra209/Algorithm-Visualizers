import bts_funcs as bts

###### Binary Tree Sort Algorithm ###### #* Done
##### To run, call 'python3 bts.py' in terminal
##### If you want to use my numbers, call 'python3 bts.py < input_nums' in terminal
if __name__ == "__main__":
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
            root = bts.Node(root_val)
        else:
            root.insert(i)
        count += 1

    print("\n")
    print(f"Root = {root_val}")
    print(f"Numbers you entered {nums}")
    root.print_tree()
    print(f"\nHeight: {bts.height(root)}")