import random

def selection_sort(arr:list) -> list:
    n = len(arr)
    for i in range(0, n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

nums = random.sample(range(0, 999999999), 1000) # selecting 500 random nums in specifed range
nums = selection_sort(nums)

if nums == sorted(nums):
    print("Did selection sort correctly")
else:
    print("Did not do it right")