import json
import requests

url_list = 'https://api.fanbox.cc/creator.listFollowing'

hd = {
    "fanbox请求headers"
    }
response = requests.get(url_list, headers=hd)

data_dict = response.json()

creator_ids = []
for item in data_dict['body']:
    creator_ids.append(item['creatorId'])

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump({'creatorIds': creator_ids}, f, ensure_ascii=False, indent=4)

print('执行成功')
