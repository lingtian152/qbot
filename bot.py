import asyncio



# bot moduels
from graia.ariadne.app import Ariadne
from graia.ariadne.model import MiraiSession
from graia.broadcast import Broadcast
from graia.saya.builtins.broadcast import BroadcastBehaviour
from graia.saya import Saya
from graia.ariadne.console import Console


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

con = Console(broadcast=broadcast, prompt="Console> ")

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
    saya.require("modules.console")
    saya.require("modules.backend")


app.launch_blocking()