```bash 
pip install pyinstaller

```

```bash 
pyinstaller snaptube_alternate_GUI.py --onefile --icon=download.ico  --noconsole --add-binary "dist/ffmpeg.exe;." --add-binary "dist/ffprobe.exe;."

```
`--onfile:` all in one file 
`--noconsole:` not open terminal 
`myicon.icon` : your image `.ico` extension for your application 
[converIco](https://www.freeconvert.com/ico-converter/download)
