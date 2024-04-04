from typing import List


def quick_sort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        partition_index = partition(arr, low, high)
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)


def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j


# Driver Code
if __name__ == "__main__":
    ip = input()
    arr: List[int] = [int(i) for i in ip.split(",")]
    print(arr)
    print(type(arr[0]))
    quick_sort(arr, low=0, high=len(arr) - 1)
    print(arr)
