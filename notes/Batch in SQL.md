#software #database #SQL 
related:: [[Sqflite]] 

Batch : 
انك تنفذ اكتر من command في نفس الوقت   و بعدين بتعمل commit 

Example on Batch in Flutter  using [[Sqflite]]

```dart 
Batch batch = db.batch() ; 
batch.excute(''' ''' ) ; 
batch.excute(''' ''' ) ; 
await batch.commit() ; 
```
