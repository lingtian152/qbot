import json
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

channel = Channel.current()
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("菜单")],
    )
)
async def help(app: Ariadne, group: Group):
    with open("group_modules\config\group_config.json", "r") as con:
        config = json.load(con)

        if config[str(group.id)] == "true":
            with open("group_modules\config\help.txt", 'r', encoding='utf8', errors='ignore') as f:
                txt = f.readlines()
            await app.send_group_message(group, MessageChain.create(txt))

            f.close()