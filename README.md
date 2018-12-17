# photosort
photo collection screening tool in python

#Depends on packages:
-------------------------

PyQT4, numpy, rawpy, imageio

Installation notes:
-------------------------

>$ sudo apt install python-pip  
>$ sudo apt-get install python-qt4  

Install libraw version 19.1 (the default version: 19.0 does not work on linux!): https://www.libraw.org/

Install rawpy from source on Linux/macOS: https://pypi.org/project/rawpy/

installing rawpy:  
> git clone https://github.com/LibRaw/LibRaw.git libraw  
> git clone https://github.com/LibRaw/LibRaw-cmake.git libraw-cmake  
> cd libraw  
> git checkout 0.19.0  
> cp -R ../libraw-cmake/* .  
> cmake .  
> sudo make install  
> pip install numpy  
> pip install rawpy --no-binary rawpy  

Install imageio  
> pip install imageio  



Startup
-------------------------

Run command:  
>$ python photosort_main.py  


Usermanual:
-------------------------
usermanual.pdf

In the config tab select the folder with your images by pressing the master button.
With th slave button you can select a folder with raw or png files corresponding to the files in your master folder. All operations executed on files in the master folders will be mirrored on the files in the slave folder. Selecting a slave folder is optional.  
When you selected a master folder (and optionally a slave folder) press the select-files button. This will load the images.  
Different possible operations:. 
Sort: repeatedly select the best of two pictures (quicksort) untill you ordered all pictures. Faster if the amount of photo's you have to go trough is smaller. Recommended to uwe this operation last.  
