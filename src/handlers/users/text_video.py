from main import dp, bot
from aiogram import types, F
from src.states.user import States_v
from aiogram.fsm.context import FSMContext
from src.keyboards.inline import button3



@dp.callback_query(F.data.startswith('text_video'))
async def callback(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выбирите соотношение сторон картинки", reply_markup=button3.as_markup(resize_keyboard = True))




@dp.callback_query(F.data.startswith("v_"))
async def callback(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    data = call.data.split("_")[-1]
    await state.update_data(W_H=data)
    await call.message.answer("Пожалуйста напишите свой промпт.")
    await state.set_state(States_v.prompt)

@dp.message(States_v.prompt)
async def state2(message: types.Message, state: FSMContext):
    await state.update_data(prompt=message.text)
    data = await state.get_data()
    await message.answer("Вы выбрали:\n"
                         F"Преобразование текста в видео\n"
                         f"Соотношение сторон : {data['W_H']}\n"
                         f"Текстовый промпт: {data['prompt']}")

    await state.clear()