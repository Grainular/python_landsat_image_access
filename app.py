# python_landsat_image_access/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from landsat_lat_long_to_path_row import get_next_pass
from landsat_download import download_landsat_data

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes (configure as needed for security)

# Endpoint to get Landsat pass information
@app.route('/api/get-landsat-pass', methods=['POST'])
def get_landsat_pass():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    print("lat: ",latitude)
    if latitude is None or longitude is None:
        return jsonify({'error': 'Latitude and Longitude are required.'}), 400

    try:
        pass_info = get_next_pass(lat=latitude, long=longitude)
        return jsonify(pass_info), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to download Landsat data
@app.route('/api/download-landsat', methods=['POST'])
def download_landsat():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    max_cloud_cover = data.get('max_cloud_cover', 10)

    if not all([latitude, longitude, start_date, end_date]):
        return jsonify({'error': 'Latitude, Longitude, Start Date, and End Date are required.'}), 400

    try:
        downloaded_scenes = download_landsat_data(
            latitude=latitude,
            longitude=longitude,
            start_date=start_date,
            end_date=end_date,
            max_cloud_cover=max_cloud_cover
        )
        return jsonify({'downloaded_scenes': downloaded_scenes}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
