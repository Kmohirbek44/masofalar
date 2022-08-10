import requests
from aiogram import executor
from handlers import dp,bot
import config
from items import item
async def on(dp):
    await item.set(dp)
    await bot.send_message(chat_id=572054993,text="Qayum nima bo'ldi pastigingda pulin bormi")
    await bot.send_message(chat_id=452785654,text="Qayum nima bo'ldi pastigingda pulin bormi")
    requests.post(f"https://api.telegram.org/bot{config.token}/sendMessage?chat_id={config.ip}&text=Qayum nima bo'ldi pastigingda pulin bormi")
executor.start_polling(dp,on_startup=on)
