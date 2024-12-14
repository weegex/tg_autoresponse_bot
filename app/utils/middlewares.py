from aiogram import BaseMiddleware, types
from setup import keys, bot
from utils import check_opening_hours


class NoAdminMiddleware(BaseMiddleware):
    async def __call__(self, handler, message: types.Message, data: str):
        if (message.from_user.id != keys.admin_id) and (message.from_user.id != bot.id):
            return await handler(message, data)
        

class BusinessMiddleware(BaseMiddleware):  
    async def __call__(self, handler, event: types.Message, data: str) -> any:
        admin_chat: types.Chat = await bot.get_chat(chat_id=keys.admin_id)

        if check_opening_hours(admin_chat.business_opening_hours):  
            try:
                if event.business_connection_id:
                    return await handler(event, data)
            except AttributeError:
                if event.message.business_connection_id:
                    return await handler(event, data)
