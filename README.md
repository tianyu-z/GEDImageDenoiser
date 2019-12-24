# Denoising_Residual_Learning

## Section 1. Structure of this repository.
 
There are in total twelve folders presented in this repository.
1.1 The data folder (zipped) consists of 3 subfolders: Train, training datasets; 68 and 12 consisting of 68 images and 12 images for testing.
1.2 The Beta_estimator_VGG corresponds to the classification model which is trained to detect the beta level of each given noisy picture.
1.3 The seven folders beta0.83179394, beta0.90207981, beta1.14831186, beta1.4063303, beta1, beta2, beta6, contains the code and trained model for each beta level correspondingly. Within each folder:
- To train the model, the code files are utils.py, dataset.py, models.py, train.py.
- The “logs” subfolder contains the trained model.
- The log.txt file is the log during training.
- To test the model, the code files are test.py, testT.py, testGED.py, whose purpose is to test the model based on the test dataset (either 12 or 68) and based on the given noise (either Gaussian noise or noise with fat tail). The log files during testing are also presented in this folder and are named correspondingly.
1.4 The orgb10, and orgs10 are two folders for the original model. The files in these two folders have the same structure as the seven folders with name starting with “beta”.
1.5 Denoised picture for set 12 contained the noisy picture and clean picture of the test dataset 12.

## Section 2. How to use this repository.

If you have a ground-truth picture and you would like to the effect of our model. You may copy and paste your image to [the model you want test]/org/Set68 and run the test.py under this folder to see the PSNR of the denoised picture based on your ground-truth picture with artifical noise. You may choose the model which gives a denoised picture with the highest PSNR.

If you don't have a ground-truth picture. You have a picture with noise and you want to denoise it. We cannot calculate the PSNR under this circumstance because the original picture is needed when calculating PSNR. You need to [download](https://drive.google.com/open?id=1JY9jBRAHLjDyIryFfgLIybn9qaQ8LAnG) a VGG beta estimator to estimate the beta and then choose the corrsponding model to denoise your pending pictures. The VGG estimator is a classifier with ten classes with an top-1 arrcuracy of 55%. (We believe there are some room for improvement). The mapping from the class label to the beta of the model is as follows.

class label | beta estimator
:-: | :-: 
0 | 6 
1 | 2
2 | 1.40633033 
3 | 1.14831186
4 | 1 
5 | 0.90207981
larger than 5 | 0.83179394
