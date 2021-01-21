from pathlib import Path

# import nonebot
from nonebot import get_driver,load_plugins,on_command,on_startswith
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event


card = on_startswith("打卡", rule=to_me(), priority=1)

@card.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    await card.finish("打卡啦")