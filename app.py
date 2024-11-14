# Write the Streamlit app code to a file
app_code = """
import streamlit as st
import geopandas as gpd
import folium
from folium import raster_layers
import rasterio
from streamlit_folium import folium_static

# Set up map and data
st.title("Geospatial Visualization for Romania")
tiff_file = '/content/data/land_use_romania.tif'  # Correct path to your TIFF file

with rasterio.open(tiff_file) as src:
    image_data = src.read(1)  # Read the first band
    bounds = src.bounds

# Initialize Folium map
m = folium.Map(location=[45.0, 25.0], zoom_start=7)

# Add raster layer to map
raster_layers.ImageOverlay(
    image_data,
    bounds=[[bounds[1], bounds[0]], [bounds[3], bounds[2]]],
    opacity=0.7,
).add_to(m)

# Display the map
folium_static(m)
"""

# Save the code to a file
with open("/content/app.py", "w") as file:
    file.write(app_code)

