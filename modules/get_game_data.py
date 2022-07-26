import asyncio
import re
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
    "游戏Id 接收器"

    def __init__(self, friend: Friend):
        self.friend = friend if isinstance(friend, int) else friend.id
    async def detected_event(self, friend: Friend, message: MessageChain):
        if self.friend == friend.id:
            return message


@channel.use(
    ListenerSchema(
        listening_events=[FriendMessage],
        decorators=[MatchContent("获取游戏数据")],
    )
)
async def get_game_data(app: Ariadne, friend: Friend):
        await app.send_friend_message(friend, MessageChain("请在10秒内发送游戏Id"))
        try:
            ret_msg = await inc.wait(SetuTagWaiter(friend), timeout=10)  # 强烈建议设置超时时间否则将可能会永远等待
        except asyncio.TimeoutError:
            await app.send_friend_message(friend, MessageChain("未收到游戏Id"))
        else:
            try:
                async with aiohttp.ClientSession() as session:
                    response = requests.get(f'https://api.roblox.com/universes/get-universe-containing-place?placeid={ret_msg}')
                    text = response.text
                    temp = re.findall(r'\d+', text)
                    universes_Id = list(map(int, temp))
                    game__web_api_url = f'https://games.roblox.com/v1/games?universeIds={universes_Id[0]}'
                    game_vote_url = f'https://games.roblox.com/v1/games/votes?universeIds={universes_Id[0]}'
                    game_Icon_url = f'https://thumbnails.roblox.com/v1/games/icons?universeIds={universes_Id[0]}&size=256x256&format=Png&isCircular=false'
                    game_place_url = f'https://www.roblox.com/games/{ret_msg}'
                    async with aiohttp.ClientSession() as session:
                        async with session.get(game__web_api_url) as r:
                            if r.status == 200:
                                    ret = await r.json()
                                    game_name = ret["data"][0]["name"]
                                    game_id = ret["data"][0]["id"]
                                    game_playing = ret["data"][0]["playing"]
                                    game_favorite = ret["data"][0]["favoritedCount"]
                                    visits = ret["data"][0]["visits"]
                                    last_time_updated = ret["data"][0]["updated"]
                                    creator_name = ret["data"][0]["creator"]["name"]
                            async with session.get(game_vote_url) as r:
                                if r.status == 200:
                                    ret = await r.json()
                                    vote_up = ret["data"][0]["upVotes"]
                                    vote_down = ret["data"][0]["downVotes"]
                            async with session.get(game_Icon_url) as r:
                                if r.status == 200:
                                    ret= await r.json()
                                    game_icon = ret["data"][0]["imageUrl"]
                            await app.send_friend_message(friend, MessageChain.create(Plain("正在获取游戏数据...")))
                            await asyncio.sleep(5)
                            await app.send_friend_message(friend, 
                            MessageChain.create(
                                Plain(f'游戏名字: {game_name}\n游戏ID: {game_id}\n开发者: {creator_name}\n游戏在线人数: {game_playing}\n游戏收藏量: {game_favorite}\n浏览量: {visits}\n最后一次更新时间: {last_time_updated}\n喜欢人数: {vote_up}\n不喜欢人数: {vote_down}\n总投票人数: {vote_up + vote_down}\n游戏链接: {game_place_url}\n游戏封面:'),
                                Image(url=game_icon)
                                )
                            )
            except Exception as Err:
                await app.send_friend_message(friend, MessageChain.create(Plain(f'错误 {Err}')))
