import requests
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import FriendMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Friend
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

channel = Channel.current()


@channel.use(
    ListenerSchema(
        listening_events=[FriendMessage],
        decorators=[MatchContent("舔狗日记")],
    )
)
async def shoahua(app: Ariadne, friend: Friend):  # 骚话
    try:
        req = requests.get("http://api.ay15.cn/api/tiangou/api.php")
        text = req.content

        await app.send_friend_message(friend, MessageChain(Plain(text)))
    except Exception as Err:
        await app.send_friend_message(friend, MessageChain(Plain(f'错误 {Err}')))
        print(f'错误 {Err}')
