# twitter-stream1.py
import tweepy
from datetime import timedelta
CK = 'nZK2vC8e58xYpu319vq3xey3y'
CS = 'FYLzkwe1ZWudST1uAEvLdEwu9vj9xrcpM2sn4nElZaZCL9drWI'
#Twitter Deverloper Portalで取得したベアラートークンをコーテション('')の間に入れる
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAH4RsgEAAAAAx2phEmbAQtdV6DCRAaItUM7VN7E%3D7YGZbqdfY7zCncPyUy1qjCIqK7yxvHVxjIc13d0JU8ATfzPocP'
#Twitter Deverloper Portalで生成したアクセストークンをコーテション('')の間にそれぞれ入れる
AT = 'NllZbkRieUJLNWNiMm1VbDRTWDU6MTpjaQ'
AS = 'oOJqY74-v6QWwvilef0RQ8G6X0CoUIo_n6xJDeqRg01MrRW4gF'
'''
CK = 'xxxx' # Consumer Key
CS = 'xxxx' # Consumer Secret
AT = 'xxxx' # Access Token
AS = 'xxxx' # Accesss Token Secert
'''
 # StreamListenerを継承するクラスListener作成
class Listener(tweepy.StreamListener):
    def on_status(self, status):
        status.created_at += timedelta(hours=9)#世界標準時から日本時間に

        print('------------------------------')
        print(status.text)
        print("{name}({screen}) {created} via {src}\n".format(
                                                               name=status.author.name, screen=status.author.screen_name,
                                                               created=status.created_at, src=status.source))
        return True

    def on_error(self, status_code):
        print('エラー発生: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

 # Listenerクラスのインスタンス
listener = Listener()
# 受信開始
stream = tweepy.Stream(auth, listener)
stream.filter(track = ["プログラミング"])# 指定の検索ワードでフィルタ