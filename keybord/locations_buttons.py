from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard=ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="location",
                       request_location=True

                       )
        ],

    ],
    resize_keyboard=True
)