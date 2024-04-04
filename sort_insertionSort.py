from typing import List


def insertion_sort(arr):
    n = len(arr)
    for i in range(0, n):
        j = i
        while j > 0 and (arr[j] < arr[j - 1]):
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1


# Driver Code
if __name__ == "__main__":

    ip = input()
    arr: List[int] = [
        int(i) for i in ip.split(",")
    ]  # cast to integer using list comperhensions
    print(arr)
    print(type(arr[0]))
    insertion_sort(arr)
    print(arr)
