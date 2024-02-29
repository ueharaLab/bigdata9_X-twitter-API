import json
import requests
import urllib.parse


# 検索条件
url = f'https://api.twitter.com/2/tweets/search/recent'
# 認証
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAH4RsgEAAAAAx2phEmbAQtdV6DCRAaItUM7VN7E%3D7YGZbqdfY7zCncPyUy1qjCIqK7yxvHVxjIc13d0JU8ATfzPocP'
headers = {'Authorization': f'Bearer {bearer_token}'}
# API実行
# context_annotationsを指定すると、entity, contextが抽出できる
params = {'query':'一番搾り',                    
        'tweet.fields': 'id,text,author_id,context_annotations',        
        }
response = requests.request("GET", url, headers = headers, params = params)
result = json.loads(response.content.decode('utf-8'))
print(json.dumps(result, indent=4, ensure_ascii=False))