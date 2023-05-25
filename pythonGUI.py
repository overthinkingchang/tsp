import tkinter as tk
from tkinter import *
import folium
import geocoder
from tkinter import ttk
import tkinter_map as tmap
from IPython.display import display
import webbrowser


''' This program can only geocode cities in the United States

    Makes a HTML document in the same directory as this script 

'''
def makemap():
    output_file = 'fig.html'
    begin_place = variable.get()
    tmap.fig(begin_place).save(output_file)
    webbrowser.open(output_file, new=2) 

place = ["Basketball Yard",
        "Fulbright University Vietnam",
        "Docklands Residence",
        "Starlight Bridge",
        "Big C",
        "Bamos 24h Coffee",
        "The Waterfront Residence",
        "Chicken Plus",
        "Soccer Yard",
        "Swimming Pool",
        "Nguyen Van Cu Bookstore",
        "Crescent Mall"]

master = Tk()
master.geometry("500x500") #You want the size of the app to be 500x500

variable = StringVar(master)
variable.set(place[0]) # default value

w = OptionMenu(master, variable, *place)
w.grid(column=250, row = 250)

tk.Button(master, text='Generate', command=makemap).grid(column = 250, row=251, sticky='W')

#
# test stuff
master.mainloop()