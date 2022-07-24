<<<<<<< HEAD
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
        decorators=[MatchContent("黑丝")],
    )
)

async def heisi(app: Ariadne, friend: Friend): # lsp专属
    ero_url = "https://api.lolicon.app/setu/v2?r18=0&tag=黑丝"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(ero_url) as r:
                ret = await r.json()
                pic_url = ret["data"][0]["urls"]["original"]
            async with session.get(pic_url) as r:
                pic = await r.read()
                await app.send_friend_message(friend, MessageChain.create(FlashImage(data_bytes=pic)))
    except Exception as Err:
        await app.send_friend_message(friend, MessageChain.create(f'错误 {Err}'))
=======
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
        decorators=[MatchContent("黑丝")],
    )
)

async def heisi(app: Ariadne, friend: Friend): # lsp专属
    ero_url = "https://api.lolicon.app/setu/v2?r18=0&tag=黑丝"
    async with aiohttp.ClientSession() as session:
        async with session.get(ero_url) as r:
            ret = await r.json()
            pic_url = ret["data"][0]["urls"]["original"]
        async with session.get(pic_url) as r:
            pic = await r.read()
            await app.sendFriendMessage(friend, MessageChain.create(FlashImage(data_bytes=pic)))
>>>>>>> 8709c7ac59921100c5a4936eda9f178021bb5f67
