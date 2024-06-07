from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import  InlineKeyboardButton


button1 = InlineKeyboardBuilder()
button1.add(InlineKeyboardButton(text="Текст в картинку", callback_data="text_picture")) \
    .add(InlineKeyboardButton(text="Текст в видео", callback_data="text_video")) \
    .add(InlineKeyboardButton(text="Картинку в видео", callback_data="picture_video"))


#Преобразование текста в картинку
button2 = InlineKeyboardBuilder()
button2.add(InlineKeyboardButton(text="4:3", callback_data="p_4:3")) \
    .add(InlineKeyboardButton(text="1:1", callback_data="p_1:1")) \
    .add(InlineKeyboardButton(text="3:4", callback_data="p_3:4"))


#преобразование текста в видео
button3 = InlineKeyboardBuilder()
button3.add(InlineKeyboardButton(text="4:3", callback_data="v_4:3")) \
    .add(InlineKeyboardButton(text="1:1", callback_data="v_1:1")) \
    .add(InlineKeyboardButton(text="3:4", callback_data="v_3:4"))