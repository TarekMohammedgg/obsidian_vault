---
---
#NLP #NLP_fine_tuning
### intro to llm : 
there are parameters affect on llm : 
1. temperature 
2. stop sequences 
3. frequency penalty 
4. presence penalty 

**Temperature:** 
range : [0:1]
definition : control on the llm if will be deterministic to the specific field he is talk about or not ? 
يعني مثلا لو بيتكلم في مجال الطب يبقي يفضل ملتزم بالكلمات المستخدمه بكثره في مجال الطب ، هكذا . 
**stop sequence:**
definition : prevent a llm from generating more text after a specific string appear like "Apple" or "End" . 

**frequency penalty:** 
range : [-2 : 2 ] if positive => reduce repeating , if negative => increasing repeating . 
definition : prevent llm from repeat token 

**presence penalty:**
range : if positive => make the model choose unique words . 
definition : control on the uniqueness of words 

**what is the diff between freq and presence ?**
freq penalty : introduce more unique words 
presence penalty : avoid excessive(التكرار المبالغ فيه) repetition . 

----
if i want to model answer in specific format we will use prompt engineering  

type of prompt engineering : 
1. few shot => give the model some hints 
2. chain of thoughts => give the model the explain of how we calculate it (useful in mathematical responding)
3. zero shot => make the model depend on your self 
4. self consistency => ask model more than one time and the model will take the common answers and make it the final answer  . 

----
**RLHF(reinforcement learning from human feedback):**
created by : chatGPT  
improve the efficiency of llm by guide the llm by human feedback . 
this technique use the next algorithm **PPO(proximal policy optimization)** => make the llm learn from mistakes without dramatically changing behavior  
this discuss how chatGPT good :
1. fine tune the model on conversation dataset 
2. make the model generate more responses and rank the answers by reward model this ranking from humas , so this option is so expensive . 
3. put reward model data into chatGPT again . 
**RLAIF(reinforcement learning from ai feedback):**
created by : anthropic 
use Ai (trained on human principles and rules ) for guiding another ai

---
### evaluating your llm (benchmark)
for fast generating llm use closed source models from anthropic or chatGPT 
we use common technique name : perplexity evaluation metric . 

**perplexity evaluation metric** 
هو عبارة عن معيارة لقياس مدي حيرة  الموديل علي عمل text بناءاً علي الداتا الي دخله ، فكلما قل كلما دل ذلك ان الموديل قادر يطلع more fluent and natural text و بيقوم بالحسبة دي من خلال انه بيقارن اداء الموديل مع الموديلز الاخري ... و لكن مينفعش اعتمد علي المعيار ده فقط ، لان مش كل الموديلز بيبقي متوفر فيها امكانية انها تدينا المعلومات الي زي دي و كمان المقياس ده مش بيعرفنا هل الموديل ده كويس في ال summarization مثلا ولا لأ (يعني مش بيعرفنا قدرة الموديل علي القيام بالمهام الدقيقة و المعقدة ولا لأ ) . 

### choose the suitable llm for specific task 
there are three factors is 
1. quality 
2. cost 
3. ease of  use for each 

#### how to improve exist llm 
using prompt engineering [[prompt engineering using langchain]]
**when use this option specially (few shot prompt):**
1. your task is not necessary knowledge specific 
2. your model has the answer 
----
use another technique is RAG (retrieve augmented generation) or deep memory by Activeloop
**when to use this approaches:**
1. when we use few shot prompt and the model still suffer from bad response . 
---
the last choice [[Fine Tuning]]
there are several approaches to do this : 
1. adjust the weights with a small learning rate => to minimally affect on the model's general abilities 
2. freezing the network weights and introducing new weights for fine tuning 
**when using fine tuning:**
3. when have more time 
4. have large amount of training dataset 
----
### LLMOps (large language model operations )


