from aiogram import Bot, Dispatcher

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    token: str


settings = Settings()


bot = Bot(
    token=settings.token
)

dp = Dispatcher()


async def run() -> None:
    await dp.start_polling(bot)
