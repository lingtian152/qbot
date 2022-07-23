import asyncio
import aiohttp
import requests



from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import FriendMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain, Image
from graia.ariadne.message.parser.base import MatchContent
from graia.broadcast.interrupt import InterruptControl
from graia.ariadne.model import Friend
from graia.saya import Channel, Saya
from graia.saya.builtins.broadcast import ListenerSchema
from graia.broadcast.interrupt.waiter import Waiter

saya = Saya.current()
channel = Channel.current()
inc = InterruptControl(saya.broadcast)  # type: ignore



class SetuTagWaiter(Waiter.create([FriendMessage])):
    "用户Id 接收器"

    def __init__(self, friend: Friend):
        self.friend = friend if isinstance(friend, int) else friend.id
    async def detected_event(self, friend: Friend, message: MessageChain):
        if self.friend == friend.id:
            return message

def onlinereturn(online):
    if str(online) == 'False':
        return "离线"
    elif str(online) == "True":
        return "在线"

def check_status(status):
    if str(status) == "Offline":
        return "离线"
    elif str(status) == "Online":
        return "在线"

def check_game_place(place):
    if str(place) == "None":
        return "用户不在游玩"

@channel.use(
    ListenerSchema(
        listening_events=[FriendMessage],
        decorators=[MatchContent("获取用户状态")],
    )
)
async def get_game_data(app: Ariadne, friend: Friend):
        await app.sendFriendMessage(friend, MessageChain("请在10秒内发送用户Id"))
        try:
            ret_msg = await inc.wait(SetuTagWaiter(friend), timeout=10)  # 强烈建议设置超时时间否则将可能会永远等待
        except asyncio.TimeoutError:
            await app.sendFriendMessage(friend, MessageChain("未收到用户Id"))
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.roblox.com/users/{ret_msg}/onlinestatus/') as r:
                    ret = await r.json()
                    Online = ret["IsOnline"]
                    LastLocation = ret["LastLocation"]
                    LastOnline = ret["LastOnline"]
                    game_PlaceId = ret["PlaceId"]

                async with session.get(f'https://api.roblox.com/users/{ret_msg}') as r:
                    ret = await r.json()
                    username = ret["Username"]
                    UserId = ret["id"]


            await app.send_friend_message(friend, MessageChain.create(Plain(
                f"用户名: {username}\n用户ID:{UserId}\n用户在线: {onlinereturn(Online)}\n最后状态: {check_status(LastLocation)}\n最后在线时间: {LastOnline}\n当前所在游戏Id: {check_game_place(game_PlaceId)}"
                )
                )
                )
