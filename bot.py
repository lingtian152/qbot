import asyncio
import random
import aiohttp
import requests

# bot moduels
from graia.ariadne import get_running
from graia.ariadne.adapter import Adapter
from graia.ariadne.app import Ariadne
from graia.ariadne.console import Console
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import FlashImage, Image, Plain
from graia.ariadne.model import Friend, MiraiSession
from graia.broadcast import Broadcast

loop = asyncio.new_event_loop()

broadcast = Broadcast(loop=loop)
app = Ariadne(
    broadcast=broadcast,
    connect_info=MiraiSession(
        host="http://localhost:8080",  # 填入 HTTP API 服务运行的地址
        verify_key="INITKEYxyFw6Q17",  # 填入 verifyKey
        account= 1330542948,  # 你的机器人的 qq 号
    )
)


bot_owner = 1553396053 # 机器人持有者账号
bot_admin = None # 机器人管理者账号 格式: {"114514", "114514"}

con = Console(broadcast=broadcast, prompt="Console> ")

# 控制台


@con.register()
async def cmd(app: Ariadne, command: str):
    if str(command) == "stop" or str(command) == "exit":
        await app.stop()

async def help(app, msg, friend): # 帮助
    await app.sendFriendMessage(friend, msg.create([Plain(f'菜单 \n ----------- \n 1. 看腿 \n 2. 二次元 \n 3. 看美女(看妹子) \n 4. 涩图 \n 5. 黑丝 \n 6. 短发 \n 7. 白丝 8. 原神 \n 9.骚话 \n 10. 白发 \n ----------- \n 发送序列号或者文字 即可使用 \n -------------')]))

async def tui(app, msg, friend):  # 腿控图
    r = requests.get("http://api.lingfeng.press/api/tu.php")
    data = r.text
    async with aiohttp.ClientSession() as session:
        await app.sendFriendMessage(friend, msg.create(Image(url=data)))


async def anime(app, msg, friend):  # 动漫
    ero_url = "https://api.ghser.com/random/api.php"
    async with aiohttp.ClientSession() as session:
        await app.sendFriendMessage(friend, msg.create(Image(url=ero_url)))


async def meinu(app, msg, friend): # lsp专属
    session = get_running(Adapter).session
    img = ["http://api.lingfeng.press/api/pcmnt.php",
           "http://api.lingfeng.press/api/sjmnt.php"]
    async with session.get(str(random.choice(img))) as r:
        data = await r.read()
        await app.sendFriendMessage(friend, msg.create(Image(data_bytes=data)))


async def se_Image(app, msg, friend): # lsp专属#2
    ero_url = "https://api.lolicon.app/setu/v2"
    async with aiohttp.ClientSession() as session:
       async with session.get(ero_url) as r:
            ret = await r.json()
            pic_url = ret["data"][0]["urls"]["original"]
       async with session.get(pic_url) as r:
            pic = await r.read()
            await app.sendFriendMessage(friend, msg.create(FlashImage(data_bytes=pic)))

async def baisi(app, msg, friend): # 白丝
    ero_url = "https://api.lolicon.app/setu/v2?r18=0&tag=白丝"
    async with aiohttp.ClientSession() as session:
        async with session.get(ero_url) as r:
            ret = await r.json()
            pic_url = ret["data"][0]["urls"]["original"]
        async with session.get(pic_url) as r:
            pic = await r.read()
            await app.sendFriendMessage(friend, msg.create(FlashImage(data_bytes=pic)))

async def heisi(app, msg, friend): # 黑丝
    ero_url = "https://api.lolicon.app/setu/v2?r18=0&tag=黑丝"
    async with aiohttp.ClientSession() as session:
        async with session.get(ero_url) as r:
            ret = await r.json()
            pic_url = ret["data"][0]["urls"]["original"]
        async with session.get(pic_url) as r:
            pic = await r.read()
            await app.sendFriendMessage(friend, msg.create(FlashImage(data_bytes=pic)))

async def short_hair(app, msg, friend): # 短发
    ero_url = "https://api.lolicon.app/setu/v2?r18=0&tag=短发"
    async with aiohttp.ClientSession() as session:
        async with session.get(ero_url) as r:
            ret = await r.json()
            pic_url = ret["data"][0]["urls"]["original"]
        async with session.get(pic_url) as r:
            pic = await r.read()
            await app.sendFriendMessage(friend, msg.create(FlashImage(data_bytes=pic)))

async def genshin(app, msg, friend): # 原神
    ero_url = "https://api.lolicon.app/setu/v2?r18=0&tag=原神"
    async with aiohttp.ClientSession() as session:
        async with session.get(ero_url) as r:
            ret = await r.json()
            pic_url = ret["data"][0]["urls"]["original"]
        async with session.get(pic_url) as r:
            pic = await r.read()
            await app.sendFriendMessage(friend, msg.create(FlashImage(data_bytes=pic)))

async def shaohua(app, msg, friend):
    req = requests.get("https://api.ghser.com/saohua/")
    text = req.content
    await app.sendFriendMessage(friend, msg.create(Plain(text)))

async def white_hair(app, msg, friend):
    ero_url = "https://api.lolicon.app/setu/v2?tag=白髮&r18=0"
    async with aiohttp.ClientSession() as session:
        async with session.get(ero_url) as r:
            ret = await r.json()
            pic_url = ret["data"][0]["urls"]["original"]
    async with session.get(pic_url) as r:
        pic = await r.read()
        await app.sendFriendMessage(friend, msg.create(FlashImage(data_bytes=pic)))

# 好友消息
@broadcast.receiver("FriendMessage")
async def on_message(app: Ariadne, friend: Friend, msg: MessageChain):
    if str(msg) == "菜单":
        asyncio.create_task(help(app, msg, friend))
    elif str(msg) == "看腿" or str(msg) == "1":
        asyncio.create_task(tui(app, msg, friend))
    elif str(msg) == "二次元" or str(msg) == "2":
        asyncio.create_task(anime(app, msg, friend))
    elif str(msg) == "看妹子" or str(msg) == "看美女" or str(msg) == "3":
        asyncio.create_task(meinu(app, msg, friend))
    elif str(msg) == "涩图" or str(msg) == 4:
        asyncio.create_task(se_Image(app, msg, friend))
    elif str(msg) == "白丝" or str(msg) == "7":
        asyncio.create_task(baisi(app, msg, friend))
    elif str(msg) == "黑丝" or str(msg) == "5":
        asyncio.create_task(heisi(app, msg, friend))
    elif str(msg) == "短发":
        asyncio.create_task(short_hair(app, msg, friend))
    elif str(msg) == "原神" or str(msg) == "8":
        asyncio.create_task(genshin(app, msg, friend))
    elif str(msg) == "骚话" or str(msg) == "9":
        asyncio.create_task(shaohua(app, msg, friend))
    elif str(msg) == "白发" or str(msg) == "10":
        asyncio.create_task(white_hair(app, msg, friend))

    if friend.id == bot_owner:
        if str(msg) == "exit" or str(msg) == "stop" or str(msg) == "关机":
            await app.sendFriendMessage(friend, msg.create(Plain('已关机')))
            await app.stop()
        elif str(msg) == "获取游戏数据":
            game_url = "https://games.roblox.com/v1/games?universeIds=2530837063"
            game_vote_url = "https://games.roblox.com/v1/games/votes?universeIds=2530837063"
            async with aiohttp.ClientSession() as session:
                async with session.get(game_url) as r:
                    if r.status == 200:
                        ret = await r.json()
                        game_name = ret["data"][0]["name"]
                        game_id = ret["data"][0]["id"]
                        game_playing = ret["data"][0]["playing"]
                        game_favorite = ret["data"][0]["favoritedCount"]
                        visits = ret["data"][0]["visits"]
                async with session.get(game_vote_url) as r:
                    if r.status == 200:
                        ret = await r.json()
                        vote_up = ret["data"][0]["upVotes"]
                        vote_down = ret["data"][0]["downVotes"]
                await app.sendFriendMessage(friend, msg.create(Plain("正在获取游戏数据...")))
                asyncio.sleep(5)
                await app.sendFriendMessage(friend, msg.create(Plain(f'游戏名字: {game_name}\n游戏ID: {game_id}\n游戏在线人数: {game_playing}\n游戏收藏量: {game_favorite}\n浏览量: {visits}\n喜欢人数: {vote_up}\n不喜欢人数: {vote_down}\n总投票人数: {vote_up + vote_down}')))
                

loop.run_until_complete(app.lifecycle())
