import json

from graia.ariadne.event.mirai import BotInvitedJoinGroupRequestEvent, BotJoinGroupEvent
from graia.ariadne.app import Ariadne
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema




channel_1 = Channel.current()
channel_2 = Channel.current()

@channel_1.use(
    ListenerSchema(
        listening_events=[BotJoinGroupEvent],
    )
)
async def Join_group(app: Ariadne, group: BotJoinGroupEvent):
    with open('group_modules\config\group_config.json', "r") as f:
        group_id = json.load(f)
    
    group_id[str(group.group.id)] = "false"

    with open("group_modules\config\group_config.json", "w") as f:
        json.dump(group_id, f, indent=4)


@channel_2.use(
    ListenerSchema(
        listening_events=[BotInvitedJoinGroupRequestEvent],
    )
)
async def Join_group(app: Ariadne, group: BotInvitedJoinGroupRequestEvent):
    with open('group_modules\config\group_config.json', "r", encoding="utf-8") as f:
        group_id = json.load(f)
    
    group_id[str(group.source_group)] = "false"

    with open("group_modules\config\group_config.json", "w", encoding="utf-8") as f:
        json.dump(group_id, f, indent=4)