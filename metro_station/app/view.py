from app import app
from flask import request
import requests
import json

@app.route('/api/v1/metro/verificate/', methods=["POST"])
def sync_stations():
    try:
        data = set(request.get_json())
        full_json = requests.get('https://api.hh.ru/metro/1').json()
        base_stations = set()
        for lines in full_json['lines']:
            for station in lines['stations']:
                base_stations.add(station['name'])

        unchanged = data & base_stations
        updated = data - base_stations
        deleted = base_stations - data

        final_json = {"unchanged": list(unchanged),
                    "updated": list(updated),
                    "deleted": list(deleted)}
        response = app.response_class(
            response=json.dumps(final_json),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as ex:
        return app.response_class(
            response=str(ex),
            status=400,
        )


