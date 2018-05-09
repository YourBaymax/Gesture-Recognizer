#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 01:01:43 2017

@author: abhisheksingh
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
from keras.optimizers import SGD,RMSprop,adam
from keras.utils import np_utils

# We require this for Theano lib ONLY. Remove it for TensorFlow usage
from keras import backend as K
K.set_image_dim_ordering('th')

import numpy as np
#import matplotlib.pyplot as plt
import os
import theano
from PIL import Image
# SKLEARN
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import json
        
