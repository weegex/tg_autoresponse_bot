from aiogram.filters import Filter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import Bot
from modules.autoresponse.states import QuestionStates


class CheckNoQuestionStates(Filter):
     async def __call__(self, message: Message, state: FSMContext) -> bool:
        current_state = await state.get_state()

        if not (current_state in QuestionStates):
            return True


class CheckQuestionStates(Filter):
     async def __call__(self, message: Message, state: FSMContext) -> bool:
        current_state = await state.get_state()

        if current_state in QuestionStates:
            return True
