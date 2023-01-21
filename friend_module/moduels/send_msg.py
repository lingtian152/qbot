import aiohttp
import requests


from graia.ariadne import Ariadne
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain, Image, FlashImage



class send_msg:
    async def send_friend_img(slef, app: Ariadne,type: str, img_type: str, url: str, target: str):
        if type == "requests":
            
            return
        elif type == "aiohttp":
            if img_type == "FlashImage":
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(url) as r:
                            ret = await r.json()
                            pic_url = ret["data"][0]["urls"]["original"]
                        async with session.get(pic_url) as r:
                            pic = await r.read()
                            await app.send_friend_message(target, MessageChain(FlashImage(data_bytes=pic)))
                except Exception as Err:
                    await app.send_friend_message(target, MessageChain(Plain(f'错误 {Err}')))
                    print(f'错误 {Err}')
            elif img_type == "Image":
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(url) as r:
                            ret = await r.json()
                            pic_url = ret["data"][0]["urls"]["original"]
                        async with session.get(pic_url) as r:
                            pic = await r.read()
                            await app.send_friend_message(target, MessageChain(Image(data_bytes=pic)))
                except Exception as Err:
                    await app.send_friend_message(target, MessageChain(Plain(f'错误 {Err}')))
                    print(f'错误 {Err}')
            return