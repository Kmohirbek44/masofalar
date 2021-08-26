from aiogram import types
async def set(dp):
    await dp.bot.set_my_commands(
        [types.BotCommand("distance", "bu orqali siz botni ishga tushura olasiz")]

)