import random

def bubble_sort(arr:list) -> list:
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
                
                
nums = random.sample(range(0, 999999999), 1000) # selecting 500 random nums in specifed range
# print(f"Original list: {nums}")

nums = bubble_sort(nums)
# print(f"Sorted list via bubble sort: {nums}")

if bubble_sort(nums) == sorted(nums):
    print("Bubble Sort worked correctly")
else:
    print("Did not do it right")