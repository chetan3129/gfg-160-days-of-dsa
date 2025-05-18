# Approach 2: Two-Pass Linear Search
class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        if n<2:
            return -1
        largest = secondlargest = float('-inf')
        for i in range(n):
            if arr[i] > largest:
                secondlargest = largest
                largest = arr[i]
            elif arr[i] < largest and arr[i] > secondlargest:
                secondlargest = arr[i]
        if secondlargest == float('-inf'):
            return -1
        else:
            return secondlargest        
# Example:
print(getSecondLargest([10, 5, 10]))  # 5
