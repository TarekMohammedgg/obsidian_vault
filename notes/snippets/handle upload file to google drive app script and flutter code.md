

# App Script Code 

> take care you must add the app script on the manager account 

```json 
function doPost(e) {
  try {
    // 1. استقبال الداتا من فلاتر
    var data = JSON.parse(e.postData.contents);
    
    var folderId = data.folderId; // آيدي الفولدر اللي عايز ترفع فيه
    var filename = data.filename;
    var base64Data = data.base64; // الصورة متشفرة Base64
    
    // 2. فك التشفير وتجهيز الملف
    var decodedData = Utilities.base64Decode(base64Data);
    var blob = Utilities.newBlob(decodedData, data.mimeType, filename);
    
    // 3. الوصول للفولدر والرفع
    var folder = DriveApp.getFolderById(folderId);
    var file = folder.createFile(blob);
    
    // 4. الرد على فلاتر بالنجاح والرابط
    return ContentService.createTextOutput(JSON.stringify({
      "status": "success",
      "fileUrl": file.getUrl(),
      "fileId": file.getId()
    })).setMimeType(ContentService.MimeType.JSON);
    
  } catch (error) {
    // التعامل مع الأخطاء
    return ContentService.createTextOutput(JSON.stringify({
      "status": "error",
      "message": error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}
```

----

# Handling in flutter 

packages: 
`mime: ^2.0.0`
`http: ^1.6.0`

> i faced the problem of redirect when the app script return redirect the http package follow this redirect automatically ,but can't handle this redirect , so the solution is make the follow redirect link off (false) and follow it manual this handled in the next code also and return the url link for the image . 



```dart 
import 'dart:convert';
import 'dart:developer';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:mime/mime.dart';
import 'package:path/path.dart' as p;

class DriveUploadService {
  final String _scriptUrl =
      'https://script.google.com/macros/s/AKfycbx1PjcLfG9Yv5W49So35hA1qY6q8lO2goSsaBXL5gz763NUdOY2yxc-h5FlNx-IDTnreg/exec';
  final String _managerFolderId = '1LiWgxJ81hlvZ68gVrqcSIvVgBpAjgku7';

  Future<void> uploadImage(File imageFile) async {
    try {
      log('Converting image to Base64...');
      final fileBytes = await imageFile.openRead(0, 1024).first;
      final mimeType = lookupMimeType(imageFile.path, headerBytes: fileBytes);
      List<int> imageBytes = await imageFile.readAsBytes();
      String base64Image = base64Encode(imageBytes);
      String fileName = p.basename(imageFile.path);

      Map<String, dynamic> body = {
        "folderId": _managerFolderId,
        "filename": fileName,
        "mimeType": mimeType ?? "image/jpeg",
        "base64": base64Image,
      };

      log('Uploading...');

      var request = http.Request('POST', Uri.parse(_scriptUrl));
      request.body = jsonEncode(body);
      request.headers.addAll({"Content-Type": "application/json"});

      request.followRedirects = false;

      final streamedResponse = await request.send();

      var response = await http.Response.fromStream(streamedResponse);

      if (response.statusCode == 302 || response.statusCode == 301) {
        final String? redirectUrl = response.headers['location'];

        if (redirectUrl != null) {
          final jsonResponseRaw = await http.get(Uri.parse(redirectUrl));

          var jsonResponse = jsonDecode(jsonResponseRaw.body);

          if (jsonResponse['status'] == 'success') {
            log('✅ Upload Done Successfully!');
            log('File URL: ${jsonResponse['fileUrl']}');
          } else {
            log('❌ Script Error: ${jsonResponse['message']}');
          }
        }
      } else if (response.statusCode == 200) {
        var jsonResponse = jsonDecode(response.body);
        if (jsonResponse['status'] == 'success') {
          log('✅ Upload Done (Direct)!');
        }
      } else {
        log('❌ HTTP Error: ${response.statusCode}');
        log('Body: ${response.body}');
      }
    } catch (e) {
      log('❌ Exception: $e');
    }
  }
}

```

