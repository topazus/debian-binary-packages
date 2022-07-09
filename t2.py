import json
from pprint import pprint
import requests

repo='numpy/numpy'
url=f'https://api.github.com/repos/{repo}/releases/latest'
response=requests.get(url=url)
api_json=response.json()
