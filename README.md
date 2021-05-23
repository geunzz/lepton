# lepton

This code collects thermal images using the Lepton sensor module in a Windows environment.
The lepton sensor is a sensor that visualizes the temperature of an object from each pixel. 
By converting the raw data of each pixel into temperature, the temperature of the corresponding point can be known, 
and the color difference according to the temperature can be checked as a thermal image.
It is a code that operates in the environment of Lepton 2.5 and 3.5, and displays a thermal image with Lepton. 
If you double-click on the displayed image, the thermal image is saved in the designated path.
Repton 2.5 can obtain an image with a resolution of 60x80 pixels, 
and Repton 3.5 can obtain an image with a resolution of 120x160 pixels, and this pixel value is stored as it is.


sample of saved image
---------------------

![FACE_gray_1](https://user-images.githubusercontent.com/84235639/119262376-f6730400-bc15-11eb-91f9-6613378c450b.jpg)
![FACE_map_1](https://user-images.githubusercontent.com/84235639/119262381-f8d55e00-bc15-11eb-9753-9c5a0b07d714.jpg)
![FACE_origin_1](https://user-images.githubusercontent.com/84235639/119262383-f96df480-bc15-11eb-8191-011fe433178f.jpg)  
  
Three types of thermal images are saved as shown in the picture above. 
The original shape without any processing on the thermal image is the picture on the far right. 
If you apply the rainbow palette filter here, the color image in the middle comes out. 
You can get the leftmost image by converting this image to gray scale using the opencv library.
You can get images of various colors depending on the palette type. 
Since the rainbow palette best represents the relative difference in temperature, this code chose to save the palette image.
If you want to use a different type of palette, you can apply a different filter value instead of the'colormap_rainbow' list in the colormap_lepton.py file.

If there is a problem with the provided dll file, you need to download and run the sdk file again from below path  
https://lepton.flir.com/software-sdk/  

