import asyncio
from asyncio.windows_events import NULL
import json
import random
import aiohttp
import requests
from pathlib import Path

from graia.broadcast import Broadcast
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage, FriendMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain, Image
from graia.ariadne.model import Group, MiraiSession, Friend, Member
from graia.ariadne.message.parser.twilight import Twilight, ParamMatch, Sparkle, MatchResult
from graia.ariadne.console import Console
from graia.broadcast import Broadcast
from graia.saya.builtins.broadcast import BroadcastBehaviour
from graia.ariadne import get_running
from graia.ariadne.adapter import Adapter


loop = asyncio.new_event_loop()

broadcast = Broadcast(loop=loop)
app = Ariadne(
    broadcast=broadcast,
    connect_info=MiraiSession(
        host="http://localhost:8080",  # 填入 HTTP API 服务运行的地址
        verify_key="INITKEY5Fqqtvij",  # 填入 verifyKey
        account=1330542948,  # 你的机器人的 qq 号
    )
)


con = Console(broadcast=broadcast, prompt="Console> ")


@con.register()
async def cmd(app: Ariadne, command: str):
    if str(command) == "stop":
        await app.stop()


@broadcast.receiver("GroupMessage")
async def group_message_listener(app: Ariadne, group: Group, msg: MessageChain):
    if group.id != int(435237486):
        return NULL
    else:
        if str(msg) == "菜单":
            await app.sendGroupMessage(group, msg.create([Plain(f'菜单 \n ----------- \n 1. 看腿 \n 2. 二次元(暂时无法使用) \n 3. 看美女(看妹子) \n -----------')]))
        elif str(msg) == "看腿":
            session = get_running(Adapter).session
            async with session.get("http://api.lingfeng.press/api/tk.php") as r:
                data = await r.read()
                await app.sendGroupMessage(group, msg.create(Image(data_bytes=data)))
        elif str(msg) == "看妹子" or str(msg) == "看美女":
            session = get_running(Adapter).session
            img = ["http://api.lingfeng.press/api/pcmnt.php",
                   "http://api.lingfeng.press/api/sjmnt.php",
                   "http://api.lingfeng.press/api/sjmnt2.php"]
            async with session.get(str(random.choice(img))) as r:
                data = await r.read()
                await app.sendGroupMessage(group, msg.create(Image(data_bytes=data)))


@broadcast.receiver("FriendMessage")
async def on_message(app: Ariadne, friend: Friend, msg: MessageChain):
    if str(msg) == "菜单":
        await app.sendFriendMessage(friend, msg.create([Plain(f'菜单 \n ----------- \n 1. 看腿 \n 2. 二次元(暂时无法使用) \n 3. 看美女(看妹子) \n -----------')]))
    elif str(msg) == "看腿":
        session = get_running(Adapter).session
        async with session.get("http://api.lingfeng.press/api/tk.php") as r:
            data = await r.read()
            await app.sendFriendMessage(friend, msg.create(Image(data_bytes=data)))
    elif str(msg) == "看妹子" or str(msg) == "看美女":
        session = get_running(Adapter).session
        img = ["http://api.lingfeng.press/api/pcmnt.php",
               "http://api.lingfeng.press/api/sjmnt.php",
               "http://api.lingfeng.press/api/sjmnt2.php"]
        async with session.get(str(random.choice(img))) as r:
            data = await r.read()
            await app.sendFriendMessage(friend, msg.create(Image(data_bytes=data)))


loop.run_until_complete(app.lifecycle())
