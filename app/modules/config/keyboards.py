from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def menu() -> types.ReplyKeyboardMarkup:
    buttons = [
        [
            types.KeyboardButton(
                text="Настройки"
            ),
            types.KeyboardButton(
                text="Тексты"
            )
        ]
    ]

    return types.ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )
