import time

def impl_binarySearch(low, high, mid, arr, elm):
    if (low > high):
        print("not in")
        return
    elif (arr[mid] == elm):
        print(mid)
        return
    elif (elm < arr[mid]):
        high = mid - 1
        mid = (low + high ) // 2
        impl_binarySearch(low, high, mid, arr, elm)
    elif (elm > arr[mid]):
        low = mid + 1
        mid = (low + high ) // 2
        impl_binarySearch(low, high, mid, arr, elm)


def rec_binarySearch(arr, elm):
    low = 0
    high = len(arr) - 1
    mid = (low + high ) // 2
    impl_binarySearch(low, high, mid, arr, elm)

def ite_binarySearch(arr, elm):
    low = 0
    high = len(arr) - 1
    mid = (low + high ) // 2
    while (low <= high):
        if (arr[mid] == elm):
            print(mid)
            return
        if (elm < arr[mid]):
            high = mid - 1
            mid = (low + high ) // 2
        elif (elm > arr[mid]):
            low = mid + 1
            mid = (low + high ) // 2
    else:
        print("not in")

def linear(arr, elm):
    for i in range(0, len(arr)):
        if arr[i] == elm:
            print(i)

arr = [i for i in range(0, 10000000)]
