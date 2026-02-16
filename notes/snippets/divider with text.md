

```dart
import 'package:stock_application/common.dart';

class DividerWithText extends StatelessWidget {
  const DividerWithText({super.key});

  @override
  Widget build(BuildContext context) {
    return const Row(
        children: <Widget>[
          Expanded(
              child: Divider()
          ),

          Text("  OR  "),

          Expanded(
              child: Divider()
          ),
        ]
    ) ;
  }
}

```