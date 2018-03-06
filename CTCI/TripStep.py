def TripStep(n):
    
    arr = [0] * n
    return MemoTripStep(n, arr)
    
def MemoTripStep(n, arr):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        if arr[n-1] == 0:
            arr[n-1] = MemoTripStep(n-1, arr) + MemoTripStep(n-2, arr) + MemoTripStep(n-3, arr)
        
        return arr[n- 1] 

print(TripStep(3))
