---
---
#NLP #Word_Embedding


في العادة يكون تمثيل الكلمات علي صيغة     hot-1 . 
 و ده ليه عيوب منها إنه بيصعب مهمة ال Represent Generalization علي  Pattern يمشي عليه بسبب تمثيلها المصمط للكلمات مثال : 
 Orange => (6257) 
 Apple => (456) 
 يعني هنا مثلا  مفيش علاقة ما بين القيمتين علي حسب التمثيل ده بالرغم من ان الاتنين من نفس ال category ، و لكن التعبير المكتوب بيه مش بيقول كده . 
### word Embedding representation 
Each word is represented as a vector of real N 

الفكرة اني هدي لكل كلمة مجموعة probability بناء علي معايير معينة بحيث الكلمات القريبة و المتشابهة من بعضها بيبقوا جنب بعض اثناء تمثيل الكلمات 2D ، و ده بيدي معني اكتر للكلمات و يخلي ال Algorithm قادر يصنف الكلمات الي اجزاء و يعرف ايه المتشابه و ايه غير المتشابهه . 
#### properties of word Embeddings 
cosine similarity **Sim(u,v )** =  $u^(T)\dot{v} /\lvert u \rvert .\dot{\lvert v \rvert}$ 
![](../assets/assets/Pasted image 20241009222405.webp)
### Word2vec model 
word2vec => skip-gram and CBOW 
طريقة مريحة و يسيطة لمعرفة ال Embedding بتاع الكلمات 

**Skip-grams** : predict surrounding context words given word  (target -> context) 
Negative words : هي الكلمات التي ليس لها علاقة بالكلمة الهدف 
**CBOW**: predict target word give surrounding context words (context -> target)

### Glove word (Global vectors for word Representation)
helps us to understand and work with the meanings of words by turning them into vectors , these vectors are based on how words appear together in large texts . used commonly in Wikipedia . 

**How it works** 
1. counting words pairs : counts how often every word appear near every other word this table called a **Co-Occurrence** 
	for example : how many times 'king' appear near 'queen' 
2. learning word vector : Represent each words as a vector so that the relation between these vectors 
3. weighted importance : Give more importance to pairs that appear together , frequently and less importance to rare pairs 
4. Training the model 

### The diff between word2vec and glove ? 
**word2vec (skip-gram , cbow )** : looks at small pieces of text and learns from them 
**Glove** : looks at big picture and count how often words appear together 

---

### Draft 
**Negative words**  : هي الكلمات التي ليس لها علاقة بالكلمة الهدف 
used in NLP to speed up of model's learning 
Example : 
If the sentence is "The dog barked loudly," and "dog" is the target word, then:

Positive words (actual context): "the", "barked", "loudly".
Negative words (random, unrelated): "apple", "computer", "mountain" (words that do not appear near "dog" in the current context).
