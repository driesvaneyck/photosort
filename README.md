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
Photosort directly alters your file names by adding a prefix or by placing undesired files in a subdirectory.

In the config tab select the folder with your images by pressing the master button.
With th slave button you can select a folder with raw or png files corresponding to the files in your master folder. All operations executed on files in the master folders will be mirrored on the files in the slave folder. Selecting a slave folder is optional.  
When you selected a master folder (and optionally a slave folder) press the select-files button. This will load the images.   
Different possible operations:.  
- Sort: repeatedly select the best of two pictures (quicksort) untill you ordered all pictures. Faster if the amount of photo's you have to go trough is smaller. Recommended to uwe this operation last.   
- Screening. Simple pass fail filter for all photo's. Use this to trim collection of the worst photo's. The photo's you didn't select are moved to a subdirectory.  
- Bucket:  you van use this option to sort pictures in up to six categories.  
- Duplicates(bannish): use this to compare simmilar photo's and only keep the best one. The photo's you didn't select are moved to a subdirectory. Duplicates works via drag and drop. Drag and drop the similar photo's from your master of slave folder into the text field above the 'sorteer' (sort) button. Press that button after. Dropping the files.  


After each completed operation (when the doen screen appears) reload the image array by pressing the 'selectFile' button in the config tab. The duplicates(bannish) tab is the exception to this rule.

The sort, duplicates and screenng operations are operated by using numpad-4 and numpad-6. The bucket tab is operated by using the numpad-7, -8, -9, -4, -5, -6 keys to sort the files into buckegs 1,2,3,4,5,6 respectivly. Each opperation can be terminated prematurely with partial results by pressing numpad-0.

