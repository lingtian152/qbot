import aiohttp
import random

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import FriendMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Image, Plain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Friend
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

channel = Channel.current()


@channel.use(
    ListenerSchema(
        listening_events=[FriendMessage],
        decorators=[MatchContent("二次元")],
    )
)
async def anime(app: Ariadne, friend: Friend, msg: MessageChain):  # 动漫
    ero_url = ["https://api.ghser.com/random/api.php",
               "https://api.ghser.com/random/pc.php",
               "https://api.ghser.com/random/pe.php"]

    async with aiohttp.ClientSession() as client:
        try:
            await app.send_friend_message(friend, msg.create(Image(url=random.choice(ero_url))))
        except Exception as err:
            await app.send_friend_message(friend, msg.create(Plain(f'错误 {err}')))
            print(f'错误 {err}')