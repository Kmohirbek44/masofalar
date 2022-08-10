import requests
from aiogram import executor
from handlers import dp,bot
import config
from items import item
async def on(dp):
    await item.set(dp)
    requests.post(f"https://api.telegram.org/bot{config.token}/sendMessage?chat_id={config.ip}&text=Qayum nima bo'ldi pastigingda pulin bormi")
executor.start_polling(dp,on_startup=on)
