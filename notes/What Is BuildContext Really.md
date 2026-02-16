link:https://www.youtube.com/watch?v=5Eb5n1AncO0&list=PLma9WZYj7JS_zX7smAo4xEcQ6dSzJk28L&index=2

#flutter #flutter_architecture  

related: [[how flutter framework build]] ,  [[Flutter Framework Architecture]]

-----
- what is `BuildContext`  ? 
	- ما هو الا تصغير لل Element object ، لانه و بكل بساطه بيشاور علي ال Element object الي مربوط بيه و كمان ال `BuildContext` هو interface لل `Element`
	- بنادي عليه برده لانه بيعبر عن المكان الي احنا موجودين فيه في ال Widget tree 

- mounted in BuildContext ? 
	- و دي عن هل ال element object ارتبط بال widget ولا لسه ؟ 

- `findAncestors...` ? 
	- هو ده الي  بيدور عن ال parent بتاعك في ال widget 