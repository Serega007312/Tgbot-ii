import time
import traceback
from main import dp, bot
from aiogram import types, F
from src.states.user import States_pv
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile




@dp.callback_query(F.data.startswith('picture_video'))
async def callback(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Пожалуйста пришлите картинку")
    await state.set_state(States_pv.picture)



@dp.message(States_pv.picture)
async def state2(message: types.Message, state: FSMContext):
    try:
        file_id = message.photo[-1].file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        userid = message.from_user.id
        await bot.download_file(file_path,f"src\\data\\photos\\{userid}.jpg")
        time.sleep(1)
        photo_path = f"src//data//photos//{userid}.jpg"
        photo = FSInputFile(photo_path,"photo")
        await bot.send_photo(userid,photo,caption="Вы прислали это фото")
        await state.clear()
    except Exception as e:
        traceback.print_exc()
        #except:
    #    print(Exception)
    #    await message.answer("Вы прислали что-то не то")
    #    await state.set_state(States_pv.picture)