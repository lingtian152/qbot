from graia.ariadne.app import Ariadne
from graia.ariadne.console.saya import ConsoleSchema
from graia.ariadne.message.parser.twilight import MatchResult, ParamMatch, Twilight
from graia.saya import Channel

channel = Channel.current()


@channel.use(ConsoleSchema([Twilight.from_command("发送群组消息 {id} {message}")]))
async def console_group_chat(app: Ariadne, id: MatchResult, message: MatchResult):
    group_id = id.result.asDisplay()
    await app.sendGroupMessage(int(group_id), message.result)

@channel.use(ConsoleSchema([Twilight.from_command("发送私聊消息 {id} {message}")]))
async def console_friend_chat(app: Ariadne, id: MatchResult, message: MatchResult):
    friend_id = id.result.asDisplay()
    await app.sendFriendMessage(int(friend_id), message.result)