from typing import List


def bubble_sort(arr: List[int]):
  n = len(arr)
  for i in range(n-1,-1,-1):
    for j in range(0,i):
      if arr[j] > arr[i]:
        arr[j],arr[i] = arr[i] ,arr[j]
      


# Driver Code
if __name__ == "__main__":

    ip = input()
    arr: List[int] = [
        int(i) for i in ip.split(",")
    ]  # cast to integer using list comperhensions
    print(arr)
    print(type(arr[0]))
    bubble_sort(arr)
    print(arr)
