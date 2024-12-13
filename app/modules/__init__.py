from aiogram import Router
from . import config, start


router = Router()


router.include_routers(
    config.router,
    start.router
)
