---
title: TOApy Documentation
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

TOApy is a simple but powerful program for thermoopltical analysis of movie obtained during 
polarized microscope observation. 

1.1 Reference
-------------
If you use this program for a scientific research that leads to publication, we ask that you acknowledge use of the program by citing the following paper in your publication:

2. Installation
===============

2.1 Software requirements
-------------------------
TOApy has been written in Python programming language, therefore to use the software, you must have Python 3.4 or Python 3.5 installed. In addition, the following third-party Python libraries are also required:

- NumPy - library for scientific computing with Python
- OpenCV 3 - open source computer vision library
- matplotlib - Python ploting library
- Scipy - library for scientific computing with Python
- csv - library for csv file

Standard Python 3 relases can be obtain from https://www.python.org/downloads/. The third-party libraries can be found uisng nay Internet search engine or at the Python Package Index.

However more convenient option is to obtain science-oriented Python distribution i.e. Anaconda Python. These distribution already include almost all necessary libraries, without OpenCV. Information abut installing and downland OpenCV can be found from http://opencv.org/downloads.html.

To check if all necessary librarys are installed please run testModules.py. Detailed description how to run testModules.py is described in Quic-start guide chapter.

2.2 TOApy installation
----------------------

The source code of TOApy can be downlanded from Github repository https://github.com/NataliaOsiecka/TOApy. This software can be downlanded as a zip file or cloning.

To downland TOApy module push the green "Clone or downland" button. Than push "Download ZIP" button.

To clone this git repository push the green "Clone or downland" button. Select the copy icon near the https://github.com/NataliaOsiecka/TOApy.git url address. After selecting this icon "Copy to clipboard" messeage shuld show up. Push the icon. The "Copied!" message should show up. Using the unix shell or git bash go to the directory for TOApy, then write on console:

git clone https://github.com/NataliaOsiecka/TOApy.git

For more information how to use git repositories or unix shell see Software Carpentry lessons "Version Control with Git" http://swcarpentry.github.io/git-novice/ and "The Unix Shell" http://swcarpentry.github.io/shell-novice/.

3. Quick-start guide
====================
This guide assumes that the TOApy program has been correctly installed and all nesecary third-party library also. Run testModules.py to check the third-party library installation.

The TOApy program is a command-line application, therefore all the input files are supplied as command-line arguments. In general, the TOApy is executed from a command shell as:

python3 toa.py input1 input2 input3 input4 input5 



