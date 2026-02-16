---
date: 2025-12-01
tags:
  - AI/project
  - Main
status: complete
parent:
Area:
---
## Goal of the chatbot 
\- the goal of the chatbot answer on the questions that related to bank field (FAQ) response  chatbot . 
Steps : 
### 1.Data collection 
amazon FAQs data (json) 

---

### 2.pre-trained Model and Tokenizer 
choose the suitable model => Qwin2-1.5b parameters finetuned 
choose the suitable tokenizer and adjust   your data to tokenizer 

---
### 3.Prompt engineering 
choose  the suitable prompt for our model  
for data and fine tuned 
[[prompt engineering using langchain]]

---
### 4.train pre-trained model to your data (fine tune) 
we must train the next : 
\- argument 
\- train dataset (adjust dataset , to make the model can understand the data by tokenization)

PEFT 
	lora 
	qlora


---


links :
https://medium.com/@mohitdulani/fine-tune-any-llm-using-your-custom-dataset-f5e712eb6836


