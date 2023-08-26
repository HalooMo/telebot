from aiogram.types import  InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, ReplyKeyboardMarkup

menu=[
    [KeyboardButton(text="Непрочитанные новости", callback_data="new_news"),
     KeyboardButton(text="Новости с сайта ", callback_data="news1")],
    [KeyboardButton(text="Новости с сайта", callback_data="news2"),
     KeyboardButton(text="Новости с сайта", callback_data="news3")],

]


menu_all = ReplyKeyboardMarkup(keyboard=menu, resize_keyboard=True)
menu_start = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Подписаться на стрим новостей", callback_data="start")]])
