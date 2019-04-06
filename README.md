This is our CprE 186 project.

It is by Rolf, Ritz, William, and Alexis.

We designed a digital screen with computer vision to identify targets and show where the user should point the gun.  It also has motorized iron sights to assist.

Copyright 2019.

This software is for a raspberry pi running raspian stretch

Dependencies:
   
   Python version: 2.7
      Packages required:

		build-essential 
   		cmake 
   		pkg-config
   		libjpeg-dev 
   		libtiff5-dev 
   		libjasper-dev 
   		libpng12-dev
   		libavcodec-dev 
   		libavformat-dev 
   		libswscale-dev
   		libv4l-dev
   		libxvidcore-dev 
   		libx264-dev
        libatlas-base-dev
        gfortran
        python-3 (for header files)
        
        
        
Step 1: Install dependencies      
  
  Install dependencies and python using apt.
  You can either use sudo or have a superuser shell.
   
  $ sudo apt install python2.7 python2.7-dev build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
                   libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libgtk2.0-dev libgtk-3-dev
                   libatlas-base-dev gfortran python3-dev
                   
Step 2: Download OpenCV source code

  Be sure to be in your home directory.
  
  Download and unzip source code for opencv3.
  
  $ wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.0.zip
  $ unzip opencv.zip
  
  For extra credits, download the opencv_contrib repo and unzip.
  
  $ wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.0.zip
  $ unzip opencv_contrib.zip
  
  Additionally, get pip - the python package manager.
  
  $ wget https://bootstrap.pypa.io/get-pip.py
  $ sudo python get-pip.py
  
  Get virtualenv for your python environment.
  
  $ sudo pip install virtualenv virtualenvwrapper
  $ sudo rm -rf ~/.cache/pip
  
  Update ~/.profile
  
  $ nano ~/.profile
  
  # ~/.profile
  export WORKON_HOME=$HOME/.virtualenvs
  export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2.7
  source /usr/local/bin/virtualenvwrapper.sh
  
  Now load this ~/.profile.
  
  $ source ~/.profile
  
  
  
        
             
