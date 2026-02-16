
```dart
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

class SqlDb {
  static Database? _db;
  Future<Database?> get db async {
    if (_db == null) {
      _db = await initialDb();
      return _db;
    } else {
      return _db;
    }
  }

  // CREATE DATABASE
  initialDb() async {
    String databasePath = await getDatabasesPath();
    String path = join(databasePath, 'my_database.db');

    Database mydb = await openDatabase(
      path,
      onCreate: _onCreate,
      version: 2,
      onUpgrade: _onUpgrade,
    );
    return mydb;
  }

  // Upgrad  Database
  _onUpgrade(Database db, int oldVersion, int newVersion) {
    print("Upgrad Database =========================== ");
  }

  // CREATE TABLE
  _onCreate(Database db, int version) async {
    await db.execute('''
      CREATE TABLE "notes"(
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "note" TEXT NOT NULL
      )
    ''');
    print(
      "Create Database and Table successfully =========================== ",
    );
  }

  //SELECT
  readData(String sql) async {
    Database? mydb = await db;
    List<Map> response = await mydb!.rawQuery(sql);
    return response;
  }

  //INSERT
  insertData(String sql) async {
    Database? mydb = await db;
    int response = await mydb!.rawInsert(sql);
    return response;
  }

  //UPDATE
  updateData(String sql) async {
    Database? mydb = await db;
    int response = await mydb!.rawUpdate(sql);
    return response;
  }

  //DELETE
  deleteData(String sql) async {
    Database? mydb = await db;
    int response = await mydb!.rawDelete(sql);
    return response;
  }
}

```