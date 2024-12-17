import requests
import yaml

def fetch_real_world_data():
    with open("config/settings.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    api_url = config["real_world_data_sources"][0]["url"]
    api_key = config["real_world_data_sources"][0]["api_key"]

    response = requests.get(api_url, params={"apiKey": api_key, "country": "us"})
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch real-world data.")
        return {}
