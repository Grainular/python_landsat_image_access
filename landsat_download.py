from landsatxplore.api import API
from landsatxplore.earthexplorer import EarthExplorer

# Your Earth Explorer credentials
username = 'farmlink'
password = 'farmlink123!!'

# Connect to the API
api = API(username, password)

# Define your search parameters: Landsat 8, Path/Row values, date range
landsat_mission = 'LANDSAT_ETM_C1'
latitude = 34.05   # Example latitude (Los Angeles)
longitude = -118.25 # Example longitude (Los Angeles)
start_date = '2022-01-01'
end_date = '2022-12-31'

# Search for available scenes
scenes = api.search(
    dataset=landsat_mission,
    latitude=latitude,
    longitude=longitude,
    start_date=start_date,
    end_date=end_date,
    max_cloud_cover=10,
)

# Print the results
for scene in scenes:
    print(f"ID: {scene['entityId']}, Acquisition Date: {scene['acquisitionDate']}, Cloud Cover: {scene['cloudCover']}")

# Close the API session
api.logout()
