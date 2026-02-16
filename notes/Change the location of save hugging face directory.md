---
---
#helper #hugging_face

### Change the location of save hugging face directory? 
**default location:**
```cmd
C:\Users\USER\.cache\huggingface
```

**move that to where your want**

**take the path of the new location and open system environment and create new user variable name it for example :`HF_Home` and put the new location**

**to change that in Vscode do the next**
1. go preference > settings 
2. search for `terminal.integrated.env.windows` and open it 
3. put the this code : `"HF_HOME": "D:/huggingface_cache"` under the `"terminal.integrated.env.windows":` key 
4. restart vscode and run this code in vscode terminal `set HF_HOME=D:\huggingface_cache  

```python
## for Ensure that  hugginface location changed use this code:
from huggingface_hub import hf_hub_download import os print("HF Cache Directory:", os.getenv("HF_HOME"))
#------------------------------------------
## for Ensure the location that will be used for download new huggingface models use this code : 
import os

print("Hugging Face Cache Directory:", os.getenv("HF_HOME", "Not Set"))

```


