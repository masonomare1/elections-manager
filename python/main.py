import requests
import json

SDK_KEY = 'devsinc_554aa21b'
LAUNCH_URL = 'https://s2s.singular.net/api/v1/launch'

referrer_values = {
    "referrer": "tracking_id%3D123456789&utm_source%3Dmdotm%26utm_medium%3Dbanner%26utm_campaign%3Dcampaign",
    "referrer_source" : "service",
    "clickTimestampSeconds" : 1550420123,
    "installBeginTimestampSeconds" : 1550420123,
    "current_device_time" : 1550420454906
    }

referrer_values = json.dumps(referrer_values, separators=(',',':'))



params = {
    'a': SDK_KEY,
    'p': 'Android',
    'i': 'com.singular.app',
    'ip': '10.1.2.3',
    've': '9.2',
    'ma': 'samsung',
    'mo': 'SM-G935F',
    'lc': 'en_US',
    'aifa': '4012358e-69e6-49a8-a3f3-57b743751cb8',
    'asid': '6f8375c3-a326-b31f-e19a-d691af54012b',
    'andi': 'fc8d449516de0dfb',
    'utime': 1483228800,
    'dnt': 1,
    'install': 'true',
    'n': 'Go Go Magnet!',
    'c': 'wifi',
    'cn': 'Comcast',
    'bd': 'Build/13D15',
    'fcm':'bk3RNwTe3H0CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1',
    'app_v':'1.2.3',
    'openuri':'myapp%3A%2F%2Fhome%2Fpage%3Fqueryparam1%3Dvalue1',
    'install_source': 'com.android.vending',
    'install_time': 1510040127,
    'update_time': 1510090877,
    'custom_user_id': 'player_id_1234',
    'install_ref': referrer_values
}

result = requests.get(LAUNCH_URL, params=params)
print(result.json())
