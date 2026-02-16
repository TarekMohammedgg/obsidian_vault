---
---


## what is Image segmentation ? 
image segmentation meaning divide an image into regions or objects 

## what is the most common and simple  segmentation  technique ?
segmentation is based on histogram and image thresholding  
## what is the main idea from segmentation ? 
to group individual pixels together into regions 
## what is the meaning of similarity  ? 
similar can mean they are the same intensity (shade of gray ) , from a texture 

## what is the main component in the image ? 
background (one gray level and it's have large peak ) and object (another gray level and it's have smaller peak ) in the histogram 
مع الاخذ في الاعتبار : 
the largest peak represent the background and the next largest peak the object . 


## what is the function of histogram and thresholding in histogram-based technique ? 
histogram for illustrate the gray levels in the image , the largest is background and the next largest is object or subject , and thresholding for separate object from background 

## how the thresholding separate the background and object in the histogram-based technique ? 

in this example  , 
ال thresholding بيبقي موجود في المنتصف ما بين اعلي نقطة الي هي ال background و تاني اعلي نقطة الي هي object و بالتالي الي بيقي اقل من ال threshold بيبقي ال background و بعض النقاط (intensity points )  و الي ممكن تقول انها errors و الي بعد ال threshold بيبقي object and some intensity points . 

## what is the main problem in the histogram-based technique ? 
the main problem is select the thresholding correctly without try and errors  , because there are many  difficulties like : 
\- noise and low - contrast 
\- histogram is based on bimodal (background and object )  this mean in real world images (that have many gray level) , it is difficult to select the correct threshold . 

## what is the function of Region Growing ? 
is to group the  pixels in each separated regions  and gives them unique label , this step happened after apply thresholding  on the image (split pixels into zero's and one's )
**how it implementation**

## what is the types technique in histogram-based Technique ? 
Manual segmentation 
high peak histogram 
high valley histogram 
adaptive technique 

## what is the properties of Manual Technique ? 
\- it is try-error nature 
\- is good for fine tuning and understanding the operation
\- is input parameters (high and low threshold  , value parameter and segment parameter)

## what is the function of value  parameter and segment parameter in Manual histogram technique ? 
**value parameter** : make the values outside the high-low threshold be Zero 
**segment parameter** : parameter specify whether or not to grow regions after thresholding

----
###### Notes 
 Chapter 10 - edge base and growing region

What is the diff between edge base and histogram based ? 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdhGvPZ5kJ96UL_nw1q6jWgjrrl3NdVMcKzLxEOFWgpPZb8KLMm2gqktLNAJRDR6tCOq36QQ9isAz5TD0Xf2M-ZdlVMooCCrYjemxmVgz7dJ1gonHSZbEHeVmN9ex32OuI4DCrc7g?key=_RuxG6s85nOQGE102pRkyo_5)

  

In edge base method we can solve the problem of Noise sensitive by the next methods  : 

1. Median filtering : remove large pixels 

2. High filtering : the output have many large numbers (spikes ) 

3. Low filtering : the output will be one’s 
----

## Chapter 11 - morphological filters 

Brief review on chapter 11 ( Morphological Filter ) 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdgF7L4jQPhI9A7mOgi-tBElqH97w6BY-VQCxfoxD2ELgoV8PizWBugOoR7Es97iBUDQ1fHluqSA_eCvwkn-XFESKnXaxck7mvl_f5PKqbNCAXLr9RgsO56hA1th9dhgTOWMbG8iw?key=_RuxG6s85nOQGE102pRkyo_5)

  

[university hand image processing chapter 11 summarize.jpg](https://drive.google.com/open?id=1lWGKCEASRzv_si_gLNy7gTC4efrtxQjE)

----
## Chapter 12 - Boolean and Overlay operations 

What is the types of Overlay operation and what is the affect of each other : 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfGGDGX3zU9CFoTHQs-KNXSTWs0LVulJMfEBWE0kxK-gQkhHwO_HqxnKl-CcUv70iLS44t8WV8rdfwYk00CoLJCwMiwNYvazGxWBReuIKEccJhuQus1F14mEv7OaXOX8kmTXrkD9w?key=_RuxG6s85nOQGE102pRkyo_5)