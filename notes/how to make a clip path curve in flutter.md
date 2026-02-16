---
tags:
  - Flutter/Helper
---
عشان اقدر اعمل ال clippath الي زي كده 

محتاج اعمل wrap widget لحاجة اسمها `clipPath` ، و ده بيديني تحكم اكتر لشكل ال curve الي عايز احطه علي ال widget . 
- code : 
	```dart 
	import 'package:flutter/material.dart';
	
	  
	
	class TCustomCurvedEdges extends CustomClipper<Path> {
	
	  @override
	
	  Path getClip(Size size) {
	
	    var path = Path();
	
	    path.lineTo(0, size.height);
	
	    final firstCurve = Offset(0, size.height - 20);
	
	    final lastCurve = Offset(30, size.height - 20);
	
	    path.quadraticBezierTo(
	
	      firstCurve.dx,
	
	      firstCurve.dy,
	
	      lastCurve.dx,
	
	      lastCurve.dy,
	
	    );
	
	  
	
	    final secondFirstCurve = Offset(0, size.height - 20);
	
	    final secondLastCurve = Offset(size.width - 30, size.height - 20);
	
	    path.quadraticBezierTo(
	
	      secondFirstCurve.dx,
	
	      secondFirstCurve.dy,
	
	      secondLastCurve.dx,
	
	      secondLastCurve.dy,
	
	    );
	
	  
	
	    final thirdFirstCurve = Offset(size.width, size.height - 20);
	
	    final thirdLastCurve = Offset(size.width, size.height);
	
	    path.quadraticBezierTo(
	
	      thirdFirstCurve.dx,
	
	      thirdFirstCurve.dy,
	
	      thirdLastCurve.dx,
	
	      thirdLastCurve.dy,
	
	    );
	
	  
	
	    path.lineTo(size.width, 0);
	
	    path.close();
	
	    return path;
	
	  }
	
	  
	
	  @override
	
	  bool shouldReclip(covariant CustomClipper<Path> oldClipper) {
	
	    return true;
	
	  }
	
	}
	
	
	```
و بتعمل class لواحده تعمله extend لل `customclipper` و بعدين تتحكم في شكل ال curve براحتك 

