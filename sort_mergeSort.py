from typing import List


def merge_sort(arr:List[int],low:int,high:int):
  if(low>=high):
    return
  mid = int((low + high) / 2)
  merge_sort(arr,low,mid)
  merge_sort(arr,mid+1,high)
  merge(arr,low,mid,high)
  
  




def merge(arr:List[int],low:int,mid:int,high:int):
  temp = []
  left = low
  right = mid+1
  
  while(left <= mid and right <= high):
    if(arr[left]<=arr[right]):
      temp.append(arr[left])
      left+=1
    else:
      temp.append(arr[right])
      right+=1
  while(left<=mid):
    temp.append(arr[left])
    left+=1
  while(right<=high):
    temp.append(arr[right])
    right+=1
    
  for i in range(low , high+1):
    arr[i] = temp[i-low]
    
    


# Driver Code
if __name__ == "__main__":

    ip = input()
    arr: List[int] = [
        int(i) for i in ip.split(",")
    ]  # cast to integer using list comperhensions
    print(arr)
    print(type(arr[0]))
    merge_sort(arr,low=2,high=len(arr)-1)
    print(arr)
