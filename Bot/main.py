import os, logging
from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from app.handlers import api

state_storage = StateMemoryStorage()
bot = TeleBot(os.getenv("BOT_TOKEN"), state_storage=state_storage, num_threads=5)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def register_handlers():
    bot.register_message_handler(api.start, commands=['start'], pass_bot=True)
    bot.register_message_handler(api.some_call_api_1, commands=['call1'], pass_bot=True)
    bot.register_message_handler(api.some_call_api_2, commands=['call2'], pass_bot=True)

register_handlers()
bot.infinity_polling()