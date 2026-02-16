#flutter #flutter_utils
YouTube::https://www.youtube.com/watch?si=gd8UgiWSuS_hFwuy&v=6Hpfl68ug2M&feature=youtu.be

---

Package::https://pub.dev/packages/skeletonizer

----
### Example:: 
```dart 
Skeletonizer(
  enabled: _loading,
  child: ListView.builder(
    itemCount: 7,
    itemBuilder: (context, index) {
      return Card(
        child: ListTile(
          title: Text('Item number $index as title'),
          subtitle: const Text('Subtitle here'),
          trailing: const Icon(Icons.ac_unit),
        ),
      );
    },
  ),
)
```
