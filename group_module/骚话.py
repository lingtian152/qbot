import json

import requests
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

channel = Channel.current()


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("骚话")],
    )
)
async def saohua(app: Ariadne, group: Group):  # 骚话
    with open("group_module\config\group_config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    if config[str(group.id)] == "true":
        try:
            req = requests.get("http://api.ay15.cn/api/saohua/api.php")
            text = req.content

            await app.send_group_message(group, MessageChain(Plain(text)))
        except Exception as Err:
            await app.send_group_message(group, MessageChain(Plain(f'错误 {Err}')))
            print(f'错误 {Err}')
