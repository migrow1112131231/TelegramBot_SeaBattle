import logging
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from handbook import handbook
from database import users
from logic import reset_field
from keyboards import get_field_keyboard
from classes import FieldCallbackFactory

router = Router()

@router.message(F.text == '/start')
async def process_command_start(message: Message):
    await message.answer(
        text='<b>Это жирный текст</b>\n\
<i>Это прописной текст</i>\n\
<u>Это подчеркнутый текст</u>\n\
<del>Это перечеркнутый текст</del>\n\
<a href="https://vk.com/m_boltachev">Это ссылка</a>\n\
<tg-spoiler>Это тг спойлер</tg-spoiler>'
    )

@router.message(F.text == '/play')
async def process_command_play(message: Message):
    if not users.get(message.from_user.id):
        users[message.from_user.id] = {}
    reset_field(message.from_user.id)
    await message.answer(
        text=handbook['/play'],
        reply_markup=get_field_keyboard(message.from_user.id)
    )

@router.callback_query(FieldCallbackFactory.filter())
async def process_press_button(callback: CallbackQuery, callback_data: FieldCallbackFactory):
    field = users[callback.from_user.id]['field']
    ships = users[callback.from_user.id]['ships']
    if field[callback_data.x][callback_data.y] == 0 and \
    ships[callback_data.x][callback_data.y] == 0:
        answer = handbook['miss']
        field[callback_data.x][callback_data.y] = 1
    elif field[callback_data.x][callback_data.y] == 0 and \
    ships[callback_data.x][callback_data.y] == 1:
        answer = handbook['hit']
        field[callback_data.x][callback_data.y] = 2
    else:
        answer = handbook['used']
    try:
        await callback.message.edit_text(
            text=handbook['next_move'],
            reply_markup=get_field_keyboard(callback.from_user.id)
        )
    except:
        pass

    await callback.answer(
        text=answer,
        show_alert=False
    )

@router.message()
async def test(message: Message):
    logging.info('Хэндлер поймал апдейт')