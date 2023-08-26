from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import utils
from aiogram import flags
import logging
from states import Gen
from aiogram.types import Message,CallbackQuery
import kb
import asyncio
from db import generate_news, get, set
import time

router = Router()


@router.message(Command("start"))
@flags.chat_action("type")
async def start(msg: Message, state: FSMContext):
    await msg.answer("Привет это новостной бот для ТРЕЙДЕРОВ", reply_markup=kb.menu_start)


@router.callback_query(F.data=="start")
async def start(clbck: CallbackQuery, state: FSMContext):
    time.sleep(1)
    await clbck.message.answer("Вы подписаны на стрим\n", reply_markup=kb.menu_all)
    time.sleep(2)
    await clbck.message.answer("ПРИЯТНОГО ПРОСМОТРА")
    while True:
        news_from_site = generate_news()
        news_from_db = get()
        print(news_from_db)
        for i in news_from_site:
            if i[0] in news_from_db:
                pass
            else:
                await clbck.message.answer("{0}  -  {1}\nINVESTING\n{2}".format(i[3], i[0], i[1]))
                set(i)
                time.sleep(180)






'''
@router.message(Gen.text_prompt)
@flags.chat_action("typing")
@flags.chat_action("upload_photo")
async def hello_handler(msg: Message, state: FSMContext):
    await msg.answer_photo(photo="https://yandex.ru/images/search?pos=0&from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FVKcSkbm48O0%2Fmaxresdefault.jpg&text=asyncio+python&rpt=simage&lr=10758", caption="Какая-то  фотка")
'''