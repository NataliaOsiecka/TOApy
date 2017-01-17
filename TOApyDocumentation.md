---
title: TOApy Documentation
author: Natalia Osiecka
date: Kraków, 2016
papersize: A4
fontsize: 12pt
geometry: margin=3.5cm
fontfamily: palatino
header-includes:
    - \usepackage{fancyhdr}
    - \pagestyle{fancy}
---

1. Introduction
===============

TOApy is a simple, yet powerful program for the analysis of movies recorded during thermoopltical examination of samples by means of polarising microscope, e.g. while studying polymorphism of liquid crystals. It addresses the needs of ever growing research community using a wealth of equipment for the thermooptic analysis. TOApy has been designed for easy of use, speed and automated operation. It takes a necessary minimum of input and requires little user experience, so even a novice user is not likely to encounter any problems. A live preview feature with a freeze-frame option offers the user an opportunity to capture an image of choice corresponding to the thermodynamic state of the sample under study. TOApy used three different algorithms to obtain thermooptical analysis plot. The first algorithm (alled 'gray') transfers a color image to a gray-scale image and adds the values of pixels. The values obtained during such procedure are plotted as a function of temperature. The next algorithm (called 'rgb') divides color image to three images in shades of red, blue and green. Then, the values of pixels are added for the each image separately and plotted in a function of temperature. The last one algorithm (called 'svd') uses singular value decomposition (SVD) of the image. The first element in the diagonal matrix is taken and plotted in a function of temperature, as a results of SVD analysis.
The software can be used either as a standalone application or as a Python module that can be called from other scripts. The software is free for non-profit academic research, but it requires an agreement for commercial use.  

1.1 How to quote the use of TOApy
---------------------------------
In case the use of TOApy contributed to a published research, we would be thankful if the following paper was properly cited:

*N. Osiecka, Z. Galewski, M. Massalska-Arodź; "TOApy - program for the thermooptical analysis of phase transitions" submitted*.

2. Installation
===============

2.1 Software requirements
-------------------------
TOApy has been written in Python programming language. Therefore to use the software, you must have Python 3.4 or Python 3.5 installed. In addition, the following third-party Python libraries are also required:

- NumPy - library for scientific computing with Python
- OpenCV 3 - open source computer vision library
- matplotlib - Python ploting library
- Scipy - library for scientific computing with Python
- csv - library for csv file

Standard Python 3 releases can be obtained from https://www.python.org/downloads/. The third-party libraries can be found using any Internet search engine or at the Python Package Index.

However, a more convenient option is to obtain a science-oriented Python distribution e.g., Anaconda Python. This distribution already includes almost all necessary libraries, without OpenCV. Information how to download and install OpenCV can be found here http://opencv.org/downloads.html.

To check if all necessary libraries are installed please run testModules.py. Refer to the corresponding chapter in the Quick-start guide for a detailed instruction on how to run testModules.py.

2.2 TOApy installation
----------------------

The source code of TOApy can be downloaded from Github repository https://github.com/NataliaOsiecka/TOApy. This software can be downloaded as a zip file or cloned.

To download TOApy module push the green "Clone or download" button. Then push "Download ZIP" button.

To clone this git repository push the green "Clone or download" button. Select the copy icon near the https://github.com/NataliaOsiecka/TOApy.git url address. After selecting this icon "Copy to clipboard" message should show up. Push the icon. The "Copied!" message should show up. Using the UNIX shell or git bash go to the directory for TOApy, then type on console:

```
git clone https://github.com/NataliaOsiecka/TOApy.git
```

For more information on how to use git repositories or UNIX shell see Software Carpentry lessons "Version Control with Git" http://swcarpentry.github.io/git-novice/ and "The Unix Shell" http://swcarpentry.github.io/shell-novice/.

3. Quick-start guide
====================

This guide assumes that the TOApy program has been correctly installed, along with all necessary third-party libraries. To do this, open the command-line console in the directory where testModules.py file resides, and if you use Windows operation system type:

```
python testModules.py
```

and if you use UNIX operation system type:

```
python3 testModules.py
```

The output will inform you if all necessary third-party library were installed correctly.

TOApy is a command-line application that awaits all its input as command-line arguments. In general, the TOApy is executed from a command shell (in case computers with Windows operation system) as:

```
python toa.py arg1 arg2 arg3 arg4 arg5 
```

where:
arg1 - file name of the movie to be analysed,
arg2 - starting temperature [C],
arg3 - cooling/heating rate [C/min],
arg4 - [c/h]: direction of the temperature change: c for cooling, or h for heating,
arg5 - [-gray / -svd / -rgb]: selects the desired algorithm for thermooptical analysis.

Example: To perform TOA analysis using computer witha UNIX operation system and the '-gray' method of the '5BBAA_c120_10.avi' movie, which was recorded during cooling with the rate of 10C/min starting from 120C, open the command ilne interface in the directory where TAOpy software resides, and type:

```
python3 toa.py 5BBAA_c120_10.avi 120.0 10.0 c -gray
```

The '5BBAA_c120_10.avi' movie should be in the same directory as TOApy.

If successful, a movie player window should pop up with '5BBAA_c120_10.avi'. Press the 's' key on keyboard to capture the frame you like. The image will be saved in the same directory as 'ImageXY.png', where XY is the temperature in Celsius. When the application is running the time and temperature of POM observation is displayed on the command-line interface.

Press the 'q' key on keyboard to quit the apllication or wait till the end of the movie. The TOA plot will appear on screen and the corresponding csv data will be saved in the same directory.

