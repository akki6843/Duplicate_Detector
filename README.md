# Duplicate_Detector
This task is aimed to perform a duplicate detection for a bulk of images. 

######################################################################################

1) Data_cleaner.ipynb:

For this task two datasets were provided 1) 5Gb dump 2)small 1.3Gb dump. Because of lim-
ited resources small dump was chosen for processing as big dump was simply not loading in
the system. As every product had 4 urls, only the 200x200 resolution was chosen for the pro-
cess. Moving-on, From the initial data review it was clear that only the following coloums
are required, [‘ProductId’, ‘title’, ‘description’, ‘imageURLstr’]. on further analysis it was
clear that description can lead to lot of false positive as a result ‘description’ coloum was
droped. Then title coloum was targeted which drastically helped it shortlisting the required
data. This required data was further filtered based on urls then productId. This filtering
helped the to shortlist the images from lakhs of images to only thousands.

########################################################################################

2) Method.ipynb

The file discuss the different methods that can be used to solve the task. It starts from sub-
tracting two images and calculating the pixel value difference. As this can be t he quick way
to check the similarity but, it can be very catostrophic as illumination and pose difference
can cause alot of noise. Therefore, moving towards a approach that can help us to take care
of data with its noise. So images were compared for there mse values. For this initial val-
ues for similar images were great but as image move away from similarity it gets dificult
to pin-point a threshold values for making the decision of similarity. Hence the method
of deeplearning is chosen as it can takecare of illumination, rotation and little noise in the
images. As a outcome deeplearning based feature extraction method is chosen for the task.

###########################################################################################

3) Downloader.ipynb:

As the name suggest this script downloads the images. For further simplicity and data track-
ing all images were downloaded and renamed with there respective product id example: .

##########################################################################################

4) Duplicate_detection_processor.ipynb:

In this file all the images that are downloaded are processed. Idea is to extract features using
pre-trained model. For this task VGG16 model is used trained on imagenet dataset. In this
file every image is passed through the network and features are extracted from ‘fc2’ layer.
Each feature is of size [1,4096]. So each image is now represented as a feature vector. This
feature vectors are then stored in a pickle file for later use.

############################################################################################

5) Duplicate_finder.ipynb:

Now that we have all the feature vectors for the images here, we calculate the features of
all the query images and calculate the euclidean distance between query image feature vec-
tor against precomputed feature vectors. And based on distance value we decide whether
image have a duplicate or not, if so the list of duplicates is prepared and then dumped in a
dictonary. The list of query images was taken to be 100 images because of limited processing
power. Final results are stored in json file as a dictonary.

##############################################################################################

6) Duplicate_checker.ipynb:

Here the design is made to process in a fashion of checking whether two image are duplicate
or not. Also here one more case is added where it takes one image as input and check all the
duplicates in the preprocessed vectors.
