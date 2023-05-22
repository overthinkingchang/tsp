import gmaps
from datetime import datetime
import finalprojectcode
import pandas as pd
import matplotlib.pyplot as plt

apikey = "AIzaSyByn24_1Q4NxLWHcIJvvktLB1F986Wg07U"

distances = pd.read_csv('Database.csv', index_col=0)

uni_dict = {
    "Basketball Yard": (10.720617879404582, 106.72913106652106),
    "Fulbright University Vietnam": (10.726891209799389, 106.72027573768574),
    "Docklands Residence": (10.735724151495258, 106.72676033768579),
    "Starlight Bridge": (10.72498302509042, 106.7184931646735),
    "Big C": (10.741424479463072, 106.72544430258864),
    "Bamos 24h Coffee": (10.736087297489892, 106.70613345302723),
    "The Waterfront Residence":(10.725373676251985, 106.72457028186257),
    "Chicken Plus":(10.739337966986922, 106.70951286836876),
    "Soccer Yard": (10.740716666071622, 106.7313046800152),
    "Swimming Pool": (10.732173507032183, 106.71621098001502),
    "Nguyen Van Cu Bookstore": (10.739513125948669, 106.73008188186265),
    "Crescent Mall":(10.728899726166452, 106.7193049376858)
}

start = uni_dict["Basketball Yard"] #this is our start address
end = uni_dict["Basketball Yard"] #my start address is same as end address

visiting_nodes, cycle_length = finalprojectcode.tsp(distances, "Basketball Yard")
backnode = len(cycle_length)-1
cycle_waypoints = cycle_length[1:backnode:1]
waypoints = []
#the addresses my route has to move through
for i in cycle_waypoints:
    waypoints.append(uni_dict[i])

#configure api
gmaps.configure(api_key=apikey)


#Create the map
fig = gmaps.figure()
#create the layer
layer = gmaps.directions.Directions(start, end,waypoints = waypoints,optimize_waypoints=True,
                                    mode='car',api_key=apikey,departure_time = datetime.now())
#Add the layer
fig.add_layer(layer)
fig.add_layer(gmaps.traffic_layer())
print(fig)
