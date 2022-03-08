# 3D House Project

## Description

Consolidation of Python knowledge through a 3D plotting exercise. 

### The mission 

*We are LIDAR PLANES, active in the Geospatial industry. 
We would like to use our data to launch a new branch in the insurance business. 
So, we need you to build a solution with our data to model a house in 3D with only a home address.*

### Files included

- **Data_Exploring.ipynb**: Jupyter Notebook with Data exploration, thought process and 
developpment of final codes. 
- **3D_project_presentation**: Keynote file with the final presentation to the customer
- **main.py**: *on-going* GUI project 
- **location.py**: *on-going* OOP associated with main.py 
- **3D_houses.py**: functioning program to be launched from Terminal 

## Installation

The data must be downloaded from:
 - http://www.geopunt.be/download?container=dhm-vlaanderen-ii-dsm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DSM,%20raster,%201m
 - http://www.geopunt.be/download?container=dhm-vlaanderen-ii-dsm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DSM,%20raster,%201m

Then installed in a folder named "./Data"

This program will require your computer to have python 3.9 and all the following dependencies:
- Numpy 
- geopy 
- plotly
- pyproj 
- rasterio 


## Usage

To launch the program, open your terminal and be sure to be in the folder where the *3D_houses.py* file is.

Type *"python3 3D_houses.py"*. A prompt will ask you to input an address. 
It's preferable to insert a flemish address for area located in Flanders. 
Brussels region will take English and french typing without issues. 


