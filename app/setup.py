from aiogram import Bot, Dispatcher

from pydantic_settings import BaseSettings, SettingsConfigDict


class Keys(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    token: str
    admin_id: int


keys = Keys()


bot = Bot(
    token=keys.token
)

dp = Dispatcher()


async def run() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
