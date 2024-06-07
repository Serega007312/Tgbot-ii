from aiogram.types import Message
from main import dp, bot
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hlink
from src.keyboards.inline import button1
from src.services.db.db_connection import select_user,insert_user


@dp.message(CommandStart())
async def command_start(message: Message, **kwargs):
    try:
        user_token = 10 #задел на проверку баланса

        userID = message.from_user.id
        #Проверяем подписан ли пользователь на канал
        user_channel_status = await bot.get_chat_member(chat_id='-4180701211', user_id=userID)
        user_in_bd = select_user(int(userID))
        if user_channel_status.status != 'left':
            if user_in_bd == None:
                insert_user(userID)
                await bot.send_message(message.chat.id, "Выберите действие.",
                                       reply_markup=button1.as_markup(resize_keyboard=True))
            else:
                if user_in_bd[0] <= 100:
                    await bot.send_message(message.chat.id, "Пополните балланс (Пока убрал кнопку пополнения....).",
                                           reply_markup=button1.as_markup(resize_keyboard=True))

            #if user_token > 0: #Задел под проверку баланса
            #    await bot.send_message(message.chat.id,"Выберите действие.",reply_markup=button1.as_markup(resize_keyboard = True))
            #else:
            #    await bot.send_message(message.chat.id,"Пополни баланс")
        else:
            text = hlink('Группа №1', 'https://t.me/+gNsVlxubZLViNzEy')
            await message.answer(f"Hello, {message.from_user.full_name}!\n"
                                 f"Для начала использования бота, подпишись на канал\n"
                                 f"{text}", parse_mode="HTML")
            print("он не подписан")


    except Exception:
        print(Exception)
