from setup import bot
from aiogram import Router, filters, types


router = Router()


@router.business_message(filters.CommandStart())
async def start_command(message: types.Message) -> None:
    pass
