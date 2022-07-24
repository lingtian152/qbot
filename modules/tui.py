import requests
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
        decorators=[MatchContent("看腿")],
    )
)

async def tui(app: Ariadne, friend: Friend):  # 腿控图
    try:
        r = requests.get("http://api.lingfeng.press/api/tu.php")
        data = r.text
        async with aiohttp.ClientSession() as session:
            await app.send_friend_message(friend, MessageChain.create(Image(url=data)))
    except Exception as Err:
        await app.send_friend_message(friend, MessageChain.create(Plain(f'错误 {Err}')))
        print(f'错误 {Err}')
