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
        await app.send_friend_message(friend, MessageChain.create(Plain("菜单 \n-------------\n1. 看腿\n2. 二次元\n3. 看美女\n4. 涩图\n5. 白丝\n6. 黑丝\n7. 短发\n8. 原神\n9. 骚话\n10. 白发\n11. cos图(收图有一定的延迟)\n12. 舔狗日记\n--------------\n发送文字 即可食用\n-------------")))
