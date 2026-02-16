---
share_link: https://share.note.sx/millgcur#N9NVMBCZEg7tDNCfso4f7z+1O5SfA+6U9dao6WlGsEQ
share_updated: 2025-05-04T13:07:31+03:00
---
ال ctc هو بديل للطريقة التقليدية الي كنا بنستخدم ال [[sr - Hidden Markov Model - HMM]] في الاول . 

---

الفكرة دلوقتي اني عايز اعمل classification للصوت الي جيلي بحيث مثلا لو دخلت في ال input 

Cat 

هي عبارة عن frames كتير جدا فانا عايز اخذ كل حبة فريمات و اصنفهم c   -    a   -  t مثلا كده ، فعشان الموضوع يتم بشكل اتوماتيكي و ميكنش مرهق هنحتاج لل ctc و هنعبر عن ال input بال X و ال length بتاعها هيكون T فيبقي عندك مثلا 
```
X = [x1 , x2 , x3 , .... , xt]
```

و ال output بال Y و ال length  بتاعها هيبقي U فيبقي عندك مثلا 
```
Y = [y1 , y2 , y3 , .... , yu]
```

الفكرة بقي انك هيبقي بالشكل ده ال  T > U غالبا ده لو مكنش دائما و ده بسبب ان عدد ال frames هيبقي اكتر من عدد ال labels or classes . 

CTC : 
- loss function 
P(Y|X)
- inference : 
$Y^{*}$ = argmax(P(Y|X))

- algorithm : 
الالجوريزم يبقي ماشي ازاي بقي ، انك بتاخد اكبر عدد من ال alignments في ال input 
1. [c,c,a,a,a,a,t,t] => X
2. [c,a,t] => Y 
الطريقة دي فيها مشاكل ، مثال بقي لو الكلمة نفسها فيها حروف متكرره زي مثلا hello في الحالة دي هيطلع helo ، طب عشان نحل المشكلة دي هنعمل حاجه اسمها Blank 
1- [h,h,e,blank , blank , l , l , blank l , o]
2- [h,e,blank,l,blank,l,o]
3- [h,e,l,l,o]
بس الموضوع بقي هيبقي معتمد علي المكان الي هتحط فيه ال blank يعني تختار المكان المناسب . 


عشان بقي نطبق فكرة ال prediction بشكل صحيح هنعمل ال neural network عشان نطلع بال prediction output و عشان نقلل عدد ال input الي داخله علي ال neural network هنعمل grouping للقيم المتشابه فالبتالي هيطلع عندي 

Z = [blank , h , blank , e ,  blank ,l , blank , l , blank , o , blank ]


---
### inference 
نيجي بقي بعد ما جبنا اكثر ال alignments المتكرره عايزي بقي ناخد اكتر واحد ما بينهم كلها زي نظام كده ال SoftMax . 


فيه مشكلة ممكن تقابلني اثناء قياس ال probability  بتاع كل alignment ممكن تقابلني الـ case دي : 

[a , a , a]  , [a , a, blank ] , [b , b , b ]
و لاقين ان مثلا  ال [b , b, b] هي الاعلي من حيث ال probability هي الاعلي في حين مثلا لو جمعت الاتنين الباقين مع بعض هتكون النسبة بتاعتهم اكبر من الثلاثة b ، و من هنا ظهرت المشكلة و الحل في الحالة هي اننا نعمل merge to same alignments كخطوة اخيره و بعدها نعمل ال argmax ، طب و هنبحث ازاي بقي عن same alignments الي هنعملهم merge هنستخدم حاجه اسمها ال beam search . 

والي بيعمله ال beam search انه بيقرب المسافات و بيصغر حجم ال map الي المفروض تتعمل لكل حرف ، بحيث لو حرفين ليهم نفس ال output خلاص نجمعهم مع بعض زي فكرة [a,blank, b] هيطلع في الاخر [a,b] و برده لو عملت [a,b] هيطلع في الاخر برده [a,b] هنروح مجمعين الاتنين مع بعض من غير ما نكمل بقي حسبه ملهاش لازمه . 

$Y^{*}$ = argmax P(Y|X) . $P(Y)^{a}$ language model . $L(Y)^{\beta}$ word insertion bonus

- language model : 
احتجناه لان ال CTC بيبقي independency مش معتمد علي حاجه غير هو بس ولا الي قبليه ولا الي بعديه، فلازمة ال language model اني يظبط الكلام الي طالع طبقا لل context 
- word insertion bonus : 
  عشان يخليه يفضل الاجابات الاقصر اكتر من انه يسهب في الكلام  .
---
في النهايه ممكن نستبدل ال CTC  بال transformers و ده هيبقي احسن طبعا لان ال CTC قولنا انه مش بيحسب الكلام طبقا لل context بل احنا بنحتاج معاه ال language model ، علي عكس ال Transformers بيبقي معاه ال context في الحسبان 

--- 
خلي بالك الفرق  بين [[sr - Hidden Markov Model - HMM]] ، و ال ctc ان ال ctc بيبقي independent لاما قدام لاما وراء لاما زي ما نت  و لكن ال hmm اقدر اروح لكل حته في ال word context 

---
at => frame level 
st => word 
[at-1 , st-1 ] => move  forward 
[at-1 , st ] => stay 
[at-1 , st-2] => skip forward 

---
فيه طريقتين احدث من ال CTC : 

### RNN transducer : 
و هنا هنستخدم language model عشان يقول الكلام المستقبل المتوقع عكس ال ctc  و بعدين Encoder زي مترجم مبديء  و بعملهم Joint network و يخش علي softmax و بعدين ال ctc عشان يعمله alignment و يديني القيمة النهائية ، يعني تقدر تقول انه شكل محسن من ال ctc العادي . 

 ----
### Attention Based End to end 
Encoder -> Attention + language model + Decoder + softmax  



----
lectures 16 , 17 : https://chatgpt.com/share/680f1ff8-e5f8-800a-bc00-b776e156fa3f


chapter 10 link : https://chatgpt.com/share/680f1fe5-4ff0-800a-8cbb-1711cb806aca


