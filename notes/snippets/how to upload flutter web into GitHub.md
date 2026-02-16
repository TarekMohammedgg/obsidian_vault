
first , we need to create an responsive app using `LayoutBuilder` and if you want to add more interactive experience use `MouseRegion` to add action when hover on the card or container 

then we need to build the web version from our application ,we need to add follow the next steps 

1. first, delete this part from `web/index.html` direction 
	- `<base href="$FLUTTER_BASE_HREF">` and replace it with             `<base href="GITHUB_ADDRESS">` 
2. second, commit this command `flutter build web` 
3. third, we have two options 
	- use package `peanut` 
		- `dart pub global activate peanut`
		- `peanut`
		- `git push origin gh-pages` this will create new branch named `gh-pages` on GITHUB


we can make it easier using `github action` when push or pull to main branch update the web version 
```yaml 
name: Build and Deploy

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: write

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout 🛎️
        uses: actions/checkout@v4

      - name: Setup Flutter 🚀
        uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.32.4' # choose your flutter version
          channel: 'stable'

      - name: Install dependencies 📦
        run: flutter pub get

      - name: Build Web 🏗️
        run: flutter build web

      - name: Deploy to GitHub Pages 🚀
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./build/web
          publish_branch: gh-pages

```


![Image|655x355](https://drive.google.com/thumbnail?id=1Kq2pVTWTIVhz7VSAaCmvqkkk-heSeYdO&sz=w1000)


[](https://drive.google.com/file/d/1Kq2pVTWTIVhz7VSAaCmvqkkk-heSeYdO/view)
