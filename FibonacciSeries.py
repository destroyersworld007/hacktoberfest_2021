#recrusive
def fibRecursive(n):
    if n == 1 or n == 2:
        return 1
    
    return fibRecursive(n-1) + fibRecursive(n-2)



#iterative
def fibIterative(n):
    current = 1
    prev  = 1

    if n == 1 or n == 2:
        return 1
    else:
        for _ in range (3, n+1):
            result = current + prev
            prev, current = current, result
        
        return result
