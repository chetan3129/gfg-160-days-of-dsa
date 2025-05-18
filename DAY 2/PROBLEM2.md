
# Move All Zeros to End of Array

#PROBLEM

You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

---

## 📘 Contents

- [Naive Approach (Using Temporary Array)](#1-naive-approach-using-temporary-array)
- [Better Approach (Two Traversals)](#2-better-approach-two-traversals)
- [Expected Approach (One Traversal)](#3-expected-approach-one-traversal)

---

## 1. Naive Approach (Using Temporary Array)

### 🔗 Code
```python
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
```

### 🔄 Loop Execution

**Input:** `[1, 2, 0, 4, 3, 0, 5, 0]`

**First loop (copy non-zero elements):**

| i | arr[i] | Action         | temp[]                        | j |
|---|--------|----------------|-------------------------------|---|
| 0 | 1      | temp[0] = 1    | [1, 0, 0, 0, 0, 0, 0, 0]       | 1 |
| 1 | 2      | temp[1] = 2    | [1, 2, 0, 0, 0, 0, 0, 0]       | 2 |
| 2 | 0      | skip           |                               | 2 |
| 3 | 4      | temp[2] = 4    | [1, 2, 4, 0, 0, 0, 0, 0]       | 3 |
| 4 | 3      | temp[3] = 3    | [1, 2, 4, 3, 0, 0, 0, 0]       | 4 |
| 5 | 0      | skip           |                               | 4 |
| 6 | 5      | temp[4] = 5    | [1, 2, 4, 3, 5, 0, 0, 0]       | 5 |
| 7 | 0      | skip           |                               | 5 |

**Second loop (copy temp back to arr):**

Final `arr[]`: `[1, 2, 4, 3, 5, 0, 0, 0]`

---

## 2. Better Approach (Two Traversals)

### 🔗 Code
```python
def pushZerosToEnd(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < len(arr):
        arr[count] = 0
        count += 1
```

### 🔄 Loop Execution

**Input:** `[1, 2, 0, 4, 3, 0, 5, 0]`

**First loop (shift non-zeros):**

| i | arr[i] | Action         | arr[] after step           | count |
|---|--------|----------------|-----------------------------|--------|
| 0 | 1      | arr[0] = 1     | [1, 2, 0, 4, 3, 0, 5, 0]    | 1      |
| 1 | 2      | arr[1] = 2     | [1, 2, 0, 4, 3, 0, 5, 0]    | 2      |
| 2 | 0      | skip           |                             | 2      |
| 3 | 4      | arr[2] = 4     | [1, 2, 4, 4, 3, 0, 5, 0]    | 3      |
| 4 | 3      | arr[3] = 3     | [1, 2, 4, 3, 3, 0, 5, 0]    | 4      |
| 5 | 0      | skip           |                             | 4      |
| 6 | 5      | arr[4] = 5     | [1, 2, 4, 3, 5, 0, 5, 0]    | 5      |
| 7 | 0      | skip           |                             | 5      |

**Second loop (fill 0s):**

| count | Action         | arr[]                        |
|--------|----------------|-------------------------------|
| 5      | arr[5] = 0     | [1, 2, 4, 3, 5, 0, 5, 0]     |
| 6      | arr[6] = 0     | [1, 2, 4, 3, 5, 0, 0, 0]     |
| 7      | arr[7] = 0     | [1, 2, 4, 3, 5, 0, 0, 0]     |

Final `arr[]`: `[1, 2, 4, 3, 5, 0, 0, 0]`

---

## 3. Expected Approach (One Traversal)

### 🔗 Code
```python
def pushZerosToEnd(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1
```

### 🔄 Loop Execution

**Input:** `[1, 2, 0, 4, 3, 0, 5, 0]`

| i | arr[i] | Action                    | arr[] after step         | count |
|---|--------|---------------------------|----------------------------|--------|
| 0 | 1      | swap arr[0] ↔ arr[0]      | [1, 2, 0, 4, 3, 0, 5, 0]  | 1      |
| 1 | 2      | swap arr[1] ↔ arr[1]      | [1, 2, 0, 4, 3, 0, 5, 0]  | 2      |
| 2 | 0      | skip                      |                            | 2      |
| 3 | 4      | swap arr[3] ↔ arr[2]      | [1, 2, 4, 0, 3, 0, 5, 0]  | 3      |
| 4 | 3      | swap arr[4] ↔ arr[3]      | [1, 2, 4, 3, 0, 0, 5, 0]  | 4      |
| 5 | 0      | skip                      |                            | 4      |
| 6 | 5      | swap arr[6] ↔ arr[4]      | [1, 2, 4, 3, 5, 0, 0, 0]  | 5      |
| 7 | 0      | skip                      |                            | 5      |

Final `arr[]`: `[1, 2, 4, 3, 5, 0, 0, 0]`

---

## ✅ Conclusion

All three approaches produce the same result, but the one traversal method is the most efficient with:
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
