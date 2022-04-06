import math

test_arr = [3, 2, 4, 1, 5, 6, 8, 7] # len = 6

def merge_sort(a:list):
    n = len(a)
    b = []
    c = []
    bound = math.floor(n / 2)
    if n > 1:
        b[0:bound] = a[0:bound]
        c[0:bound] = a[bound:n]
        merge_sort(b)
        merge_sort(c)
        merge(b, c, a) 
    return a
    
def merge(b:list, c:list, a:list):
    i, j, k = 0, 0, 0
    p = len(b)
    q = len(c)

    while i < p and j < q:
        if b[i] <= c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
        
        k += 1

    if i == p:
        a[k:(p+q)] = c[j:q]
    else:
        a[k:(p+q)] = b[i:p]
    
    return a

