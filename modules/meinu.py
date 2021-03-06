import random
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

async def meinu(app: Ariadne, friend: Friend): # lsp专属
    img = ["http://api.lingfeng.press/api/pcmnt.php",
           "http://api.lingfeng.press/api/sjmnt.php"]
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(str(random.choice(img))) as r:
                data = await r.read()
        await app.send_friend_message(friend, MessageChain.create(Image(data_bytes=data)))
    except Exception as Err:
        await app.send_friend_message(friend, MessageChain.create(Plain(f'错误 {Err}')))
        print(f'错误 {Err}')
