---
tags:
  - problem_solving
site: leetCode
source:
  - https://leetcode.com/problems/valid-parentheses/description/
level: Easy
---
```dart
class Solution {

  bool isValid(String s) {

    List<String> stack = [];

    // Map opening brackets to their corresponding closing brackets

    Map<String, String> mapping = {'(': ')', '{': '}', '[': ']'};

    for (int i = 0; i < s.length; i++) {

      String char = s[i];

      if (mapping.containsKey(char)) {

        stack.add(char);

      } else if (mapping.containsValue(char)) {

        if (stack.isEmpty) {

          return false;

        }

        String top = stack.removeLast();

        if (mapping[top] != char) {

          return false;

        }

      }

    }

    return stack.isEmpty;

  }

}
```