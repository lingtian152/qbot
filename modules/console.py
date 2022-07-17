from graia.ariadne.app import Ariadne
from graia.ariadne.console.saya import ConsoleSchema
from graia.ariadne.message.parser.twilight import MatchResult, ParamMatch, Twilight
from graia.saya import Channel

channel = Channel.current()


@channel.use(ConsoleSchema([Twilight.from_command("stop")]))
async def stop():
    await Ariadne.stop()

@channel.use(ConsoleSchema([Twilight.from_command("停止")]))
async def stop():
    await Ariadne.stop()