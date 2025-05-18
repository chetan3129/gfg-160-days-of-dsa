def pushZerosToEnd(arr):
  n = len(arr)
  temp = [0] * n  
  j = 0
  for i in range(n):
    if arr[i] != 0:
      temp[j] = arr[i]
      j += 1
  for i in range(n):
    arr[i] = temp[i]
  return arr
if __name__ == "__main__":
  arr = [1, 2, 0, 4, 3, 0, 5, 0]
  print(move(arr)) # output [1, 2, 4, 3, 5, 0, 0, 0]
