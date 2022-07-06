import requests
import aiohttp
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import FriendMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Image
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Friend
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

channel = Channel.current()


@channel.use(
    ListenerSchema(
        listening_events=[FriendMessage],
        decorators=[MatchContent("看腿")],
    )
)

async def tui(app: Ariadne, friend: Friend):  # 腿控图
    r = requests.get("http://api.lingfeng.press/api/tu.php")
    data = r.text
    async with aiohttp.ClientSession() as session:
        await app.sendFriendMessage(friend, MessageChain.create(Image(url=data)))