---
date: 2026-01-25
tags:
  - "problem_solving"
---

source:: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/1895834368/

```dart 
class Solution {
int strStr(String haystack, String needle) {
  return haystack.indexOf(RegExp(needle));
}
}

```
