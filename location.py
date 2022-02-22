import geopy
from typing import Tuple, Any
from geopy.geocoders import Nominatim
from pathlib import Path
from pyproj import Proj, transform
import rasterio
from rasterio.plot import show
from rasterio.windows import Window


class Location:

    def __init__(self):
        self.longitude = 0
        self.latitude = 0
        self.x = 0
        self.y = 0
        self.address = input("What is your address?\n")

    def address_to_location(self):
        geopy.geocoders.ArcGIS()
        geolocator = Nominatim(user_agent="ArcGIS")
        location = geolocator.geocode(f"{self.address}")
        self.latitude = location.latitude
        self.longitude = location.longitude
        self.location_to_crs(self.longitude, self.latitude)

    def location_to_crs(self, long: float, lat: float) -> Tuple[Any, Any]:
        self.longitude = long
        self.latitude = lat
        inproj = Proj('epsg:4326')
        outproj = Proj('epsg:31370')
        self.x, self.y = transform(inproj, outproj, self.longitude, self.latitude)
        return int(self.x), int(self.y)

    def tiff_finder(self):
        paths = Path("Data").glob("**/*.tif")
        for path in paths:
            with rasterio.open(path) as fd:
                if fd.bounds.left <= self.x <= fd.bounds.right:
                    if fd.bounds.bottom <= self.y <= fd.bounds.top:
                        crop = fd.read(1, window=Window(self.x, self.y, 100, 100))
                        return show(crop)
