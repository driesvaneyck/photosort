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