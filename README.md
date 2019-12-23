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

