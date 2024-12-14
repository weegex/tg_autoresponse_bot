from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def menu() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(
        keyboard=[],
        
    )
    builder = ReplyKeyboardBuilder.from_markup(markup=markup)
    builder.button(
        text="Настройки"
    )
    builder.button(
        text="Тексты"
    )

    return builder.as_markup()
