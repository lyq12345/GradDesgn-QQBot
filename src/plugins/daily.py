import requests
from nonebot import on_command, on_startswith
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment, Message
import random

love = on_startswith("每日一句", priority=3)


# love = on_keyword("土味情话",priority=3)

# 识别参数 并且给state 赋值


@love.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    soillove = await get_soil_sentence()
    await love.finish("???")


async def get_soil_sentence():
    url = 'http://open.iciba.com/dsapi/'
    res = requests.get(url)
    content_e = res.json()['content']
    content_c = res.json()['note']
    return [content_c, content_e]