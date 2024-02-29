# annotationを取得する
params中、'tweet.fields': `context_annotations'を指定すると、context, entity情報を抽出できる。これらのコード体系は[こちら](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet)  
[get_tweet_json_annot.py](get_tweet_json_annot.py)
``` python 
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
```

# page nation
1 page(100 tweet)づつ繰り返し取得する。parmsのnext token に['meta']['next_token']に返却されるnext page情報を設定する。コーディング例は[こちら](https://is-ai.jp/?p=16)  
[get_tweet_json_pagenation.py](get_tweet_json_pagenation.py)


``` python
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
```