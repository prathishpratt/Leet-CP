def rverse(arr):
    l , h= 0, len(arr)-1

    while(h>l):
        arr[h], arr[l] = arr[l], arr[h]
        l +=1
        h -=1

    return arr

def rotateArray(arr: list, k: int) -> list:
    return rverse(rverse(arr[:k]) + rverse(arr[k:]))
