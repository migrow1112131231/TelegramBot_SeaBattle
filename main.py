import asyncio
from config import Config, add_config
from aiogram import Dispatcher, Bot
from handlers import users_handlers
import logging

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )
    logger.info('Starting bot')

    config = add_config()
    dp = Dispatcher()
    bot = Bot(token=config.telegram_bot.token, parse_mode='HTML')

    dp.include_router(router=users_handlers.router)
    # dp.startup.register(create_keyboard_menu)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
