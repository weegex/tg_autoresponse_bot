from setup import bot
from aiogram import Router, filters, types
from . import keyboards


router = Router()


@router.message(filters.CommandStart())
async def start_command(message: types.Message) -> None:
    await message.answer(
        "Привет! Я твой автоответчик, чем могу помочь?",
        reply_markup=keyboards.menu()
    )
