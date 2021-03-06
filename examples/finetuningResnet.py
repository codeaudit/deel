from deel import *
from deel.network import *
from deel.commands import *
from deel.network.resnet152 import *
#from deel.network.googlenet import *
import chainer.functions as F
import time

deel = Deel(gpu=0)
from chainer import cuda
cuda.cudnn_enabled=False
CNN = ResNet152()
BatchTrainer.batchsize=12
BatchTrainer.val_batchsize=4
Deel.defferedTuning=True

InputBatch(train="data/train.txt",
            val="data/test.txt")

def workout(x,t):
   CNN.batch_feature(x,t) 
   return CNN.backprop(t)

def checkout():
   CNN.save('model_google_cpu.hdf5')

BatchTrain(workout,checkout)
