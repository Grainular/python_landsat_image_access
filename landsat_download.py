from landsatxplore.api import API
from landsatxplore.earthexplorer import EarthExplorer
import os

# # Your Earth Explorer credentials
# username = 'farmlink'
# password = 'farmlink123!!'

# # Connect to the API
# api = API(username, password)

# # Define your search parameters: Landsat 8, Path/Row values, date range
# landsat_mission = 'landsat_ot_c2_l1'
# latitude = 45.0   # Example latitude (Los Angeles)
# longitude = -63.0 # Example longitude (Los Angeles)
# start_date = '2022-01-01'
# end_date = '2022-12-31'

# # Search for available scenes
# scenes = api.search(
#     dataset=landsat_mission,
#     latitude=latitude,
#     longitude=longitude,
#     start_date=start_date,
#     end_date=end_date,
#     max_cloud_cover=10,
# )

# # Print the results
# for scene in scenes:
#     ee = EarthExplorer(username, password)
#     print(scene['entity_id'])
#     ee.download(scene['entity_id'], output_dir='.')

# # Close the API session
# api.logout()

def download_landsat_data(latitude, longitude, start_date, end_date, max_cloud_cover=10):
    # Your Earth Explorer credentials (ensure these are secured, e.g., using environment variables)
    username = os.getenv('EARTH_EXPLORER_USERNAME')
    password = os.getenv('EARTH_EXPLORER_PASSWORD')

    # Connect to the API
    api = API(username, password)

    # Define your search parameters: Landsat 8, Path/Row values, date range
    landsat_mission = 'landsat_ot_c2_l1'

    try:
        # Search for available scenes
        scenes = api.search(
            dataset=landsat_mission,
            latitude=latitude,
            longitude=longitude,
            start_date=start_date,
            end_date=end_date,
            max_cloud_cover=max_cloud_cover,
        )

        ee = EarthExplorer(username, password)
        downloaded_scenes = []

        for scene in scenes:
            entity_id = scene['entity_id']
            print(f"Downloading scene: {entity_id}")
            ee.download(scene['entity_id'], output_dir='downloads/')
            downloaded_scenes.append(entity_id)

    except Exception as e:
        print(f"Error during download: {e}")
        downloaded_scenes = []

    finally:
        # Close the API session
        api.logout()
        ee.logout()

    return downloaded_scenes

if __name__ == "__main__":
    scenes_downloaded = download_landsat_data(45.0, -63.0, '2022-01-01', '2022-12-31')
    print(scenes_downloaded)