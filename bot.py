import asyncio



# bot moduels
from graia.ariadne import get_running
from graia.ariadne.adapter import Adapter
from graia.ariadne.app import Ariadne
from graia.ariadne.console import Console
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import FlashImage, Image, Plain
from graia.ariadne.model import Friend, MiraiSession
from graia.broadcast import Broadcast
from graia.saya.builtins.broadcast import BroadcastBehaviour
from graia.saya import Saya



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
saya = Ariadne.create(app, Saya)
saya.install_behaviours(BroadcastBehaviour(broadcast))

bot_owner = 1553396053 # 机器人持有者账号
bot_admin = None # 机器人管理者账号 格式: {"114514", "114514"}


with saya.module_context(): # 模块加载
    saya.require("modules.help")
    saya.require("modules.tui")
    saya.require("modules.anime")
    saya.require("modules.meinu")
    saya.require("modules.setu")
    saya.require("modules.baisi")
    saya.require("modules.short_hair")
    saya.require("modules.genshin")
    saya.require("modules.shaohua")
    saya.require("modules.white_hair")
    saya.require("modules.get_game_data")


    # if friend.id == bot_owner:
    #     if str(msg) == "exit" or str(msg) == "stop" or str(msg) == "关机":
    #         await app.sendFriendMessage(friend, msg.create(Plain('已关机')))
    #         await app.stop()
        # elif str(msg) == "获取游戏数据":
            
            # game_url = "https://games.roblox.com/v1/games?universeIds=2530837063"
            # game_vote_url = "https://games.roblox.com/v1/games/votes?universeIds=2530837063"
            # async with aiohttp.ClientSession() as session:
            #     async with session.get(game_url) as r:
            #         if r.status == 200:
            #             ret = await r.json()
            #             game_name = ret["data"][0]["name"]
            #             game_id = ret["data"][0]["id"]
            #             game_playing = ret["data"][0]["playing"]
            #             game_favorite = ret["data"][0]["favoritedCount"]
            #             visits = ret["data"][0]["visits"]
            #     async with session.get(game_vote_url) as r:
            #         if r.status == 200:
            #             ret = await r.json()
            #             vote_up = ret["data"][0]["upVotes"]
            #             vote_down = ret["data"][0]["downVotes"]
            #     await app.sendFriendMessage(friend, msg.create(Plain("正在获取游戏数据...")))
            #     asyncio.sleep(5)
            #     await app.sendFriendMessage(friend, msg.create(Plain(f'游戏名字: {game_name}\n游戏ID: {game_id}\n游戏在线人数: {game_playing}\n游戏收藏量: {game_favorite}\n浏览量: {visits}\n喜欢人数: {vote_up}\n不喜欢人数: {vote_down}\n总投票人数: {vote_up + vote_down}')))
                

app.launch_blocking()