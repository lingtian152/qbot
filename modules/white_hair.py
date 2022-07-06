import random
import aiohttp
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import FriendMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import FlashImage
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Friend
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

channel = Channel.current()


@channel.use(
    ListenerSchema(
        listening_events=[FriendMessage],
        decorators=[MatchContent("白发")],
    )
)

async def white_hair(app: Ariadne, friend: Friend): # lsp专属
    ero_url = "https://api.lolicon.app/setu/v2?tag=白髮&r18=0"
    async with aiohttp.ClientSession() as session:
        async with session.get(ero_url) as r:
            ret = await r.json()
            pic_url = ret["data"][0]["urls"]["original"]
    async with session.get(pic_url) as r:
        pic = await r.read()
        await app.sendFriendMessage(friend, MessageChain.create(FlashImage(data_bytes=pic)))