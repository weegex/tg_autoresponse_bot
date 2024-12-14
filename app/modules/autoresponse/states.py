from aiogram.fsm.state import StatesGroup, State


class QuestionStates(StatesGroup):
    question = State()
    services = State()
