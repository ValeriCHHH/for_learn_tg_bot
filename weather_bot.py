import requests
from datetime import datetime
from config import tg_token_bot
from aiogram import Bot, types, Dispatcher


bot = Bot(token=tg_token_bot)
