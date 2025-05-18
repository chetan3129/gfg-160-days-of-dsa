# Approach 2: Two-Pass Linear Search
def getSecondLargest(arr):
  n = len(arr)
  largest = -1
  secondLargest = -1
  for i in range(n):
    if num > largest:
      largest = num
  for i in range(n):
    if num > secondLargest and num != largest:
      secondLargest = num
  return secondLargest

# Example:
print(getSecondLargest([10, 5, 10]))  # 5
