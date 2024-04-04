from typing import List


def selection_sort(arr: List[int]):
    n = len(arr)
    for i in range(0, n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]


# Driver Code
if __name__ == "__main__":

    ip = input()
    arr: List[int] = [
        int(i) for i in ip.split(",")
    ]  # cast to integer using list comperhensions
    print(arr)
    print(type(arr[0]))
    selection_sort(arr)
    print(arr)
