import folium

# Generate map at coordinates for New Delhi
m = folium.Map(location=[28.61, 77.23], zoom_start=5)
folium.Marker([28.61, 77.23], popup="New Delhi").add_to(m)

m.save("7_map.html")
# Optional: display the map object inline if running in an interactive notebook environment
m