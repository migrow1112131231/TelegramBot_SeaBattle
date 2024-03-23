from aiogram.filters.callback_data import CallbackData

class FieldCallbackFactory(CallbackData, prefix='user_field'):
    x:int
    y:int

