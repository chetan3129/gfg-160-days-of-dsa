# 🚀 Day 1: Second Largest Element

## 🧠 Problem Statement

You are given an array of positive integers `arr[]`. Your task is to return the **second largest distinct** element in the array.

- If such an element doesn't exist (i.e., all elements are equal), return `-1`.

> **Note:** The second largest must not be equal to the largest.

---

## 💡 Examples

### 🔸 Example 1
Input: arr = [12, 35, 1, 10, 34, 1]

Output: 34

✅ Explanation: Largest is `35`, second largest is `34`.

### 🔸 Example 2
Input: arr = [10, 5, 10]

Output: 5

✅ Explanation: Largest is `10`, second largest is `5`.

### 🔸 Example 3
Input: arr = [10, 10, 10]
Output: -1
✅ Explanation: All elements are the same, so no second largest.

---

## 🔍 Constraints

- `2 ≤ arr.length ≤ 10⁵`
- `1 ≤ arr[i] ≤ 10⁵` (for all `0 ≤ i < arr.length`)

---

## 📈 Time & Space Complexity

| Approach              | Description                            | Time Complexity | Space Complexity |
|-----------------------|----------------------------------------|------------------|------------------|
| Brute-force (Sorting) | Sort array and find second largest     | O(n log n)       | O(1) or O(n)*     |
| Two-pass Linear       | First pass for max, second for 2nd max | O(n)             | O(1)             |
| One-pass Optimal      | Track both in a single pass            | O(n)             | O(1)             |

> *Depends on the sorting algorithm (e.g., Timsort uses O(n) extra space).

---

## 📁 Related Files

| Filename                     | Description                        |
|------------------------------|------------------------------------|
| `second_largest_sorting.py`  | Sorting-based approach             |
| `second_largest_two_pass.py` | Two-pass linear approach           |
| `second_largest_one_pass.py` | One-pass optimal solution          |

---

Happy Coding! ✨
