from flask import current_app
from wxpy import Tuling
from wxpy.api.consts import TEXT


description = """
图灵机器人，触发条件: @群主 即可
"""

try:
    from config import TULING_KEY
except:
    TULING_KEY = '5194eb3277ec4a86b404695f8f991706'

tuling = Tuling(api_key=TULING_KEY)


class TulingPlugin:
    name = 'TulingPlugin'
    version = '0.1'
    msg_types = TEXT
    description = description

    @classmethod
    def main(cls, msg):
        nick_name = current_app.nick_name if current_app else None
        if nick_name is not None:
            at = '@{}'.format(nick_name)
            text = msg.text
            if at in text:
                msg.text = text.replace(at, '').replace('\u2005', '').strip()
                tuling.do_reply(msg)
        return ''  # do_reply已经是回应了，所以不会返回再回应一次


def export():
    return TulingPlugin
