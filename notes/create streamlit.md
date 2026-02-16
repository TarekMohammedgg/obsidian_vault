---
date: 2025-12-01
tags:
  -  
  - AI
---

## Diagnosis Extract Model 

```python
!pip install -q streamlit==1.45.1
```
### Initial Code :: 
```python
%%writefile app.py

import streamlit as st

from typing import List

from pydantic import BaseModel

import json

import re

import torch

  

from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

import bitsandbytes as bnb

import torch

  

def load_quantized_model(model_name: str,

                         load_in_4bit: bool = True,

                         use_double_quant: bool = True,

                         quant_type: str = "nf4",

                         compute_dtype=torch.float16,  # use float16 instead of bfloat16 for wider support

                         auth_token: bool = True):

    # Clear memory before loading

    import gc

    gc.collect()

    torch.cuda.empty_cache()

  

    bnb_config = BitsAndBytesConfig(

        load_in_4bit=load_in_4bit,

        bnb_4bit_use_double_quant=use_double_quant,

        bnb_4bit_quant_type=quant_type,

        bnb_4bit_compute_dtype=compute_dtype,

    )

  

    # 🧠 Remove device_map="auto" to avoid meta errors

    model = AutoModelForCausalLM.from_pretrained(

        model_name,

        quantization_config=bnb_config,

        torch_dtype=torch.float16,

        device_map={"": 0},  # send everything to cuda:0 directly

        trust_remote_code=True

    )

  

    tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=auth_token)

    tokenizer.pad_token = tokenizer.eos_token

  

    return model, tokenizer

  
  

# Replace with your model ID

base_model_id = "CohereForAI/c4ai-command-r7b-arabic-02-2025"

model, tokenizer = load_quantized_model(base_model_id)

  
  

# ========== SCHEMA MODELS ==========

  

class Turn(BaseModel):

    role: str

    content: str

  

class SummarizationInput(BaseModel):

    messages: List[Turn]

  

class TranslateModel(BaseModel):

    Translated_conversation: str

  

class SummaryModel(BaseModel):

    Diagnosis_summary: str

    Patient_symptoms: List[str]

    Recommendation: str

  

# ========== FUNCTION: CONVERSATION TO TEXT ==========

  

def convert_conversation_to_text_for_api(conversation: List[Turn]) -> str:

    result = []

    for turn in conversation:

        if turn.role == "assistant":

            result.append(f"Doctor: {turn.content.strip()}")

        elif turn.role == "user":

            result.append(f"Patient: {turn.content.strip()}")

    return "\n\n".join(result)

  

# ========== FUNCTION: TRANSLATE TEMPLATE ==========

  

def TranslateTemplate(ar_text: str, translate_model):

    return [

        {

            "role": "system",

            "content": "\n".join([

                "You are a professional translator.",

                "You will be provided with an Arabic text.",

                "Translate the text into English.",

                "Extract JSON details according to the Pydantic schema provided.",

                "Make sure that the values in the JSON are written in **English**.",

                "Respond ONLY with a valid JSON object that follows the schema – no markdown fences, no extra text."

            ])

        },

        {

            "role": "user",

            "content": "\n".join([

                "## conversation",

                ar_text,

                "",

                "## Pydantic Details",

                json.dumps(translate_model.model_json_schema(), ensure_ascii=False),

                "",

                "## Translation : ",

                "```json"

            ])

        }

    ]

  

# ========== FUNCTION: TRANSLATE GENERATE ==========

  

def TranslateGenerate(message, tokenizer, model, max_new_tokens=1500):

    input_ids = tokenizer.apply_chat_template(

        message,

        tokenize=True,

        add_generation_prompt=True,

        return_tensors="pt",

    ).to(model.device)

  

    gen_tokens = model.generate(

        input_ids,

        max_new_tokens=max_new_tokens,

        do_sample=False,

        temperature=None,

    )

  

    gen_tokens = [

        output_ids[len(input_ids):] for input_ids, output_ids in zip(input_ids, gen_tokens)

    ]

  

    gen_text = tokenizer.decode(gen_tokens[0], skip_special_tokens=True)

  

    match = re.search(r'\{.*?\}', gen_text, re.DOTALL)

    if not match:

        raise ValueError("No JSON block found in model output")

  

    json_block = match.group(0).strip()

    return json.loads(json_block)

  

# ========== FUNCTION: SUMMARY TEMPLATE ==========

  

def SummaryTemplate(en_text: str, summary_model):

    return [

        {

            "role": "system",

            "content": "\n".join([

                "You are an NLP data parser.",

                "You will be provided by an Arabic text associated with a Pydantic scheme.",

                "Generate the output in the same language.",

                "Extract JSON details from the text according to the Pydantic details.",

                "Do not generate any introduction or conclusion."

            ])

        },

        {

            "role": "user",

            "content": "\n".join([

                "## conversation",

                en_text,

                "",

                "## Pydantic Details",

                json.dumps(summary_model.model_json_schema(), ensure_ascii=False),

                "",

                "## Summarization : ",

                "```json"

            ])

        }

    ]

  

# ========== FUNCTION: SUMMARY GENERATE ==========

  

def SummaryGenerate(message, tokenizer, model, max_new_tokens=200):

    input_ids = tokenizer.apply_chat_template(

        message,

        tokenize=True,

        add_generation_prompt=True,

        return_tensors="pt",

    ).to(model.device)

  

    gen_tokens = model.generate(

        input_ids,

        max_new_tokens=max_new_tokens,

        do_sample=False,

        temperature=None,

    )

  

    gen_tokens = [

        output_ids[len(input_ids):] for input_ids, output_ids in zip(input_ids, gen_tokens)

    ]

  

    gen_text = tokenizer.decode(gen_tokens[0])

    gen_text = gen_text.replace("<|END_RESPONSE|>", "").replace("<|END_OF_TURN_TOKEN|>", "").replace("```", "").strip()

    match = re.search(r'\{.*?\}', gen_text, re.DOTALL)

    if not match:

        raise ValueError("No JSON block found in model output")

  

    json_block = match.group(0).strip()

    return json.loads(json_block)

  

# ========== STREAMLIT UI ==========

  

st.set_page_config(page_title="Medical Summarizer", layout="wide")

st.title("🩺 Medical Conversation Summarizer")

input_text = st.text_area("Conversation JSON:", height=300)

  

if st.button("Summarize"):

    with st.spinner("🔁 Running model inference... Please wait..."):

        try:

            parsed_json = json.loads(input_text)

            raw_messages = parsed_json["messages"]

            structured_input = SummarizationInput(messages=[Turn(**turn) for turn in raw_messages])

  

            ar_text = convert_conversation_to_text_for_api(structured_input.messages)

  

            translate_template_message = TranslateTemplate(ar_text, TranslateModel)

            translated_json = TranslateGenerate(translate_template_message, tokenizer, model)

            en_text = translated_json['Translated_conversation']

  

            summary_template_message = SummaryTemplate(en_text, SummaryModel)

            summary_json = SummaryGenerate(summary_template_message, tokenizer, model)

  

            st.success("✅ Summary generated successfully!")

            st.subheader("📋 Summary Output (JSON):")

            st.json(summary_json)

  

        except Exception as e:

            st.error(f"❌ Error: {str(e)}")
```

#### Run streamlit
```python
nest_asyncio.apply()

NGROK_AUTH_TOKEN = userdata.get("NGROK_AUTH_TOKEN")

ngrok.set_auth_token(NGROK_AUTH_TOKEN)

for tunnel in ngrok.get_tunnels():

    ngrok.disconnect(tunnel.public_url)

public_url = ngrok.connect(addr=8501)

print("🚀 Your API is live at:", public_url)

!streamlit run app.py &>/content/logs.txt&
```
### 
