# Logbook
-----------

## Intro

### What?

- App that shows 3D houses from address input 


### Why? 

- Insurance Company


### How? 

#### Research

- Terms, concepts and objectives of the mission
- Libraries: 
	- PyShp (Shapefile)
	- VTK (Vizualisation Toolkit)
	- PyVista (3D Plotting)
	- Geopy (adresses to coordinates)
	- GeoPandas (coordinates to CRS)
	- ArcGIS (API for coordinates)
	- Folium (Addresses to MAP)
	- Rasterio (GeoTIFF files)
	- PyProj (conversion?)
	- plotly(3D plotting)	


#### Data

- Find data for all adresses/cadastral plans in Flanders (data.gov.be)
- Merge & clean data to csv? DataFrame?


#### Python 

- Function that returns coordinates from addresses (Geopy + ArcGIS)
- Function that locates the coordinates on a map (Folium?)
- Function that matches the coordinates with right Shapefiles from DSM/DTM and Cadastral (PyShp?)
- Function that finds the matching TIFF file (Rasterio?)
- Function that plots the 3D-Home model (VTK/PyVista?)


#### BAG OF IDEAS:
- find how to use the DSM Shapefile coordinates
- convert adresses into coordinates (Geopy + ArcGIS)
- match the coordinates with Lidar data
- use the Lidar Data to model 3D houses (Library?)

- deduce features (area, square meters, pool, garden, floors, etc.):
	- more research required 

- find a way to optimize the speed and memory use (cropping)
- Develop a user-friendly GUI (TKinter?)




## Logs

#### 17.02.2022:
- repository & logbook creation
- DSM & DTM data download
- plan of actions to take + *"Bag of Ideas"*
- research:
	- terms (Shapefile, GeoTIFF, Lidar)
	- libraries overview:
		- PyShp
		- PyVista (+ VTK: Vizualisation Toolkit)
		- Geopy
- Belgium cadastral plan data (from data.gov.be)
- documentation translation
- Flowchart creation 

		
#### 18.02.2022:
- set up libraries:
	- PyShp
	- Rasterio
	- GeoPy
	- ArcGIS
	- GeoPandas
- exploratory researches:
	- opened some DSM files to see how it looks and how to proceed
	- CRS (Coordinate Reference System)
	- opened some TIFF files for same purpose
	- mostly reseach to get a grip at the libraries
	- tried some dummy queries address through GeoPy/ArcGIS API


#### 21.02.2022:
- set up libraries:
	- GDAL
	- Pyproj
- function to convert user input into coordinates
- function to convert coordinates into CRS projections
- figured out a function that finds the good .tif file


#### 22.02.2022:

- set up libraries:
	- VTK (for nothing)
	- PyVista (for nothing)
	- + ipyvtklink (for nothing)
	- plotly
- started refarctoring the code in PyCharm:
	- lost a lot of time setting *venv* for RasterIO issues - still doesn't work	
- found a way to locate and crop the tif file in one function
- plotted my first 3D buildings (two: one for each file)
- merged the two matching .tif files and plotted in one 3D file


#### 23.02.2022:

- started GUI with Tkinter
- tried to solve PyCharm environment (should I switch library??!!)
- tried to implement a shape_finder function to find the property *polygon*


#### 24.02.2022:

- working with Geopandas and Shapely for the **shape_finder** function
- Turns out it's best directly with Fiona and Rasterio?! 


#### 25.02.2022:

- still trying to find a way to crop the tiff file with the shapefile 
	while combining the 2 tiff files in one.
	Have yet to find a solution for this or I'll just give up. 
- solved the rasterio troubles in PyCharm
- managed to make a function pass an entry.get() as argument 
- discovered Plotly is not compatible with Tkinter... 
	- embed Dash module? WTH?? 
	- Matplotlib?


#### TODO:
- TKinter GUI:
	- find nice icons 
	- color theme
- find the matching property:
	- can I extract more features?? (area, floors, swimming pools, etc?)
- plot the address on a regular map (Folium?)
