# VERY HELPFUL FOLIUM DOCUMENTATION ::  https://python-visualization.github.io/folium/quickstart.html



#Import folium lib to use map objects
import folium
#import pandas to use dataframes
import pandas
#create a dataframe with volcano featurews
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"]) #extract latitude values of volcano
lon = list(data["LON"]) #extract longitude values of  volcano
elev = list(data["ELEV"]) #exract  elevation
#define a function to color code the volcanos according to elevation
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
#create a map object initialized to the mewntioned coordinates , zoom value is set at 6 , tiles extract the map from API (default is openstreetMap)
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright") #API used is MapBox Bright
#create a feature group which is a  group of all volcano markers

fgv = folium.FeatureGroup(name="Volcanoes")
#for loop used to acces lat , long, and elevation 
for lt, ln, el in zip(lat, lon, elev):
	#adding a circle marker and popup string concatenated with 'm' to increase readablity 
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m",
    fill_color=color_producer(el), fill=True,  color = 'grey', fill_opacity=0.7)) #color producer function is used to color code elevation+
#Colorcode the population , lamba function is used [choropleth is the word]
#create another feature group for population
fgp = folium.FeatureGroup(name="Population")
#create  another layer by geoJson to visulaize population 
#GeoJSON and TopoJSON layers can be passed to the map as an overlay, and multiple layers can be visualized on the same map
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'})) #lamda function to classify population 
#add feature groups as child to map object 

map.add_child(fgv)
map.add_child(fgp)
#Layer control used to render layers 
map.add_child(folium.LayerControl())
#create a html page 
map.save("Map1.html")
