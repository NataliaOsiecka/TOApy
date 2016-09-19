# -*- coding: utf-8 -*-

import csv
import cv2
import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as scil
import sys

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    temperature0 = sys.argv[2]
    rate = sys.argv[3]
    mode = sys.argv[4]
    action = sys.argv[5]
    
    if action == '--gray':
        temperature, toa = movie(filename, temperature0, rate, mode, gray)
    elif action == '--rgb':
        temperature, toa = movie(filename, temperature0, rate, mode, rgb)
    elif action == '--svd':
        temperature, toa = movie(filename, temperature0, rate, mode, svd)
        
    if action == '--rgb': 
        plot_data_rgb(temperature, toa)
    else:
        plot_data(temperature, toa)
        
    export_to_csv(temperature, toa)


def movie(filename, temperature0, rate, mode, function):
    vidcap = cv2.VideoCapture(filename)
    fps = float(vidcap.get(cv2.CAP_PROP_FPS))
    total_frame = float(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    number_of_frame = 0
    toa = []
    temperature_data = []
    temperature = 0
    while vidcap.isOpened():
        number_of_frame += 1
        ret, image = vidcap.read()
        #calculating temperature
        time = number_of_frame / fps
        xt = float(rate)*time/60.0
        
        #cooling mode
        if (mode == 'c'):  
            temperature = float(temperature0)-xt
        #heating mode
        if (mode == 'h'):
            temperature = float(temperature0)+xt
            
        print('time: {:3.3f} temperature: {:3.3f}'.format(time, temperature))
                
        x, y, z = image.shape
        smal_image = image[0:int(x*0.25), 0:int(y*0.25)]
        median = cv2.medianBlur(smal_image, 5)

        #u, s, vh = scil.svd(median)
        toa.append(function(median))
        temperature_data.append(temperature)
        
        #make svd analysis
        #show film and graph
        cv2.imshow('frame', image)
        
        key = cv2.waitKey(1) & 0xFF 
        
        if key == ord('s'):
            img = 'image' + str(int(temperature)) + '.png'
            cv2.imwrite(img, image)
            print(img +' is saved')
        elif key == ord('q'):
            vidcap.release()
            return (temperature_data, toa)
            
        if total_frame == number_of_frame:
            vidcap.release()
            return (temperature_data, toa)

def gray(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    s = cv2.sumElems(gray)    
    return s

def rgb(image):
    blue = np.sum(image[:,:,0])
    green = np.sum(image[:,:,1])
    red = np.sum(image[:,:,2])
    rgb = [blue, green, red]
    return rgb

def svd(image):
    gray = cv2tColor(image, cv2.COLOR_BGR2GRAY)
    u, s, vh = scil.svd(gray)
    return s[0]
       
def plot_data(x,y):
    plt.plot(x,y)
    plt.xlabel(r'Temperature [$^{0}$C]', fontsize = 16)
    plt.xticks(fontsize = 14)
    plt.ylabel(r'Intensity [a.u.]', fontsize = 16)
    plt.yticks(fontsize = 14)
    plt.grid()
    plt.show()

def plot_data_rgb(x,y):
    data = np.array(y)
    plt.plot(x, data[:,0], 'b', x, data[:,1], 'g', x, data[:,2], 'r')
    plt.xlabel(r'Temperature [$^{0}$C]', fontsize = 16)
    plt.xticks(fontsize = 14)
    plt.ylabel(r'Intensity [a.u.]', fontsize = 16)
    plt.yticks(fontsize = 14)
    plt.grid()
    plt.show()
    
def export_to_csv(x,y):
    z = list(zip(x,y))
    with open('toa_data.csv', 'wb') as f:
        writer = csv.writer(f)
        for item in z:
            writer.writerow(item)
  
if __name__=="__main__":
    main()




    
