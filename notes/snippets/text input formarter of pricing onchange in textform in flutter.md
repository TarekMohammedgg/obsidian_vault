
- the main goal of that 
  ```
  10000 => 10,000
  ```
  
```dart
import 'package:flutter/services.dart';
import 'package:intl/intl.dart';

class NumberTextInputFormatter extends TextInputFormatter {
  final NumberFormat _formatter =
      NumberFormat.decimalPattern('en_US');

  @override
  TextEditingValue formatEditUpdate(
    TextEditingValue oldValue,
    TextEditingValue newValue,
  ) {
    // remove commas
    final text = newValue.text.replaceAll(',', '');

    if (text.isEmpty) {
      return newValue.copyWith(text: '');
    }

    final number = int.parse(text);
    final newText = _formatter.format(number);

    return TextEditingValue(
      text: newText,
      selection: TextSelection.collapsed(
        offset: newText.length,
      ),
    );
  }
}

```

how to use it ? 
```dart 
 TextFormField(
                    inputFormatters: [
                      FilteringTextInputFormatter.digitsOnly,
                      NumberTextInputFormatter(),
                    ],
                    controller: priceController,
                    keyboardType: TextInputType.number,
                    decoration: const InputDecoration(
                      labelText: 'Price',
                      prefixIcon: Icon(Icons.attach_money),
                      border: OutlineInputBorder(),
                    ),
                    validator: (v) {
                      if (v == null || v.isEmpty) return 'Required';
                      final cleanValue = v.replaceAll(',', '');
                      if (double.tryParse(cleanValue) == null)
                        return 'Invalid number';
                      return null;
                    },
                  ),
```

