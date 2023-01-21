from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.console import Console  # 不是 from rich.console import Console 噢
from graia.ariadne.console.saya import ConsoleBehaviour
from graia.saya import Saya, Channel
from graia.broadcast import Broadcast
from graia.ariadne.console.saya import ConsoleBehaviour
from graia.ariadne.console import Console
from graia.ariadne.console.saya import ConsoleSchema
from graia.ariadne.message.parser.twilight import MatchResult, Twilight
from graia.ariadne.message.parser.base import MatchContent


import gc

channel = Channel.current()

bcc = create(Broadcast)
saya = create(Saya)

con = Console(broadcast=bcc, prompt="后台> ")
saya.install_behaviours(ConsoleBehaviour(con))


@channel.use(ConsoleSchema([MatchContent("gc")]))
async def garbage_Collection():
    try:
        gc.collect()
        print(f"Success gc {gc.get_threshold}")
    except Exception as Err:
        print(Err)


@channel.use(ConsoleSchema([MatchContent("stop")]))
async def bot_stop(app: Ariadne, console: Console):
    gc.collect()
    app.stop()
    console.stop()
