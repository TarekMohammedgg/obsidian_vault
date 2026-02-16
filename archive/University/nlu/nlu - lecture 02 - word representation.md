---
---
## types of word vector representation  ?
### Static vector representation 
الكمبيوتر بيعبر عن الكلمة الواحده ب vector واحد مها كان زي كلمة "broke" حتي لو السياق و المعني اختلف . 
### Contextual vector representation 
نخلي الكمبيوتر يبقي اذكي و يقدر يفهم الجمله كلها. 


------
**Attention:**
- اخلي الموديل يزكز علي بعض الكلمات عن غيرها و يديها قدر اكبر من الاهتمام . 
----
**Positional Encoding:**
- save the arrange of each word and can diff between ABC and CBA
----
### Models 
#### Bert : 
- بيحاول يفهم معني الكلمة بناء علي السياق من اليمين و من الشمال . 
- بيعتمد علي ال Transformers 
- و بيعتمد علي static mask 
- use Masked language model 
#### Electra : 
- بيحل مشكلتين في ال bert الا و هما جزئية ال pretrain and finetune ، و جزئية ال mlm just 15% from tokenize 
- نفس فكرة ال Bert و لكن الفرق بقي انه بيحط اكتر من طبقة لفهم الكلمة . 
- ابطأ من ال Bert عشان بيعتمد علي ال LSTM
- have special layers (generator and discriminator )
---
#### T5 : 
- بيقدر يعمل كل حاجه و ان كل مهمة بتبقي seq2seq ، و بيتم تدريبة من خلال انه يخفي اجزاء من الجملة و محاولة تخمينها . 
----
#### RoBERTa : 
- Not use binary next sentence prediction and use dynamic masked . 
- زي ال Bert ولكن مع تدريب اطول و بيانات اكتر ، و كمان علي اساس ال  
- بيعتمد علي ال dynamic mask hidden
-----
#### GPT : 
- بيعتمد علي الفهم من جهة واحده علي عكس باقي الموديلز 

---
#### Bart 
= bert + GPT 

---
#### xLNet 
- solve problem the musked not depences 
-----
## Notes 
### Seq2Seq : 
- عبارة عن هيكلية ، مميزاته انه مناسب في عمليات الترجمة او التلخيص (Encoder and decoder ) ، و لكن عيوبة انه بينسي بسرعة و لكن بعد ما تم اضافة ال attention ليه تحسن بشكل كبير . 
### Positional Encoding 
1. Absolute 
2. Frequency 
3. Full complete  
### binary next sentence prediction 
- positive : الجملتين وراء بعض يعني الجملة التانية كمالة للاولانية 
- negative: الجملتين مختارين بشكل عشوائي   
### Distillation 
- Standard (teacher para frozen , student update)
- multi teacher (multi teacher)
- co distillation (online distillation , the teacher and student are learned)
- self distillation (not transfer , but learn the basics)
-----
Bert => Encoder , bidirectional 
GPT => Decoder  , unidirectional 


