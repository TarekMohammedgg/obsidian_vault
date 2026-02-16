
```dart
import 'package:intl/intl.dart';

abstract class Functions {
  static String formatted({required String date}) {
final dateTime = DateTime.parse(date).toLocal();
final formattedDate = DateFormat('yyyy/MM/dd hh:mm a', 'en_EG').format(dateTime);

    return formattedDate;
  }
}
```