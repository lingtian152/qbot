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
        decorators=[MatchContent("菜单")],
    )
)

async def help(app: Ariadne, friend: Friend): # 帮助
    await app.sendFriendMessage(friend, MessageChain.create([Plain(f'菜单 \n ----------- \n 1. 看腿 \n 2. 二次元 \n 3. 看美女 \n 4. 涩图 \n 5. 白丝 \n 6. 黑丝 \n 7. 短发 \n 8. 原神 \n 9.骚话 \n 10. 白发(无法使用) \n ----------- \n 发送文字 即可使用 \n -------------')]))
