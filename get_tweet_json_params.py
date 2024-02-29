# Twitter API v2のTweets countsで指定キーワードを含むツイートのリストを取得
# https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction
import json
import requests
import urllib.parse

# 検索条件
url = f'https://api.twitter.com/2/tweets/search/recent'
# 認証
bearer_token = ''
headers = {'Authorization': f'Bearer {bearer_token}'}
# API実行
# paramsで抽出条件を細かく指定している。
params = {'query':'一番搾り',                    
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}}
response = requests.request("GET", url, headers = headers, params = params)
result = json.loads(response.content.decode('utf-8'))
print(json.dumps(result, indent=4, ensure_ascii=False))