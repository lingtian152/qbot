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
        decorators=[MatchContent("二次元")],
    )
)

async def anime(app: Ariadne, friend: Friend):  # 动漫
    ero_url = "https://api.ghser.com/random/api.php"
    async with aiohttp.ClientSession() as session:
        await app.sendFriendMessage(friend, MessageChain.create(Image(url=ero_url)))