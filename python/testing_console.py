import requests
import json

SDK_KEY = '5c12448f49cbf6787adb4e3babaff16dfd678b6b91c8a8518cb9d66f4e359f59'
LAUNCH_URL = 'https://api.singular.net/api/event_logger/device'


def register_device(device_id, id_type = 'AIFA'):
    url = f'https://api.singular.net/api/event_logger/device?api_key={SDK_KEY}'

    return requests.post(url, {
        "api_key": SDK_KEY,
        "device_id": device_id,
        "keyspace": id_type,
        "platform": "Android"
    }).json()

params = {
    'api_key': SDK_KEY,
    'keyspace': 'AIFA',
    'device_id': '4012358e-69e6-49a8-a3f3-57b743751cb8',
    'platform': 'Android',
}

# result = requests.get(LAUNCH_URL, params=params)
print(register_device('4012358e-69e6-49a8-a3f3-57b743751cb8'))