---
date: 2026-01-28
tags:
  - problem_solving
---

source:: https://leetcode.com/problems/remove-duplicates-from-sorted-list/


```dart 


/**

 * Definition for singly-linked list.

 * class ListNode {

 *   int val;

 *   ListNode? next;

 *   ListNode([this.val = 0, this.next]);

 * }

 */

class Solution {

ListNode? deleteDuplicates(ListNode? head) {

  var res = head;

  while (head != null && head.next != null) {

    if (head.val == head.next!.val) {

      head.next = head.next!.next;

    } else {

      head = head.next;

    }

  }

  return res;

}

}

```

## the idea 
````
Input: head = 1 → 1 → 2 → 3 → 3
````
```
 1 → 1 → 2 → 2 → 3
 h
 r
```
```
 1 → 2 → 2 → 3
 h
 r
```
```
 1 → 2 → 2 → 3
 r   h
```
```
 1 → 2 → 3
 r   h
```
