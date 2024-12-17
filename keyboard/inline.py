from aiogram.types import InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_keybord_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Обо мне", callback_data="about_me"))
    keyboard.add(InlineKeyboardButton(text="10 советов для изучения английского", callback_data="study_tips"))
    keyboard.add(InlineKeyboardButton(text="5 сайта для изучения английского", callback_data="tops_5_website"))
    keyboard.add(InlineKeyboardButton(text="5 видео для изучения английского", callback_data="tops_5_video"))
    return keyboard.adjust(1).as_markup()


def return_keybord_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="🔙 Вернуться в главное меню", callback_data="start"))
    return keyboard.as_markup()


def tops_5_website_keybord_inline():
    keyboard = InlineKeyboardBuilder()

    # Добавление кнопок с сайтами для изучения английского
    keyboard.add(
        InlineKeyboardButton(text="Duolingo", url="https://www.duolingo.com/"),
        InlineKeyboardButton(text="BBC Learning English", url="https://www.bbc.co.uk/learningenglish/"),
    )
    keyboard.add(
        InlineKeyboardButton(text="Memrise", url="https://www.memrise.com/"),
        InlineKeyboardButton(text="Busuu", url="https://www.busuu.com/"),
    )
    keyboard.add(
        InlineKeyboardButton(text="English Club", url="https://www.englishclub.com/"),
    )

    # Кнопка для возвращения в главное меню
    keyboard.add(InlineKeyboardButton(text="🔙 Вернуться в главное меню", callback_data="start"))

    return keyboard.adjust(2,2,1).as_markup()


def tops_5_video_keybord_inline():
    keyboard = InlineKeyboardBuilder()

    # Добавление кнопок с видеоуроками для изучения английского на русском
    keyboard.add(
        InlineKeyboardButton(text="Английский с Дмитрием Петровым", url="https://youtu.be/mq0Bz4YR45k?si=MUgHofujvJNKz5X6"),
        InlineKeyboardButton(text="Английский для начинающих", url="https://www.youtube.com/watch?v=8vWbR9F6FvM"),
    )
    keyboard.add(
        InlineKeyboardButton(text="Easy English", url="https://www.youtube.com/watch?v=jsE5ZV9l2tY"),
        InlineKeyboardButton(text="Английский по-русски", url="https://www.youtube.com/watch?v=8rA9mlPXX6w"),
    )
    keyboard.add(
        InlineKeyboardButton(text="English with Natasha", url="https://www.youtube.com/watch?v=GvB7gY8T5xA"),
    )

    # Кнопка для возвращения в главное меню
    keyboard.add(InlineKeyboardButton(text="🔙 Вернуться в главное меню", callback_data="start"))

    return keyboard.adjust(2,2,1).as_markup()
