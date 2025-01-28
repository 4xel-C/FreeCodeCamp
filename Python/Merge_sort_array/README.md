# Merge Sort Algorithm

## Overview
The `merge_sort` function implements the Merge Sort algorithm to sort an array in ascending order. Below is the step-by-step explanation of the algorithm using the example `array = [2, 1]`.

---

## Code Explanation

### 1. Base Case Check
- The function checks if the length of the array is less than or equal to 1.
- If true, the array is already sorted, and the function returns immediately.

### 2. Splitting the Array
- The array is divided into two halves:
  - `left_part = [2]`
  - `right_part = [1]`

### 3. Recursive Calls
- The function is called recursively on each half:
  - `merge_sort(left_part)` → Returns immediately as `left_part` contains a single element.
  - `merge_sort(right_part)` → Returns immediately as `right_part` contains a single element.

### 4. Merging
- Indices are initialized:
  - `left_array_index = 0`
  - `right_array_index = 0`
  - `sorted_index = 0`

- **Comparison Loop**:
  - Compare the first elements of `left_part` and `right_part`.
  - Since `right_part[0] (1)` is less than `left_part[0] (2)`, assign `array[sorted_index] = right_part[0] (1)` and increment:
    - `right_array_index` → 1
    - `sorted_index` → 1

- **Copy Remaining Elements**:
  - Copy the remaining element in `left_part` to the array:
    - Assign `array[sorted_index] = 2` and increment:
      - `left_array_index` → 1
      - `sorted_index` → 2

### 5. Final Result
- After merging, the array is now sorted: `[1, 2]`.

