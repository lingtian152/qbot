import asyncio
import pkgutil


# bot moduels
from creart import create
from graia.ariadne.app import Ariadne
from graia.broadcast import Broadcast
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from graia.ariadne.model import Friend
from graia.saya.builtins.broadcast import BroadcastBehaviour
from graia.saya import Saya
from graia.ariadne.console import Console

from graia.ariadne.connection.config import (
    HttpClientConfig,
    config,
)

loop = asyncio.new_event_loop()



broadcast = Broadcast(loop=loop)
app = Ariadne(
    connection=config(
        1330542948,  # 你的机器人的 qq 号
        "INITKEYxyFw6Q17",  # 填入你的 mirai-api-http 配置中的 verifyKey
        # 以下两行（不含注释）里的 host 参数的地址
        # 是你的 mirai-api-http 地址中的地址与端口
        # 他们默认为 "http://localhost:8080"
        # 如果你 mirai-api-http 的地址与端口也是 localhost:8080
        # 就可以删掉这两行，否则需要修改为 mirai-api-http 的地址与端口
        HttpClientConfig(host="http://localhost:8080"),
    ),
)
saya = create(Saya)
saya.install_behaviours(BroadcastBehaviour(broadcast))

con = Console(broadcast=broadcast, prompt="Console> ")


with saya.module_context():
    for module_info in pkgutil.iter_modules(["modules"]):
        saya.require(f"modules.{module_info.name}")


app.launch_blocking()