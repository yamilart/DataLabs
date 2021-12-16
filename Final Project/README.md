# Who let the dogs out? 🐾

Final Project: A dog Breed Recognition Project

### A Data Analysis Project...

**With images!**

As my final project I decided to dig into Computer Vision and create a Dog Breed Recognition program because... why not?


## About
 
**The basics**

I decided to work with a dataset from Kaggle that I customize to my needs because it didn't have any Dachshunds...  

- [The data](https://drive.google.com/drive/folders/1BZqDlhpX9AAszha3SD8K6k6g_JAr8RuP?usp=sharing)
- [The Final Notebook](https://github.com/yamilart/DataLabs/blob/main/Final%20Project/Final_Project.ipynb)
- [The App Process](https://github.com/yamilart/streamlit-dogbreed)
- [The Failed Attempts](https://github.com/yamilart/DataLabs/tree/main/Final%20Project/how-about-no)
- [The extra cute pictures for testing purposes](https://github.com/yamilart/DataLabs/tree/main/Final%20Project/extra-cute-pictures)
- [The Final Presentation](https://github.com/yamilart/DataLabs/blob/main/Final%20Project/Final%20Project.pdf)


## The process

My data consisted in over 10000 dog pictures classified in 120 breeds.  
Since that was going to take a lot of time and computer power to build i decided to use only 20 breeds, wich resulted in around 1600 pictures.    
The selected breeds were:    
<img width="887" alt="Screenshot 2021-12-16 at 20 01 44" src="https://user-images.githubusercontent.com/81629326/146432511-70165b8d-734b-4039-a6d6-57bb8ecd0425.png">

After the seleccion and several failed attempts I decided to build a sequential model using a pre-trained ResNet50 layer.   
Basically: a layer that already recognizes images, so it would be easier for it to learn and it could give a good accuracy.  
The said results were:    
<img width="487" alt="Screenshot 2021-12-16 at 20 04 23" src="https://user-images.githubusercontent.com/81629326/146432818-279bf517-5d9f-4ee9-aa72-81adc2fdd708.png">  
<img width="212" alt="Screenshot 2021-12-16 at 20 04 34" src="https://user-images.githubusercontent.com/81629326/146432843-3b0cb7ec-c1fa-4b08-8ab3-166fc70d8bf5.png">


## The App!

*Hey mom! I created an app!*.   
After some struggle and few hours of sleep I managed to deploy my model and to use it with any updated picture.   
[**Try it out!**](https://share.streamlit.io/yamilart/streamlit-dogbreed/breed_app.py) (remember it only works on the 20 breeds mentioned before)   
In case it's not working, here are some screenshots of the outcomes: 


<img width="500" alt="Screenshot 2021-12-16 at 19 34 58" src="https://user-images.githubusercontent.com/81629326/146433405-8bcaa939-c2b1-40bb-9d14-190bb05d20eb.png">  
<img width="500" alt="Screenshot 2021-12-16 at 19 35 49" src="https://user-images.githubusercontent.com/81629326/146433411-4a564419-274b-460f-aae6-4786742ac05e.png">  
<img width="500" alt="Screenshot 2021-12-16 at 19 35 18" src="https://user-images.githubusercontent.com/81629326/146433409-556c2d5a-f9fd-4b94-a77e-c797ac8f2ee4.png">  

