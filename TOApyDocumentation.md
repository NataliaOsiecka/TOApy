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

TOApy is a simple, but powerful program for thermoopltical analysis of movie obtained during polarized microscope observation. TOApy has been designed for easy of use, speed and automated operation. The main advance of TOApy software is decreased number of equipments for the termooptic analysis for which it can be applied. TOApy requires few inputs and not much of user experience, so it can be quickly adopted by novice users. The live-watching interactive feature allows the user to capture the microscopic image of the analyzed phase. To obtain thermooptical analysis plot three different algorithms are used in TOApy program.  The software can be used either as a standalone application or as a Python module that can be called from other scripts. For open academic research the software is free, but it requires agreement for commercial use.  

1.1 Reference
-------------
If you use this program for a scientific research that leads to publication, we ask you to acknowledge citing in your publication the following paper:

*N. Osiecka, Z. Galewski, M. Massalska-Arodź; "TOApy - program for the thermooptical analysis of phase transitions" in press*.

2. Installation
===============

2.1 Software requirements
-------------------------
TOApy has been written in Python3 programming language. Therefore to use the software, you must have Python 3.4 or Python 3.5 installed. In addition, the following third-party Python libraries are also required:

- NumPy - library for scientific computing with Python
- OpenCV 3 - open source computer vision library
- matplotlib - Python ploting library
- Scipy - library for scientific computing with Python
- csv - library for csv file

Standard Python 3 relases can be obtained from https://www.python.org/downloads/. The third-party libraries can be found using any Internet search engine or at the Python Package Index.

However more convenient option is to obtain science-oriented Python distribution i.e., Anaconda Python. This distribution includes already almost all necessary libraries, without OpenCV. Information abut installing and download OpenCV can be found from http://opencv.org/downloads.html.

To check if all necessary libraries are installed please run testModules.py. Detailed description how to run testModules.py is described in Quic-start guide chapter.

2.2 TOApy installation
----------------------

The source code of TOApy can be downloaded from Github repository https://github.com/NataliaOsiecka/TOApy. This software can be downloaded as a zip file or cloning.

To download TOApy module push the green "Clone or download" button. Than push "Download ZIP" button.

To clone this git repository push the green "Clone or download" button. Select the copy icon near the https://github.com/NataliaOsiecka/TOApy.git url address. After selecting this icon "Copy to clipboard" message should show up. Push the icon. The "Copied!" message should show up. Using the UNIX shell or git bash go to the directory for TOApy, then write on console:

```
git clone https://github.com/NataliaOsiecka/TOApy.git
```

For more information how to use git repositories or UNIX shell see Software Carpentry lessons "Version Control with Git" http://swcarpentry.github.io/git-novice/ and "The Unix Shell" http://swcarpentry.github.io/shell-novice/.

3. Quick-start guide
====================

This guide assumes that the TOApy program has been correctly installed and all necessary third-party library as well. Run testModules.py in command-line interface to check the third-party library installation. In order to hange directory to the directory where 'testModules.py' is, 'cd' command have to be used. Write in command line:

```
python testModules.py
```

The output will inform you if all necessary third-party library were installed correctly.

The TOApy program is a command-line application. Therefore, all the input files are supplied as command-line arguments. In general, the TOApy is executed from a command shell as:

```
python3 toa.py input1 input2 input3 input4 input5 
```

The input1 stands for the name of movie. Input2 is the value of starting temperature. Input3 corresponds to the cooling/heating rate of temperature changes. Input4 informs about the mode of observation, c stands for cooling mode and h for heating mode. Input5 should be replaced by one of the following variable --gray, --svd, --rgb, which corresponds to the adopted algorithm for the thermooptical analysis.

To perform TOA analysis using 'gray' method of '5BBAA_c120_10.avi' movie, which were obtained with cooling rate 10C/min starting from 120C, change the directory where TAOpy software is and write the following line in command-line interface:

```
python3 toa.py 5BBAA_c120_10.avi 120.0 10.0 c --gray
```

The '5BBAA_c120_10.avi' movie should be in the same directory as TOApy software is.

After that command a movie of '5BBAA_c120_10.avi' should appear on a screen. Press 's' key on keyboard to capture observed image. The image will be saved in the same directory were TOApy software is as an 'ImageXY.png', where XY is the temperature in Celsius degrees. When the application is running the time and temperature of POM observation is displayed on the command-line interface.

Press 'q' key on keyboard to quit the apllication or wait on the end of the movie. The TOA plot will appear on a screen while csv file with data will arrive in the directory where the TOApy software is presented.

