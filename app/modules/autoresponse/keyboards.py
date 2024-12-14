from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def question() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Почитать отзывы",
                    callback_data="reviews"
                ),
                InlineKeyboardButton(
                    text="Подробнее о Вас",
                    callback_data="about"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Хочу узнать об услугах",
                    callback_data="services"
                )
            ]
            # [
            #     InlineKeyboardButton(
            #         text="Оставить заказ",
            #         callback_data="create_order"
            #     ),
            #     InlineKeyboardButton(
            #         text="Другой вопрос",
            #         callback_data="personal_question"
            #     )
            # ]
        ]
    )


def has_need() -> InlineKeyboardMarkup:
    return  InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Да",
                    callback_data="yes"
                ),
                InlineKeyboardButton(
                    text="Нет",
                    callback_data="no"
                )
            ]
        ]
    )
