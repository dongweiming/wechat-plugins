from wxpy import Tuling
from wxpy.api.consts import TEXT


description = """
图灵机器人，触发条件: @Python之美 即可
"""

try:
    from config import TULING_KEY
except:
    TULING_KEY = '5194eb3277ec4a86b404695f8f991706'

tuling = Tuling(api_key=TULING_KEY)


class TulingPlugin:
    name = 'TulingPlugin'
    version = '0.1'
    patterns = ['@Python之美']
    description = description

    @classmethod
    def main(cls, msg):
        return tuling.do_reply(msg)


def export():
    return TulingPlugin
