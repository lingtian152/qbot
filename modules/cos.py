import random
import aiohttp
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import FriendMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import FlashImage, Plain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Friend
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

channel = Channel.current()


def number(x,y):
    num = random.randint(x,y)
    return num

@channel.use(
    ListenerSchema(
        listening_events=[FriendMessage],
        decorators=[MatchContent("cos图")],
    )
)
async def cos(app: Ariadne, friend: Friend):
    ero_url = "https://bbs-api.mihoyo.com/post/wapi/getForumPostList?forum_id=47&gids=5&is_good=false&is_hot=false&page_size=40&sort_type=1"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(ero_url) as r:
                ret = await r.json()
                pic_url = ret["data"]["list"][number(0,39)]["post"]["cover"]
            async with session.get(pic_url) as r:
                pic = await r.read()
                await app.send_friend_message(friend, MessageChain.create(
                    FlashImage(data_bytes=pic)
                    )
                    )
    except Exception as Err:
        await app.send_friend_message(friend, MessageChain.create(Plain(f'错误 {Err}')))
        print(f'错误 {Err}')
    