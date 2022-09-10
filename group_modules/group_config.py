import json

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group, Member
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema
from graia.broadcast.builtin.decorators import Depend
from graia.broadcast.exceptions import ExecutionStop

def check_member(*members: int):
    async def check_member_deco(app: Ariadne, group: Group, member: Member):
        if member.id not in members:
            raise ExecutionStop
    return Depend(check_member_deco)

channel = Channel.current()
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("开机"), check_member(1553396053)],
    )
)

async def setup(app: Ariadne, group: Group): # 帮助
        with open("group_modules\config\group_config.json", encoding='utf8', errors='ignore') as config:
            Config = json.load(config)

        Config[str(group.id)] = "true"

        with open("group_modules\config\group_config.json", "w") as config:
            json.dump(Config, config, indent=4)

        await app.send_group_message(group.id, MessageChain("已开启"))

        
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("关机"), check_member(1553396053)],
    )
)

async def setdown(app: Ariadne, group: Group): # 帮助
        with open("group_modules\config\group_config.json", encoding='utf8', errors='ignore') as config:
            Config = json.load(config)

        Config[str(group.id)] = "false"

        with open("group_modules\config\group_config.json", "w") as config:
            json.dump(Config, config, indent=4)

        await app.send_group_message(group.id, MessageChain("已关机"))