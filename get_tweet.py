import tweepy
#Twitter Deverloper Portalで取得したAPIキーをコーテション('')の間にそれぞれ入れる
API_KEY = 'nZK2vC8e58xYpu319vq3xey3y'
API_KEY_SECRET = 'FYLzkwe1ZWudST1uAEvLdEwu9vj9xrcpM2sn4nElZaZCL9drWI'
#Twitter Deverloper Portalで取得したベアラートークンをコーテション('')の間に入れる
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAH4RsgEAAAAAx2phEmbAQtdV6DCRAaItUM7VN7E%3D7YGZbqdfY7zCncPyUy1qjCIqK7yxvHVxjIc13d0JU8ATfzPocP'
#Twitter Deverloper Portalで生成したアクセストークンをコーテション('')の間にそれぞれ入れる
ACCESS_TOKEN = 'NllZbkRieUJLNWNiMm1VbDRTWDU6MTpjaQ'
ACCSESS_TOKEN_SECRET = 'oOJqY74-v6QWwvilef0RQ8G6X0CoUIo_n6xJDeqRg01MrRW4gF'

#リファレンスの内容に沿って入力（https://docs.tweepy.org/en/stable/client.html）
client = tweepy.Client(bearer_token = BEARER_TOKEN, consumer_key = API_KEY, consumer_secret = API_KEY_SECRET, access_token = ACCESS_TOKEN, access_token_secret = ACCSESS_TOKEN_SECRET)

QUERY = input("検索するキーワードを入力： ")
#Tweetを取得する上限
MAX_RESULTS = 10
tweets = client.search_recent_tweets(query = QUERY, max_results = MAX_RESULTS)
print(tweets)
tweets_data = tweets.data

if tweets_data != None:
    for i, tweet in enumerate(tweets_data):
        print("No:" + str(i+1))
        print("tweet.text: " + tweet.text)
        print("\n")
else:
    print("該当がありませんでした")