# Duplicate_Detector
This task is aimed to perform a duplicate detection for a bulk of images. 

Data_cleaner.ipynb:
For this task two datasets were provided 1) 5Gb dump 2)small 1.3Gb dump. Because of lim-
ited resources small dump was chosen for processing as big dump was simply not loading in
the system. As every product had 4 urls, only the 200x200 resolution was chosen for the pro-
cess. Moving-on, From the initial data review it was clear that only the following coloums
are required, [‘ProductId’, ‘title’, ‘description’, ‘imageURLstr’]. on further analysis it was
clear that description can lead to lot of false positive as a result ‘description’ coloum was
droped. Then title coloum was targeted which drastically helped it shortlisting the required
data. This required data was further filtered based on urls then productId. This filtering
helped the to shortlist the images from lakhs of images to only thousands.
