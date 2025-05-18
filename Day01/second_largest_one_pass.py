# Approach 3: One-Pass Optimal (Expected)
def getSecondLargest(arr):
  largest = -1
  secondLargest = -1
  for num in arr:
    if num > largest:
      secondLargest = largest
      largest = num
    elif num != largest and num > secondLargest:
      secondLargest = num
  return secondLargest

# Example:
print(getSecondLargest([10, 10, 10]))  # -1
