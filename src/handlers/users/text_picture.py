import time

from main import dp, bot
from aiogram import types, F
from src.states.user import States_p
from aiogram.fsm.context import FSMContext
from src.keyboards.inline import button2
from src.services.client import prompt0, get_picture0, get
from aiogram.types import FSInputFile

@dp.callback_query(F.data.startswith('text_picture'))
async def callback(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выбирите соотношение сторон картинки", reply_markup=button2.as_markup(resize_keyboard = True))




@dp.callback_query(F.data.startswith("p_"))
async def callback(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    data = call.data.split("_")[-1]
    await state.update_data(W_H=data)
    await call.message.answer("Пожалуйста напишите свой промпт.")
    await state.set_state(States_p.prompt)

@dp.message(States_p.prompt)
async def state1(message: types.Message, state: FSMContext):
    await state.update_data(prompt=message.text)
    data = await state.get_data()
    await message.answer("Вы выбрали:\n"
                         F"Преобразование текста в картинку\n"
                         f"Соотношение сторон : {data['W_H']}\n"
                         f"Текстовый промпт: {data['prompt']}")
    import random
    import string

    def generate_string(length):
        all_symbols = string.ascii_uppercase + string.digits
        result = ''.join(random.choice(all_symbols) for _ in range(length))
        return result
    id = generate_string(8)
    await prompt0(data["prompt"],"",id)
    t = True
    while t ==True:
        status = await get(id)
        if status == 200:
            t = False
            await get_picture0(id)
    photo_path = f"src//data//photos//{id}_new.png"
    photo = FSInputFile(photo_path, "photo")
    userid = message.from_user.id
    await bot.send_photo(userid, photo, caption="вы сгенерировали это фото")

    await state.clear()