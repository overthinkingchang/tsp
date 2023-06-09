# -*- coding: utf-8 -*-
"""FinalProjectCode.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cW12PA7clmoTUygOsq_cN11EriOyQB1J
"""

import itertools
import csv
import io
import sys
import math
import pandas as pd
import tkintermapview
#from google.colab import files
import tkinter as tk
#import matplotlib.pyplot as plt
#import networkx as nx

# Upload data
#uploaded = files.upload()
distances = pd.read_csv('Database.csv', index_col=0)
distances.head()

def tsp(adjacency_df, start_point):
    points = list(adjacency_df.columns)
    num_points = len(points)
    unvisited_points = points.copy()
    unvisited_points.remove(start_point)
    current_point = start_point
    cycle_length = 0
    cycle = [start_point]

    while unvisited_points:
        next_point = None
        min_distance = float('inf')

        for point in unvisited_points:
            distance = adjacency_df.loc[current_point, point]

            if distance < min_distance:
                min_distance = distance
                next_point = point

        cycle_length += min_distance
        cycle.append(next_point)
        unvisited_points.remove(next_point)
        current_point = next_point
    cycle_length += adjacency_df.loc[current_point, start_point]
    cycle.append(start_point)

    return cycle_length, cycle




    #for node in distances.columns:
    #visiting_nodes, cycle_length = tsp(distances, node)
    #print("Visiting Nodes:", visiting_nodes)
    #print("Cycle Length:", cycle_length)

#adr = tkintermapview.convert_coordinates_to_address(51.5122057, -0.0994014)
#print(adr.street, adr.housenumber)