import random
import aiohttp
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import FriendMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import FlashImage, Plain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Friend
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

channel = Channel.current()


@channel.use(
    ListenerSchema(
        listening_events=[FriendMessage],
        decorators=[MatchContent("短发")],
    )
)

async def heisi(app: Ariadne, friend: Friend): # lsp专属
    ero_url = "https://api.lolicon.app/setu/v2?r18=0&tag=短发"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(ero_url) as r:
                ret = await r.json()
                pic_url = ret["data"][0]["urls"]["original"]
            async with session.get(pic_url) as r:
                pic = await r.read()
                await app.send_friend_message(friend, MessageChain.create(FlashImage(data_bytes=pic)))
    except Exception as Err:
        await app.send_friend_message(friend, MessageChain.create(Plain(f'错误 {Err}')))
        print(f'错误 {Err}')