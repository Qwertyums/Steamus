from data_base.DATA import BOT_TOKEN
from aiogram import Bot, Dispatcher, F
from handlers import user_handlers

bot_token = BOT_TOKEN
bot = Bot(token=bot_token)
dp = Dispatcher()

dp.include_router(user_handlers.router)

if __name__ == '__main__':
    dp.run_polling(bot)
