---
date: 2026-01-28
tags:
  - "problem_solving"
---

source:: https://leetcode.com/problems/merge-sorted-array/

```dart 
class Solution {

void merge(List<int> nums1, int m, List<int> nums2, int n) {
  List<int> res = [];
  for (int i = 0; i < m; i++) {
    res.add(nums1[i]);
  }
  for (int i = 0; i < n; i++) {
    res.add(nums2[i]);
  }

  res.sort();
  nums1.clear(); 
  nums1.addAll(res);
  
}
}
```