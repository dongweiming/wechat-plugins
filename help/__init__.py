from flask import current_app
from wxpy import Friend
from wxpy.api.consts import TEXT

description = """
帮助信息，触发条件: "help"
"""

help_text = """
目前支持如下插件：
{}
"""

def format_desc(plugin, prefix='  '):
    name = plugin.name.replace('Plugin', '')
    desc = getattr(plugin, 'description', '').strip()
    desc = ('\n' + prefix).join(desc.split('\n'))
    return '{name}:\n{prefix}{desc}'.format(
        name=name, prefix=prefix, desc=desc
    )


class HelpPlugin:
    name = 'HelpPlugin'
    version = '0.1'
    chats = Friend
    msg_types = TEXT
    patterns = ['help']
    exclusive = True
    description = description

    @classmethod
    def main(cls, msg):
        plugin_modules = current_app.plugin_modules if current_app else []
        docs = []
        for plugin in plugin_modules.values():
            docs.append(format_desc(plugin))
        return help_text.format('\n'.join(docs))


def export():
    return HelpPlugin
