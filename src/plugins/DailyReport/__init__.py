from pathlib import Path

# import nonebot
from nonebot import get_driver, load_plugins, on_command, on_startswith
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from .report import do_report
from .config import Config
from .data_source import userExist, getUserAccount, insertUser, updateUser
import os

global_config = get_driver().config
plugin_config = Config(**global_config.dict())

card = on_command("打卡", rule=to_me(), priority=2)


@card.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    qq_number = str(event.get_user_id())
    if userExist(qq_number):
        card_number, password = getUserAccount(qq_number)
        state["account"] = card_number + " " + password
    if args:
        state["account"] = args


@card.got("account", prompt="第一次使用，请按格式输入\"一卡通号 密码\"哦")
async def handle_account(bot: Bot, event: Event, state: T_State):
    qq_num = str(event.get_user_id())
    account = state["account"]
    account_list = account.split()
    if len(account_list) != 2:
        await card.reject("格式不正确哦，请按照\'一卡通号 密码\'重新输入")

    await card.send("处理中，请稍后...")
    username = account_list[0]
    password = account_list[1]

    if not userExist(qq_num):
        insertUser(qq_num, username, password)
        await card.send("您的信息已被录入，下次直接对我说\\打卡就好啦~")
    code = do_report(username, password)
    if code == 1:
        await card.finish("打卡成功！")
    else:
        await card.finish("打卡失败，请重新尝试")
