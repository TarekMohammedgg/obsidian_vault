---
date: 2026-01-26
tags:
  - "problem_solving"
---

source:: https://leetcode.com/problems/length-of-last-word/

```dart 
class Solution {
int lengthOfLastWord(String s) {
  List<String> words = s.split(" ");
  print(words);
  int length = words.length;
  while (words[length - 1] == "") {
    length--;
  }
  return words[length - 1].length;
}
}
```