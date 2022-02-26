import asyncio
import json


from tkinter.ttk import Style
from graia.broadcast import Broadcast
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage, FriendMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from graia.ariadne.model import Group, MiraiSession, Friend, Member
from graia.ariadne.message.parser.twilight import Twilight,ParamMatch, Sparkle
from graia.ariadne.console import Console
from graia.saya import Saya
from graia.broadcast import Broadcast
from graia.saya.builtins.broadcast import BroadcastBehaviour






loop = asyncio.get_event_loop()

broadcast = Broadcast(loop=loop)
app = Ariadne(
    broadcast=broadcast,
    connect_info=MiraiSession(
        host="http://localhost:8080",  # 填入 HTTP API 服务运行的地址
        verify_key="INITKEY3dneRqjR",  # 填入 verifyKey
        account=1330542948,  # 你的机器人的 qq 号
    )
)


con = Console(broadcast=broadcast, prompt="Console> ")


loop = asyncio.get_event_loop()
broadcast = Broadcast(loop=loop)



@con.register()
async def cmd(app: Ariadne, command: str):
    if str(command) == "stop":
        await app.stop()



@broadcast.receiver("GroupMessage")
async def group_message_listener(app: Ariadne, group: Group, message: MessageChain, arg=None):
    if str(message) == "早上好":
        await app.sendGroupMessage(group, MessageChain.create([Plain("早")]))
    elif str(message) == "早":
        await app.sendGroupMessage(group, MessageChain.create([Plain("早")]))
    elif str(message) == "早啊":
        await app.sendGroupMessage(group, MessageChain.create([Plain("早")]))
    
    if Member.id == int(1553396053):
        if str(message) == ';关闭':
            with open("./group.json", "r") as f:
                prefix = json.load(f)

            prefix[str(Member.group.id)] = str("关闭")
            
            with open("./group.json", "w") as f:
                json.dump(prefix, f, indent=4)



@broadcast.receiver("FriendMessage")
async def on_message(app: Ariadne, friend: Friend, group: Group, msg: MessageChain):
    if friend.id == int(1553396053):
        if str(msg) == ";关机":
            await app.sendFriendMessage(friend, msg.create([Plain("机器人已关机")]))
            await app.stop()
        elif str(msg) == ";stop":
            await app.sendFriendMessage(friend, msg.create([Plain("机器人已关机")]))
            await app.stop()
        elif str(msg) == ";菜单":
            await app.sendFriendMessage(friend, msg.create([Plain(f'菜单 \n ----------- \n 1. ;版本 \n 2. ;关机 \n -----------')]))
        elif str(msg) == ";版本":
            await app.sendFriendMessage(friend, msg.create([Plain(f'当前版本: {str(app.remote_version)}')]))
        else:
            await app.sendFriendMessage(friend, msg.create([Plain("未查询到当前指令, 请使用 ;帮助 查看指令")]))

loop.run_until_complete(app.lifecycle())
