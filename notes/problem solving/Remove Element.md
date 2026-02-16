---
date: 2026-01-23
tags:
  - "problem_solving"
---

source:: https://leetcode.com/problems/remove-element/

```dart 
class Solution {
int removeElement(List<int> nums, int val) {
  List<int> lists = [];
  for (int i = 0; i < nums.length; i++) {
    if (nums[i] != val) {
      lists.add(nums[i]);
    }
  }
  nums.clear();
  nums.addAll(lists);
  return nums.length;
}
}
```



the next solution  is wrong :: 
```dart 
for (int i = 0; i < nums.length; i++) {
  if (nums[i] == val) {
    nums.removeAt(i);
  }
}

```

because, when remove item in the same list that you loop it the items shifts , the i is move forward and the items shifts backward , so some values not scanned ... so this solution not work . 