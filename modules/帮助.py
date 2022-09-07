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

async def help(app: Ariadne, friend: Friend) -> str: # 帮助
    with open("modules\Config\help.txt", encoding='utf8', errors='ignore') as txt:
        text = txt.readlines()
    await app.send_friend_message(friend, MessageChain.create(text))
    txt.close()