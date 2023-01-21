import aiohttp
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
        decorators=[MatchContent("看美女")],
    )
)
async def meinu(app: Ariadne, friend: Friend):  # lsp专属
    img = "https://www.hlapi.cn/api/sjmm1"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(img) as r:
                data = await r.read()
        await app.send_friend_message(friend, MessageChain(Image(data_bytes=data)))
    except Exception as Err:
        await app.send_friend_message(friend, MessageChain(Plain(f'错误 {Err}')))
        print(f'错误 {Err}')
