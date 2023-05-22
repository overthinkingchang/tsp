import folium
import finalprojectcode 
import pandas as pd
from folium import plugins
import osmnx as ox
import networkx as nx
# Map method of folium return Map object
 
# Here we pass coordinates of Gfg
# and starting Zoom level = 12
my_map1 = folium.Map(location = [10.726891209799389, 106.72027573768574],
                                        zoom_start = 20 )
distances = pd.read_csv('Database.csv', index_col=0)
visiting_nodes, cycle_length = finalprojectcode.tsp(distances, "Basketball Yard")
uni_dict = {
    "Basketball Yard": [10.720617879404582, 106.72913106652106],
    "Fulbright University Vietnam": [10.726891209799389, 106.72027573768574],
    "Docklands Residence": [10.735724151495258, 106.72676033768579],
    "Starlight Bridge": [10.72498302509042, 106.7184931646735],
    "Big C": [10.741424479463072, 106.72544430258864],
    "Bamos 24h Coffee": [10.736087297489892, 106.70613345302723],
    "The Waterfront Residence":[10.725373676251985, 106.72457028186257],
    "Chicken Plus":[10.739337966986922, 106.70951286836876],
    "Soccer Yard": [10.740716666071622, 106.7313046800152],
    "Swimming Pool": [10.732173507032183, 106.71621098001502],
    "Nguyen Van Cu Bookstore": [10.739513125948669, 106.73008188186265],
    "Crescent Mall":[10.728899726166452, 106.7193049376858]
}
location_list = []
count = 0
backnode = len(cycle_length) - 1
cycle_length = cycle_length[:backnode]
for i in cycle_length:
    count +=1
    folium.Marker(uni_dict[i], popup = i, icon = plugins.BeautifyIcon(number=count, border_color='blue',
                                            border_width=1,
                                            text_color='red',
                                            inner_icon_style='margin-top:0px;',
                                            spin=True,
                                            )).add_to(my_map1)
    location_list.append((uni_dict[i][0],uni_dict[i][1]))
 
 
# Add a line to the map by using line method .
# it connect both coordinates by the line
# line_opacity implies intensity of the line
 
plugins.AntPath(locations = location_list,
                line_opacity = 0.5).add_to(my_map1)
 
my_map1.save(" my_map1.html " )