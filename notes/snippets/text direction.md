
- don't forget add the next import 
  `import 'dart:ui' as ui;`

```dart
  TextDirection getDirection(String text) {
    if (text.isEmpty) return TextDirection.ltr;

    final firstChar = text.characters.first;
    final isRtl = RegExp(r'^[\\u0600-\\u06FF]').hasMatch(firstChar);
    return isRtl ? TextDirection.rtl : TextDirection.ltr;
  }
```


- Example 
```dart 
 TextField(
                  onChanged: (val) {
                    setState(() {
                      inputDirection = getDirection(val);
                    });
                  },
                  textAlign: inputDirection == ui.TextDirection.rtl
                      ? TextAlign.right
                      : TextAlign.left,
                  textDirection: inputDirection,
                  controller: _customInputController,
                  
                  ) 
```

