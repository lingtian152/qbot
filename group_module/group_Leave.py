import json

from graia.ariadne.app import Ariadne
from graia.ariadne.event.mirai import (BotLeaveEventActive, BotLeaveEventKick, BotLeaveEventDisband)
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

channel_1 = Channel.current()
channel_2 = Channel.current()
channel_3 = Channel.current()


@channel_1.use(
    ListenerSchema(
        listening_events=[BotLeaveEventActive],
    )
)
async def Leave_group(app: Ariadne, group: BotLeaveEventActive): # Bot Leave Group
    with open("group_module\config\group_config.json", "r") as f:
        group_id = json.load(f)

        group_id.pop(str(group.group.id)) # remove group config

    with open("group_module\config\group_config.json", "w") as f:
        json.dump(group_id, f, indent=4)


@channel_2.use(
    ListenerSchema(
        listening_events=[BotLeaveEventDisband],
    )
)
async def Leave_group(app: Ariadne, group: BotLeaveEventDisband): # ?
    with open("group_modules\config\group_config.json", "r") as f:
        group_id = json.load(f)

        group_id.pop([str(group.group.id)])

    with open("group_modules\config\group_config.json", "w") as f:
        json.dump(group_id, f, indent=4)


@channel_3.use(
    ListenerSchema(
        listening_events=[BotLeaveEventKick],
    )
)
async def Kick_Group(app: Ariadne, group: BotLeaveEventKick): # Bot Leave by Kick   
    with open("group_module\config\group_config.json", "r") as f:
        group_id = json.load(f)

        group_id.pop(str(group.group.id)) # remove group config

    with open("group_module\config\group_config.json", "w") as f:
        json.dump(group_id, f, indent=4)
