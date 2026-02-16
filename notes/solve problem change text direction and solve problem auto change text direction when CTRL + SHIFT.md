---
date: 2025-12-13
tags:
  - Window/Helper
---
# solve the problem using `autohotkey` app 
```bash 
#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%
*RAlt::
    SendInput {LAlt Down}{LShift Down}{LShift Up}{LAlt Up}
return
~LAlt Up:: return
```

هذا الكود يحل مشكلة ال `right alt + right shift` لا يعملان بشكل صحيح . 

# Solve the problem using `command` 
```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Keyboard Layout" /v "Scancode Map" /t REG_BINARY /d 000000000000000002000000380038E000000000 /f
```


