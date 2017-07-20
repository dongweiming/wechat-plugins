# -*-coding:utf-8-*-
"""
Copy from https://github.com/python-cn/slack_bot
"""

import requests
import random
from wxpy import Friend
from wxpy.api.consts import TEXT

try:
    from config import SIMSIMI_KEY
except:
    SIMSIMI_KEY = '6afe892c-596b-4743-a9a1-123ea951b88f'

description = """
色色的小黄鸡。触发条件：所有未触发其他插件的内容。
"""

COOKIE = "lang=zh_CN; normalProb=0; lc=ch; dotcom_session_key=s%3Al72WKytkaM46llEhIhE4-gRTK1esLSAX.k2HkRSHiK4UDOfM2WHTDVArOVZsmJ7%2Bfpo%2FF01qtOqg; currentChatCnt=1; _ga=GA1.2.1248391853.1500434158; _gid=GA1.2.950691851.1500434158"


class SimSimi:

    def __init__(self):

        self.session = requests.Session()

        self.chat_url = (
            'http://simsimi.com/getRealtimeReq?lc=ch&ft=1&normalProb=0&'
            'reqText={}&status=W&talkCnt=0'
        )
        self.api_url = ('http://sandbox.api.simsimi.com/request.p?'
                        'key=%s&lc=ch&ft=1.0&text=%s')

    def initSimSimiCookie(self):
        self.session.headers.update(
            {
                'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
                               ' AppleWebKit/537.36 (KHTML, like Gecko)'
                               ' Chrome/43.0.2357.81 Safari/537.36'),
                'Referer': 'http://simsimi.com/',
                'Host': 'simsimi.com',
                'Accept-Language' : 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',  # noqa
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Cookie': COOKIE
            })

    def getSimSimiResult(self, message, method='normal'):
        if method == 'normal':
            self.initSimSimiCookie()
            r = self.session.get(self.chat_url.format(message))
        else:
            url = self.api_url % (SIMSIMI_KEY, message)
            r = requests.get(url)
        return r

    def chat(self, message=''):
        if message:
            r = self.getSimSimiResult(message, 'api')
            try:
                answer = r.json()['response'].encode('utf-8')
                return answer
            except:
                try:
                    r = self.getSimSimiResult(message, 'normal')
                    answer = r.json()['respSentence'].encode('utf-8')
                    return answer
                except:
                    return random.choice(['呵呵', '。。。', '= =', '=。='])
        else:
            return '叫我干嘛'

simsimi = SimSimi()


class SimSimiPlugin:
    name = 'SimSimiPlugin'
    version = '0.1'
    chats = Friend
    msg_types = TEXT
    except_self = True
    run_async = True
    patterns = None
    exclusive = False
    description = description
    exclude_patterns = ['help']

    @classmethod
    def main(cls, msg):
        rs = simsimi.chat(msg.text.lower()).strip()
        if not isinstance(rs, str):
            rs = rs.decode('utf-8')
        return rs


def export():
    return SimSimiPlugin


if __name__ == '__main__':
    print(simsimi.chat({'message': '最后一个问题'}))
    print(simsimi.chat({'message': '还有一个问题'}))
    print(simsimi.chat({'message': '其实我有三个问题'}))
