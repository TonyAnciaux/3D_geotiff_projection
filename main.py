from tkinter import *
from location import Location


# Instantiating the window object of the application
root = Tk()
root.title("3D Houses")


# Defining input and label for users
main_text = Label(root, text="Your address", anchor="center")
entry = Entry(root, width=50)


# Defining buttons and their functions
button_3Dplot = Button(root, text="3D House", padx=60, anchor="center")
                       # command=lambda: Location.address_to_crs(entry.get)
button_map = Button(root, text="Map", padx=70, anchor="center")
                    # command=lambda: Location.address_to_location(entry.get)
button_exit = Button(root, text="X", command=root.destroy)


# Placing the buttons in the frame (grid-relative system)
button_3Dplot.grid(row=2, column=0, columnspan=2, padx=25, pady=15)
button_map.grid(row=2, column=2, columnspan=2, padx=25, pady=15)
button_exit.grid(row=0, column=3, pady=35)


# Placing input and label for users on the screen (grid)
main_text.grid(row=0, column=0, columnspan=4, padx=25)
entry.grid(row=1, column=0, columnspan=4, padx=25)


# This "event loop" will update the GUI according to program changes and user's inputs.
# It *must* stay at the end of the code.
root.mainloop()
