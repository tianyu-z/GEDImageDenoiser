import cv2
import os
import glob
import numpy as np
import torch
import torch.nn as nn
from torch.autograd import Variable
from models import DnCNN
from utils import *

def ensemble_result(modeldictsNames, logdir, test_dataset = ['Set12', '02.png'], noiseType = 'GED', beta = 2, test_noiseL = 25):
    def normalize(data):
        return data/255.
    def unnormalize(data):
        return data*255.
    def getSize(noise):
        k = 1
        for i in range(len(noise.size())):
            k *= noise.size()[i]
        return k
    def getAlpha(std, beta):
        return np.sqrt(np.square(std)/(gamma(3/beta)/gamma(1/beta)))
    test_data_dir, picName = test_dataset
    noised_pic_arr = []
    denoise_pic_arr = []
    PSNR_arr = []
    for modelname in modeldictsNames:
        net = DnCNN(channels=1, num_of_layers=17)
        device_ids = [0]
        model = nn.DataParallel(net, device_ids=device_ids).cuda()
        model.load_state_dict(torch.load(os.path.join(logdir, modelname)))
        model.eval()
        f = glob.glob(os.path.join('data', test_data_dir, picName))[0]
        # image
        Img = cv2.imread(f)
        Img = normalize(np.float32(Img[:,:,0]))
        Img = np.expand_dims(Img, 0)
        Img = np.expand_dims(Img, 1)
        ISource = torch.Tensor(Img)
        # noise
        if noiseType == 'uniform':
            noise = torch.FloatTensor(ISource.size()).uniform_(-1.732*test_noiseL/255.,1.732*test_noiseL/255.)
        elif noiseType == 'GED':
            flatSize = getSize(ISource)
            alpha = getAlpha(test_noiseL/225.,beta)
            noise = torch.FloatTensor(gennorm.rvs(beta, scale = alpha, size = flatSize, random_state = None))
            noise = noise.view(ISource.size())
        # noisy image
        INoisy = ISource + noise
        INoisyTBSave = INoisy
        INoisyTBSave = INoisyTBSave[0,0,:,:]
        INoisyTBSave = unnormalize(np.float32(INoisyTBSave))
        INoisyTBSave = np.expand_dims(INoisyTBSave, 2)
        cv2.imwrite('Noised_pic'+test_data_dir+picName,INoisyTBSave)
        ISource, INoisy = Variable(ISource.cuda()), Variable(INoisy.cuda())
        with torch.no_grad(): # this can save much memory
            Out = torch.clamp(INoisy-model(INoisy), 0., 1.)
        ## if you are using older version of PyTorch, torch.no_grad() may not be supported
        psnr = batch_PSNR(Out, ISource, 1.)
        Out = Out[0,0,:,:]
        Out = unnormalize(np.float32(Out.cpu()))
        Out = np.expand_dims(Out, 2)
        cv2.imwrite('denoised_pic'+test_data_dir+picName,Out)
        noised_pic_arr.append(INoisyTBSave)
        denoise_pic_arr.append(Out)
        PSNR_arr.append(PSNR_arr)
      max_PSNR = max(PSNR_arr)
      max_idx = PSNR_arr.index(max_PSNR)
      max_deNoisedPic = denoise_pic_arr[max_idx]
      max_NoisedPic = noised_pic_arr[max_idx]
      return max_NoisedPic, max_deNoisedPic, max_PSNR