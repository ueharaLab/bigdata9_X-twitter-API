# Twitter API v2のTweets countsで指定キーワードを含むツイートのリストを取得
# https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction
import json
import requests
import urllib.parse

# 検索条件
query = '一番搾り'
url = f'https://api.twitter.com/2/tweets/search/recent?query={urllib.parse.quote(query)}'

# 認証
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAH4RsgEAAAAAx2phEmbAQtdV6DCRAaItUM7VN7E%3D7YGZbqdfY7zCncPyUy1qjCIqK7yxvHVxjIc13d0JU8ATfzPocP'
headers = {'Authorization': f'Bearer {bearer_token}'}
# API実行
response = requests.request('GET', url, headers=headers)
result = json.loads(response.content.decode('utf-8'))
print(json.dumps(result, indent=4, ensure_ascii=False))