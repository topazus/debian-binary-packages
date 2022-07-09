import json
import os
from unittest import skip
import packaging.version
import requests

repo='gcc-mirror/gcc'
url=f'https://api.github.com/repos/{repo}/tags'
response=requests.get(url=url)
api_json=response.json()
name=repo.split('/')[1]
with open(f'{name}-tags.json','w') as f:
    json.dump(obj=api_json,fp=f,indent=4)


url=f'https://api.github.com/repos/{repo}/releases/latest'
response=requests.get(url=url)
api_json=response.json()
name=repo.split('/')[1]
with open(f'{name}-releases.json','w') as f:
    json.dump(obj=api_json,fp=f,indent=4)
# os.mkdir('')


repo='numpy/numpy'
url=f'https://api.github.com/repos/{repo}/releases/latest'
response=requests.get(url=url)
api_json=response.json()
name=repo.split('/')[1]
with open(f'{name}-releases.json','w') as f:
    json.dump(obj=api_json,fp=f,indent=4)

url=f'https://api.github.com/repos/{repo}/tags'
response=requests.get(url=url)
api_json=response.json()
print(len(api_json))

version_ls=[]
for x in api_json:
    version_str=x['tag_name']
    try:
        version=packaging.version.parse(version_str)
        if version.is_prerelease:
            skip
        version_ls.append(version)
    finally:
        skip

    
name=repo.split('/')[1]
with open(f'{name}-tags.json','w') as f:
    json.dump(obj=api_json,fp=f,indent=4)