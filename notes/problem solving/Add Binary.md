---
date: 2026-01-26
tags:
  - "problem_solving"
---

source:: https://leetcode.com/problems/add-binary/submissions/1897590251/

```dart 
class Solution {
String addBinary(String a, String b) {
  String ans = "";
  int i = a.length - 1; // point on the last digit
  int j = b.length - 1; // point on the last digit
  int carry = 0;
  while (i >= 0 || j >= 0 || carry == 1) {
    if (i >= 0) {
      int number = int.parse(a[i--]);
      carry += number - 0;
    }

    if (j >= 0) {
      int number = int.parse(b[j--]);
      carry += number - 0;
    }

    ans = (carry % 2).toString() + ans;
    carry ~/= 2;
  }
  return ans;
}
}
```