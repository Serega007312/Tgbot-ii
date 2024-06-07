from aiogram.fsm.state import State, StatesGroup


class States_p(StatesGroup):
    prompt = State()
    W_H = State()

class States_v(StatesGroup):
    prompt = State()
    W_H = State()

class States_pv(StatesGroup):
    picture = State()
