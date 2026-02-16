---
date: 2025-12-01
tags:
  - AI/project
  - Main
Hub:
  - "[[Artificial intelligence]]"
status: complete
parent:
Area:
---
###  The available options : 
1. use `gemini-1.5-flash` and prompt on it 
2. user medical dataset pretrained model `microsoft/BioGPT-Large`

### Log of tries : 
```
1. using gemini-flash (api key ) => very good , but maybe pay for it . 
2. using microsoft/BioGPT-Large (hugging face pre-trianed) => not good in my case  . 
3. using google/pegasus-cnn_dailymail (hugging face )  => give me meaningful answers but not accurate and not suitable with my input dataset 
4. using omi-health/sum-small => finetuned model from hugging face 
```

---


---
### the common used models for text summarization (Encoder - Decoder model ) ? 
- Bert 
- T5 
- PEGASUS
----
Encoder only vs. Decoder only vs. Encoder-Decoder models ? 
**Encoder only:**
- for analyzing and understanding like (text classification -  question answering extractive)
- the common models like : (Bert - T5 - PEGASUS)
**Decoder only:**
- for predicting the next word (like chatbot and conversation Ai)
- the common model like : (GPT-4 , Llama)
**Encoder-Decoder:**
- good for tasks that need deep understanding like machine translating (English -> French) 


### Most Parameters used when creating Model : 

[Helper](https://chatgpt.com/share/67c22172-8aa8-800a-87f2-2f1e88694189)

### LLM Criteria ? 
[llm criteria](https://medium.com/@anmoltalwar/llm-selection-criteria-727f8c13c3ad)


---
- model pegasus => not good for Arabic and length of token is small . 
- Llama model => not good for arabic conversation , try another version from Llama 

----
### Translating 
```python
translator = pipeline("translation_ar_to_en", model="facebook/m2m100_418M", device=0 if torch.cuda.is_available() else -1)

def translate_text(text):

    """ ترجمة النص إلى الإنجليزية """

    return translator(text)[0]['translation_text']
```

---
