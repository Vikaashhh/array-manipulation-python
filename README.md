# 🚀 Day-2 DSA Challenge – Push Zeros to End

This repository contains the solution to the classic **"Push Zeros to End"** problem. The goal is to rearrange the array so that all zero elements are moved to the end while maintaining the relative order of non-zero elements.

---

## 🧠 Problem Statement

Given an array of integers, move all the `0`s to the end while maintaining the relative order of the non-zero elements.

### ✅ Example:

**Input:**
[0, 1, 0, 3, 12]


**Output:**
[1, 3, 12, 0, 0]


---

## 🛠️ Solution Approach

- Traverse the array from left to right.
- Track the index where the next non-zero element should be placed.
- When a non-zero is encountered, swap it with the value at the `non_zero_index`.
- Increment the `non_zero_index` after every valid swap.

This algorithm runs in **O(n)** time and **O(1)** space.

---

## 🧾 Code Implementation

```python
class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        non_zero_index = 0  # Tracks the position to place the next non-zero element

        for i in range(n):
            if arr[i] != 0:
                # Swap the current non-zero element with the element at non_zero_index
                arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
                non_zero_index += 1  # Move the index forward for the next non-zero

```
🧪 Test Case (Runner Code)

```
if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    print("Original Array:", arr)

    obj = Solution()
    obj.pushZerosToEnd(arr)

    print("Modified Array:", arr)

```

📦 How to Run
Clone the repository:

git clone https://github.com/your-username/day2-push-zeros-end.git

cd day2-push-zeros-end


📌 Tags

#python #dsa #array #zero-manipulation #beginner-friendly #leetcode #100daysofcode

🙌 Author
Vikash Joshi

Frontend Developer | UI/UX Enthusiast | DSA Learner

LinkedIn:- https://www.linkedin.com/in/itaintvi/


⭐️ Show some love
If you find this helpful, feel free to ⭐️ the repo and share it with others in the community.
