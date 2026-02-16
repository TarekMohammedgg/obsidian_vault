---
date: 2026-01-26
tags:
  - "problem_solving"
---

source:: https://leetcode.com/problems/plus-one/

```dart 

class Solution {
List<int> plusOne(List<int> digits) {
  for (int i = digits.length - 1; i >= 0; i--) {
    if (digits[i] < 9) {
      digits[i] += 1;
      return digits;
    }
    digits[i] = 0;
  }
  digits.insert(0, 1);
  return digits;
}
}
```