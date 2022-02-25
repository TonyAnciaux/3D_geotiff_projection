import numpy as np
from pathlib import Path
import plotly
import plotly.graph_objects as go
import geopy
from geopy.geocoders import Nominatim
from pyproj import Proj, transform
import rasterio
from rasterio.plot import show
from rasterio.windows import Window
from tkinter import *


def address_to_location(place):
    geopy.geocoders.ArcGIS()
    geolocator = Nominatim(user_agent="ArcGIS")
    location = geolocator.geocode(f"{place}")
    latitude = location.latitude
    longitude = location.longitude

    inproj = Proj('epsg:4326')
    outproj = Proj('epsg:31370')
    x, y = transform(inproj, outproj, latitude, longitude)
    # to make coordinates appear on the window object
    main_text.config(text=f"Lambert coordinates:\n{x}, {y}")

    paths = Path("Data").glob("**/*.tif")
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
                fig.show()


# Instantiating the window object of the application
root = Tk()
root.title("3D Houses")


# Defining input and label for users
main_text = Label(root, text="", anchor="center")
address = StringVar(root, value="Type your address here")
entry = Entry(root, width=50, textvariable=address)


# Defining buttons and their functions
button_3Dplot = Button(root, text="3D House", padx=60, anchor="center",
                       command=lambda: address_to_location(entry.get()))
button_map = Button(root, text="Map", padx=70, anchor="center")
button_exit = Button(root, text="X", command=root.destroy)


# Placing the buttons in the frame (grid-relative system)
button_3Dplot.grid(row=2, column=0, columnspan=2, padx=25, pady=20)
button_map.grid(row=2, column=2, columnspan=2, padx=25, pady=20)
button_exit.grid(row=0, column=3, pady=35)


# Placing input and label for users on the screen (grid)
main_text.grid(row=0, column=0, columnspan=4, padx=25)
entry.grid(row=1, column=0, columnspan=4, padx=25)


# This "event loop" will update the GUI according to program changes and user's inputs.
# It *must* stay at the end of the code.
root.mainloop()
