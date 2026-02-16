---
date: 2026-01-23T16:50:43+02:00
tags:
  - problem_solving
---

source:: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1894423547/

```dart 

    class Solution {
  
int removeDuplicates(List<int> nums) {
  List<int> arrangedList = [];
  for (int i = 0; i < nums.length; i++) {
    int num = nums[i];
    if (!arrangedList.contains(num)) {
      arrangedList.add(num);
    }
  }
  nums.clear();
  nums.addAll(arrangedList);
  return nums.length;
}

    }
	
```