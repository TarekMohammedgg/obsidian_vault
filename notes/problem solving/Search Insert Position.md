---
date: 2026-01-25
tags:
  - "problem_solving"
---

source:: https://leetcode.com/problems/search-insert-position/

```dart

class Solution {

int searchInsert(List<int> nums, int target) {
  int right = nums.length - 1;
  int left = 0;
  while (left <= right) {
    int mid = (left + right) >> 1;
    if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return left;
}
}
```


- using binary search technique 
- `>>` is the same in `//` , mean division `/`
- 