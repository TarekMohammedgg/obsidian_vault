---
---
###### halftoning : 
- convert gray scale images to (0,1) images  
- Halftoning is irreversible 
**simple halftoning**
- using just threshold
**advanced halftoning (error diffusion )**
- usingg threshold + Error diffusion matrix (summation (old - new ) , then propagate to neighbors)

---

###### histogram 
- represent the frequency of gray levels on the x-axis 
- histogram Equalization : spread the gray levels on the x- axis 

---

###### Edge detection 
- detect the image (size , shape , texture )
- the sum of mask values is Zero ,because we want to ignore the flat (like white wall ) areas and focus on the area the bright changed suddenly (like the end of  the wall) . 
**(using convolution ) Edge detection (RSPKRL + quick mask )**
- Roberts 
- sobel 
- prewitt 
- kirsch 
- robenson 
- laplacian 
**(using substraction operations ) Advanced Edge detection (H , D , DOG , variance , range )**
- homogenity 
- difference 
- DOG 
- variance 
- contrast detection 
- edge enhancement (overlay)
- range 

----

###### Spatial Frequency : refers to the rate of change  
- binary masks : 0 or 255  
- grayscale mask : range from 0 to 255
- low flrequency : change gradually 
- high frequency : change rapidly 

**filters :**
- the sum of filters not aim to find the edges or change the contrast that is like tool help to find it not track it ..... so the sum of masks is equal to 1 (that mean not make changes on the brightness)
**low filter (transition  smooth )**
- center is positive weight and the corner pixels have lower
- Mask type type is : average convolution mask ...summation equal 1 
- weights

**median filter :**
- special from low filtering for noise removal without distroting noise free areas , replace the center pixel with the median , No convolutoin require need just sorting the pixel values . 
- used for remove Noise (specialy salt and pepper Noise ) 

**high filter (sharp changes)**
- strong positive value in the center and negative surrounding
- Mask summation equal 1 
- frequency(using fourier transform) vs. spatial filtering (using convolution mask) : spatial filtering is more simple and fast  than frequency domain  

----

###### image operations 
- addition 
- substraction 
- blank image 
- inversting (255 - x ) 0 -> 255 , 1 -> 254 

---

###### histogram based segmentation 
- multimodal => multiple peaks 
- bimodal => two peaks 
- segmentation => divide an image  into groups (shape , texure , intensity )
- high peak => background 
- smaller peak => object 
**before histogram we should do some operations :** 
1. histogram equalization 
2. high filter 
3. histogram smoother 
**thresholding :** 
1. manual 
2. histogram peak 
3. valley avoid overlap can happend in the histogram peak technique 
**adaptive** 
1. first segment : apply high peak technique 
2. second segment : mean values and tehn apply any thresholding technique . 

- region growing (optional): group  pixel and assign unique label   (depend on check connectivity )

----

###### Manipulation shape 
- we apply the manipulation shape just on segmentation images (binary images )
- **Erosion and dilation** 
- Erosion: قيم البكسلس ١ متطابقة تطابق كلي 
- Dilation : قيم البكسلس ١ متطابقة تطابق جزي ، يعني حتي لو حدث تطابق لبكسل واحده 
 و الأساس اصلا أننا بتاخد القيمة الي في منتصف الماسك و بننتقل بها في الصورة الأصلية .

- Erosion and Dilation are sensitive to sturcture element size 
**Opening and closing**
- structure element == mask that apply on the image 
- opening : use erosion first and dilation second , used to seperate objects from each other  
- closing : use dilation first and erosion second  , used to fill gaps and black hols 

**special opening and closing**
- more control on opening and closing 

**outlining**
- used as edge detector

- interior :substract erode image from original image  
- exterior : substract original image from dilation  image 

**thining and skeletonization**
- thining : make the image structure to one pixel 
- skeletonization : make the medial axis , to know more about the structure of the image  . 

----

###### Boolean and Overlays 
**Boolean**
- applicatons 
- Masking : using AND  boolean 
- Labeling : using XOR boolean 
**Overlay**
- Double Exposure : using average overlay 
- Framming 

