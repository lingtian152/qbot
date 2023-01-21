import json
import aiohttp
import random

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain, Image
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

channel = Channel.current()


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("腿")],
    )
)
async def saohua(app: Ariadne, group: Group):  # 骚话
    with open("group_module\config\group_config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    if config[str(group.id)] == "true":
        try:
            ero_url = [
                "http://api.starrobotwl.com/api/baisi.php",
                "http://api.starrobotwl.com/api/heisi.php",
            ]
            async with aiohttp.ClientSession() as session:
                await app.send_group_message(
                    group, MessageChain(Image(url=random.choice(ero_url)))
                )
        except Exception as Err:
            await app.send_group_message(group, MessageChain(Plain(f"错误 {Err}")))
            print(f"错误 {Err}")
