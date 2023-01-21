import asyncio

# bot moduels
from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.connection.config import (
    HttpClientConfig,
    config,
)
from graia.ariadne.console import Console
from graia.broadcast import Broadcast
from graia.saya import Saya
from graia.saya.builtins.broadcast import BroadcastBehaviour
from graia.ariadne.console.saya import ConsoleBehaviour
from modules import loader

loop = asyncio.new_event_loop()

broadcast = Broadcast(loop=loop)


bcc = create(Broadcast)
saya = create(Saya)


app = Ariadne(
    connection=config(
        1330542948,  # 你的机器人的 qq 号
        "114514",  # 填入你的 mirai-api-http 配置中的 verifyKey
        # 以下两行（不含注释）里的 host 参数的地址
        # 是你的 mirai-api-http 地址中的地址与端口
        # 他们默认为 "http://localhost:8080"
        # 如果你 mirai-api-http 的地址与端口也是 localhost:8080
        # 就可以删掉这两行，否则需要修改为 mirai-api-http 的地址与端口
        HttpClientConfig(host="http://localhost:8080"),
    ),
)

con = Console(broadcast=bcc, prompt="后台> ")
saya.install_behaviours(ConsoleBehaviour(con))


loader

app.launch_blocking()
