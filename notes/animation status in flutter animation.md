
- completed : 
	- لما الانيمشن يكون وصل لنقطة نهايته 
- dismissed : 
	- لما الانيمشن يكون لسه في نقطة بدايته 
- forward : 
	- لما الانميشن يكون واقف في نقطة ما بين ال begin و ال end و يكون اتجاه حركته من البداية الي النهاية 
- reverse : 
	- لما الانيمشن يكون واقف في نقطة ما بين النهاية و البداية و يكون اتجاه حركته من النهاية الي البداية 

- can access the animation status from two options : 
1. animation controller `animationController.statsu ; `
2. animation object `animation.status ; `

- how to start listen to the status when changing ? (how to listen to the animation status ? )
	- we can use a method callback named `addStatusListener`
		- `animationController.addStatusListener((status){}) ; ` 
