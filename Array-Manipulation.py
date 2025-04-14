class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        non_zero_index = 0  # Tracks the position to place the next non-zero element

        for i in range(n):
            if arr[i] != 0:
                # Swap the current non-zero element with the element at non_zero_index
                arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
                non_zero_index += 1  # Move the index forward for the next non-zero

# Test case to run the code
if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    print("Original Array:", arr)

    obj = Solution()
    obj.pushZerosToEnd(arr)

    print("Modified Array:", arr)  # Expected Output: [1, 3, 12, 0, 0]
