# twitter-stream1.py
import tweepy
from datetime import timedelta

CK = 'xxxx' # Consumer Key
CS = 'xxxx' # Consumer Secret
AT = 'xxxx' # Access Token
AS = 'xxxx' # Accesss Token Secert

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