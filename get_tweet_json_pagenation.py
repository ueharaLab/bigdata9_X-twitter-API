

import json
import requests
import urllib.parse

# 検索条件
url = f'https://api.twitter.com/2/tweets/search/recent'
# 認証
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAH4RsgEAAAAAx2phEmbAQtdV6DCRAaItUM7VN7E%3D7YGZbqdfY7zCncPyUy1qjCIqK7yxvHVxjIc13d0JU8ATfzPocP'
headers = {'Authorization': f'Bearer {bearer_token}'}
# API実行
# paramsで抽出条件を細かく指定している。
params = {'query':'一番搾り',
          'tweet.fields': 'id,text,author_id,context_annotations',        
          'next_token': {}}
def get_tweet_by_text(url,headers, params):
    response = requests.request("GET", url, headers = headers, params = params)
    result = json.loads(response.content.decode('utf-8'))
    return result

has_next = True
pages =1
while has_next:
  result = get_tweet_by_text(url, headers, params)
  
  print('page nation ',pages)
  print(json.dumps(result, indent=4, ensure_ascii=False))
  # 取得制限対策
  if not 'meta' in result:
      break
    
  # flag
  has_next = 'next_token' in result['meta']

  if has_next:
    params['next_token'] = result['meta']['next_token']
    pages+=1