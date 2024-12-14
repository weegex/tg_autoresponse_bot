from aiogram import Router, types, Bot, F
from aiogram.fsm.context import FSMContext
from setup import keys, bot
from utils.filters import CheckNoQuestionStates, CheckQuestionStates
from modules.autoresponse import keyboards
from modules.autoresponse import states
from utils import middlewares


router = Router()


# Main handler
@router.business_message(CheckNoQuestionStates())
async def message_handler(message: types.Message, bot: Bot, state: FSMContext) -> None:
    await bot.send_message(
        business_connection_id=message.business_connection_id,
        chat_id=message.from_user.id,
        text="Здравствуйте, я Автоответчик 👋😊. Готов ответить на Ваши вопросы 😎! С какой целью обращаетесь 🤔?\n\n(Выберите вариант снизу)",
        reply_markup=keyboards.question()
    )

    await state.set_state(states.QuestionStates.question)
    await state.update_data(main_message=message)


# Bot need handler
async def has_need(business_connection_id: int, chat_id: int) -> None:
    await bot.send_message(
        business_connection_id=business_connection_id,
        chat_id=chat_id,
        text="Я ещё требуюсь?",
        reply_markup=keyboards.has_need()
    )


@router.callback_query(states.QuestionStates.question, F.data == "yes")
async def yes_need_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    main_message = data.get("main_message")

    await message_handler(main_message, bot, state)
    await callback.answer()


@router.callback_query(states.QuestionStates.question, F.data == "no")
async def no_need_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    await bot.send_message(
        business_connection_id=callback.message.business_connection_id,
        chat_id=callback.message.chat.id,
        text="Отлично, рад был помочь! Напишите, если понадоблюсь"
    )

    await callback.answer()
    await state.clear()


# Answer options for main handler

@router.callback_query(CheckQuestionStates(), F.data == "reviews")
async def reviews_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    await bot.send_message(
        business_connection_id=callback.message.business_connection_id,
        chat_id=callback.message.chat.id,
        text="Конечно. Отзывы Вы можете почитать в этом канале @weegex_reviews"
    )

    await callback.answer()
    await has_need(
        callback.message.business_connection_id,
        callback.message.chat.id
    )


@router.callback_query(CheckQuestionStates(), F.data == "about")
async def about_callback(callback: types.CallbackQuery) -> None:
    await bot.send_message(
        business_connection_id=callback.message.business_connection_id,
        chat_id=callback.message.chat.id,
        text="Меня зовут Weegex. Я являюсь Full-Stack разработчиком и готов разработать "
        + "любую фичу для Вас, но этим мои навыки не ограничиваются. Более подробно "
        + "можете узнать в канале [@weegex_info](https://t.me/weegex_info/4)",
        parse_mode="Markdown"
    )

    await callback.answer()
    await has_need(
        callback.message.business_connection_id,
        callback.message.chat.id
    )


@router.callback_query(CheckQuestionStates(), F.data == "services")
async def services_callback(callback: types.CallbackQuery) -> None:
    await bot.send_message(
        business_connection_id=callback.message.business_connection_id,
        chat_id=callback.message.chat.id,
        text="Все услуги и их цены я рассписал в этом канале [@weegex_info](https://t.me/weegex_info/6)",
        parse_mode="Markdown"
    )

    await callback.answer()
    await has_need(
        callback.message.business_connection_id,
        callback.message.chat.id
    )
