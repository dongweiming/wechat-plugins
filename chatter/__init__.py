from wxpy import Friend
from wxpy.api.consts import TEXT

description = """
ChatterBot，触发条件: 和群主私聊
"""

try:
    from chatterbot import ChatBot
except ImportError:
    raise
    print('Chatterbot is not available')
    class ChatBot:
        def __init__(self, *args, **kwargs):
            pass

        def train(self, corpus):
            return ''

        def get_response(self, input_item, session_id=None):
            return ''


wechat = ChatBot('wechat',
                 database_uri='sqlite:///wechat.db',
                 trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
wechat.train('chatterbot.corpus.chinese')


class ChatterBotPlugin:
    name = 'ChatterBotPlugin'
    version = '0.1'
    chats = Friend
    msg_types = TEXT
    description = description
    exclude_patterns = ['help']

    @classmethod
    def main(cls, msg):
        return wechat.get_response(msg.text)


def export():
    return ChatterBotPlugin
