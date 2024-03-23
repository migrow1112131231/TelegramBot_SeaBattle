from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from classes import FieldCallbackFactory
from handbook import handbook
from database import users
from config import add_config, Config

config = add_config()

def get_field_keyboard(user_id: int):
    kb_builder = InlineKeyboardBuilder()
    buttons = [InlineKeyboardButton(
        text=handbook[users[user_id]['field'][i][j]],
        callback_data=FieldCallbackFactory(x=i, y=j).pack()
    ) for i in range(config.sea_battle.size) for j in range(config.sea_battle.size)
    ]
    kb_builder.row(*buttons, width=8)
    return kb_builder.as_markup()