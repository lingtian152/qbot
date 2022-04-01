import asyncio
from loguru import logger
import random
import aiohttp

from graia.broadcast import Broadcast
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage, FriendMessage
from graia.ariadne.message.chain import MessageChain, Source
from graia.ariadne.message.element import Plain, Image, FlashImage
from graia.ariadne.model import Group, MiraiSession, Friend, Member
from graia.ariadne.console import Console
from graia.broadcast import Broadcast
from graia.ariadne import get_running
from graia.ariadne.adapter import Adapter
from graia.saya import Saya
from graia.saya.builtins.broadcast import BroadcastBehaviour


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
    elif str(command) == "version":
        await logger.info(f'version: {app.getVersion}')


@broadcast.receiver("GroupMessage")
async def group_message_listener(app: Ariadne, group: Group, msg: MessageChain):
    if group.id != int(435237486):
        return None
    else:
        if str(msg) == "菜单":
            await app.sendGroupMessage(group, msg.create([Plain(f'菜单 \n ----------- \n 1. 看腿 \n 2. 二次元(暂时无法使用) \n 3. 看美女(看妹子) \n 4. 涩图 \n 5. 黑丝 \n 6. 短发 \n 7. 白丝 \n -----------')]))
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
        elif str(msg) == "涩图":
            ero_url = "https://api.lolicon.app/setu/v2"
            async with aiohttp.ClientSession() as session:
                async with session.get(ero_url) as r:
                    ret = await r.json()
                    pic_url = ret["data"][0]["urls"]["original"]
                async with session.get(pic_url) as r:
                    pic = await r.read()
                    await app.sendGroupMessage(group, msg.create(FlashImage(data_bytes=pic)))
        elif str(msg) == "白丝":
            ero_url = "https://api.lolicon.app/setu/v2?r18=0&tag=白丝"
            async with aiohttp.ClientSession() as session:
                async with session.get(ero_url) as r:
                    ret = await r.json()
                    pic_url = ret["data"][0]["urls"]["original"]
                async with session.get(pic_url) as r:
                    pic = await r.read()
                    await app.sendGroupMessage(group, msg.create(FlashImage(data_bytes=pic)))
        elif str(msg) == "黑丝":
            ero_url = "https://api.lolicon.app/setu/v2?r18=0&tag=黑丝"
            async with aiohttp.ClientSession() as session:
                async with session.get(ero_url) as r:
                    ret = await r.json()
                    pic_url = ret["data"][0]["urls"]["original"]
                async with session.get(pic_url) as r:
                    pic = await r.read()
                    await app.sendGroupMessage(group, msg.create(FlashImage(data_bytes=pic)))
        elif str(msg) == "短发":
            ero_url = "https://api.lolicon.app/setu/v2?r18=0&tag=短发"
            async with aiohttp.ClientSession() as session:
                async with session.get(ero_url) as r:
                    ret = await r.json()
                    pic_url = ret["data"][0]["urls"]["original"]
                async with session.get(pic_url) as r:
                    pic = await r.read()
                    await app.sendGroupMessage(group, msg.create(FlashImage(data_bytes=pic)))
        elif str(msg) == "原神":
            ero_url = "https://api.lolicon.app/setu/v2?r18=0&tag=原神"
            async with aiohttp.ClientSession() as session:
                async with session.get(ero_url) as r:
                    ret = await r.json()
                    pic_url = ret["data"][0]["urls"]["original"]
                async with session.get(pic_url) as r:
                    pic = await r.read()
                    await app.sendGroupMessage(group, msg.create(FlashImage(data_bytes=pic)))
            asyncio.sleep(60)
            await app.recallMessage(msg)


@broadcast.receiver("FriendMessage")
async def on_message(app: Ariadne, friend: Friend, msg: MessageChain):
    if str(msg) == "菜单":
        await app.sendFriendMessage(friend, msg.create([Plain(f'菜单 \n ----------- \n 1. 看腿 \n 2. 二次元(暂时无法使用) \n 3. 看美女(看妹子) \n 4. 涩图 \n 5. 黑丝 \n 6. 短发 \n 7. 白丝 \n -----------')]))
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
    elif str(msg) == "涩图":
        ero_url = "https://api.lolicon.app/setu/v2"
        async with aiohttp.ClientSession() as session:
            async with session.get(ero_url) as r:
                ret = await r.json()
                pic_url = ret["data"][0]["urls"]["original"]
            async with session.get(pic_url) as r:
                pic = await r.read()
                await app.sendFriendMessage(friend, msg.create(FlashImage(data_bytes=pic)))
    elif str(msg) == "白丝":
        ero_url = "https://api.lolicon.app/setu/v2?r18=0&tag=白丝"
        async with aiohttp.ClientSession() as session:
            async with session.get(ero_url) as r:
                ret = await r.json()
                pic_url = ret["data"][0]["urls"]["original"]
            async with session.get(pic_url) as r:
                pic = await r.read()
                await app.sendFriendMessage(friend, msg.create(FlashImage(data_bytes=pic)))
    elif str(msg) == "黑丝":
        ero_url = "https://api.lolicon.app/setu/v2?r18=0&tag=黑丝"
        async with aiohttp.ClientSession() as session:
            async with session.get(ero_url) as r:
                ret = await r.json()
                pic_url = ret["data"][0]["urls"]["original"]
            async with session.get(pic_url) as r:
                pic = await r.read()
                await app.sendFriendMessage(friend, msg.create(FlashImage(data_bytes=pic)))
    elif str(msg) == "短发":
        ero_url = "https://api.lolicon.app/setu/v2?r18=0&tag=短发"
        async with aiohttp.ClientSession() as session:
            async with session.get(ero_url) as r:
                ret = await r.json()
                pic_url = ret["data"][0]["urls"]["original"]
            async with session.get(pic_url) as r:
                pic = await r.read()
                await app.sendFriendMessage(friend, msg.create(FlashImage(data_bytes=pic)))


loop.run_until_complete(app.lifecycle())
