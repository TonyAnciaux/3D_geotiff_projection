#!~/.conda/envs/3D_houses/bin/python
import numpy as np
from pathlib import Path
import geopy
from geopy.geocoders import Nominatim
import plotly.graph_objects as go
from pyproj import Transformer
import rasterio
from rasterio.windows import Window


def plot_house():
    """
    Asks the user for the address of the house and send the input to address_to_crs function
    """
    address: str = input("Please, insert your address here: ")
    address_to_crs(address)


def address_to_crs(address: str):
    """
    Converts input address to geographical coordinates then to Lambert projections (CRS)
    """
    geopy.geocoders.ArcGIS()
    geolocator = Nominatim(user_agent="ArcGIS")
    location = geolocator.geocode(f"{address}")
    latitude = location.latitude
    longitude = location.longitude
    transformer = Transformer.from_crs("EPSG:4326", crs_to="EPSG:31370", always_xy=False)
    x, y = transformer.transform(latitude, longitude)
    tiff_finder(x, y)


def tiff_finder(x: float, y: float):
    """
    Finds the two GeoTiff files (DSM and DTM) matching the x and y projections
    then plots the area around the central point (200m2)
    """
    paths = Path("./Data").glob("**/*.tif")
    loc = np.zeros((200, 200))
    for path in paths:
        with rasterio.open(path) as fd:
            if fd.bounds.left <= x <= fd.bounds.right:
                if fd.bounds.bottom <= y <= fd.bounds.top:
                    radius = 100
                    left, bottom, right, top = (
                        x - radius,
                        y - radius,
                        x + radius,
                        y + radius,
                    )
                    crop = fd.read(
                        1,
                        window=rasterio.windows.from_bounds(
                            left, bottom, right, top, fd.transform
                        ),
                    )
                    loc += crop
    fig = go.Figure(data=[go.Surface(z=loc)])
    fig.update_scenes(yaxis_autorange="reversed")
    fig.show()


plot_house()
