from aiogram import types
from items.calc_distance import choose_shortest
from keybord import locations_buttons,default
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from loader import dp
@dp.message_handler(Command("distance"))
async def show_on_map(message:Message):
    await message.answer(f"Assalomu Alaykum va rahmatullohi va barakatuh {message.from_user.full_name}.\n"
                         f"pastigi tugmani bosing",
                         reply_markup=locations_buttons.keyboard
                         )

    @dp.message_handler(content_types=types.ContentTypes.LOCATION)
    async def location(message:Message):
        global choose
        location1=message.location
        choose=choose_shortest(location1)
        await message.answer('Universitetni tanlang',reply_markup=default.button)
        # @dp.message_handler(text='TATU')
        # async def TATU(message:Message):
        #
        #     c1=choose[0]
        #     text_format = "{shop_name}  gacha masofa {distance} km\n<a href='{url}'>Google</a>\n"
        #     text = "\n\n".join(
        #         [
        #             text_format.format(shop_name=shop_name, url=url, distance=distance)
        #             for shop_name, distance, url, shop_location in [c1]
        #
        #         ]
        #     )
        #
        #     await message.answer(f'{text} ',disable_web_page_preview=True,reply_markup=default.button)
        #
        @dp.message_handler(text='Eng_yaqin_filial')
        async def TDTU(message: Message):
            w = []
            print(choose)
            for a in choose:
                b=a[1]
                w.append(b)
            w.sort()
            for b in choose:
                q=w[0]
                if b[1]==q:
                    r=b
            c2 = r
            text_format = "{shop_name}. gacha masofa {distance} km\n<a href='{url}'>Google</a>\n"
            text = "\n\n".join(
                [
                    text_format.format(shop_name=shop_name, url=url, distance=distance)
                    for shop_name, distance, url, shop_location in [c2]

                ]
            )
            await message.answer(f'{text} ', disable_web_page_preview=True, reply_markup=default.button)

        # @dp.message_handler(text='Irrigatsiya')
        # async def West(message: Message):
        #     c3 = choose[2]
        #     text_format = "{shop_name}. gacha masofa {distance} km\n<a href='{url}'>Google</a>\n"
        #     text = "\n\n".join(
        #         [
        #             text_format.format(shop_name=shop_name, url=url, distance=distance)
        #             for shop_name, distance, url, shop_location in [c3]
        #
        #         ]
        #     )
        #     await message.answer(f'{text} ', disable_web_page_preview=True, reply_markup=default.button)
        #
        # @dp.message_handler(text='OZMU')
        # async def Ozmu(message: Message):
        #     c4 = choose[3]
        #     text_format = "{shop_name}. gacha masofa {distance} km\n<a href='{url}'>Google</a>\n"
        #     text = "\n\n".join(
        #         [
        #             text_format.format(shop_name=shop_name, url=url, distance=distance)
        #             for shop_name, distance, url, shop_location in [c4]
        #
        #         ]
        #     )
        #     await message.answer(f'{text} ', disable_web_page_preview=True, reply_markup=default.button)
        #
        #
        @dp.message_handler(text='Hamma_universitetlar_joylashuvi')
        async def Ozmu1(message: Message):
            c5 = choose
            text_format = "{shop_name}. gacha masofa {distance} km\n<a href='{url}'>Google</a>\n"
            text = "\n\n".join(
                [
                    text_format.format(shop_name=shop_name, url=url, distance=distance)
                    for shop_name, distance, url, shop_location in c5

                ]
            )
            await message.answer(f'{text} ', disable_web_page_preview=True, reply_markup=default.button)
