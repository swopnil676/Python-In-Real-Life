import folium
from geopy.geocoders import Nominatim
import webbrowser

location_name = input("Enter a location: ")

geolocator = Nominatim(user_agent="geoapi")
location = geolocator.geocode(location_name)

if location:
    latitude = location.latitude
    longitude = location.longitude

    my_map = folium.Map(
        location=[latitude, longitude],
        zoom_start=12
    )

    folium.Marker(
        [latitude, longitude],
        popup=location_name
    ).add_to(my_map)

    my_map.save("map.html")

    webbrowser.open("map.html")

    print("Map opened successfully!")

else:
    print("Location not found.")