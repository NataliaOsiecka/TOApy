# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:27:51 2016

@author: natalia
"""
from __future__ import print_function
import sys

try:
    import csv
    print('csv:', csv.__version__)
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
    print("Our hint: Please try write in console 'pip install csv'")
    
try:
    import cv2
    print('cv2:', cv2.__version__)
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
    print("Our hint: Please try write in console 'pip install opencv'")

try:
    import matplotlib
    print('matplotlib:', matplotlib.__version__)
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
    print("Our hint: Please try write in console 'pip install matplotlib'")

try:
    import numpy 
    print('numpy:', numpy.__version__)
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
    print("Our hint: Please try write in console 'pip install numpy'")
    
try:
    import scipy
    print('scipy:', scipy.__version__)
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
    print("Our hint: Please try write in console 'pip install scipy'")


