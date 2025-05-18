# Approach 1: Sorting (Naive)
def getSecondLargest(arr):
  n = len(arr)
  arr.sort() # Sort the array in non-decreasing order
  for i in range(n - 2, -1, -1):
    if arr[i] != arr[n - 1]:
      return arr[i]
  return -1

# Example:
print(getSecondLargest([12, 35, 1, 10, 34, 1]))  # 34
