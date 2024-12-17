from aiogram import F, types, Router, Bot
from aiogram.enums import ParseMode, ChatMemberStatus
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardButton, Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.ext.asyncio import AsyncSession

from keyboard.inline import start_keybord_inline, return_keybord_inline, tops_5_website_keybord_inline

start_functions_private_router = Router()
# start_functions_private_router.message.filter(ChatTypeFilter(['private']))


@start_functions_private_router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer_photo(
        photo=types.FSInputFile("media/img.png"),
        caption= """👋 *Добро пожаловать в Baiastan Linguist!*  
Мы рады видеть вас здесь! ✨  
📚 В нашем сообществе вы найдёте советы, ресурсы и поддержку для изучения английского языка.  
Начните своё путешествие прямо сейчас и улучшайте свои навыки вместе с нами!  """,
        reply_markup=start_keybord_inline(),
    )


@start_functions_private_router.callback_query(F.data == "start")
async def start_handler_callback_query(callback_query: CallbackQuery):
    await callback_query.message.edit_caption(
        caption="""👋 *Добро пожаловать в Baiastan Linguist!*  
        Мы рады видеть вас здесь! ✨  
        📚 В нашем сообществе вы найдёте советы, ресурсы и поддержку для изучения английского языка.  
        Начните своё путешествие прямо сейчас и улучшайте свои навыки вместе с нами!  """,
        reply_markup=start_keybord_inline(),
    )


@start_functions_private_router.callback_query(F.data  == "about_me")
async def about_me_handler(callback_query: CallbackQuery):
    await callback_query.message.edit_caption(
        caption="""☺️Здравствуйте ☺️, я baiastan.linguist. Я профессиональный преподаватель иностранных языков по собственной методике.🥳 Я успешно обучил более тысячи студентов🥳. Если вы ищете наиболее подходящего преподавателя, то я тот, кто вам нужен.""",
        reply_markup = return_keybord_inline(),
    )


@start_functions_private_router.callback_query(F.data  == "study_tips")
async def study_tips_handler(callback_query: CallbackQuery):
    await callback_query.message.edit_caption(
        caption= """ *10 советов для изучения английского языка:*  
1. 🗣 **Практикуйтесь каждый день.** Каждый день старайтесь говорить или писать на английском языке.  
2. 📖 **Учите новые слова.** Выбирайте слово дня и используйте его в предложениях.  
3. 📚 **Читайте книги и статьи.** Начинайте с простых текстов и переходите к более сложным.  
4. 🎧 **Слушайте аудиоматериалы.** Слушайте подкасты, песни или аудиокниги.  
5. 🎥 **Смотрите фильмы и сериалы.** Используйте субтитры, чтобы понять значение слов.  
6. 💡 **Не бойтесь ошибаться.** Ошибки в речи — это естественная часть обучения.  
7. 📱 **Используйте мобильные приложения.** Такие приложения, как Duolingo или LingQ, помогут вам.  
8. ✍️ **Записывайте слова.** Создавайте предложения с новыми словами, чтобы запомнить их лучше.  
9. 👥 **Общайтесь с друзьями.** Найдите друзей, которые говорят на английском, или используйте платформы для обмена языками.  
10. 🎯 **Ставьте цели.** Например: выучить 50 новых слов за месяц или прочитать книгу.""",
        reply_markup = return_keybord_inline(),
        parse_mode=ParseMode.MARKDOWN

    )


@start_functions_private_router.callback_query(F.data  == "tops_5_website")
async def tops_10_website_handler(callback_query: CallbackQuery):
    await callback_query.message.edit_caption(
        caption= """
        5 сайта для изучения английского
        """,
        reply_markup = tops_5_website_keybord_inline(),
        parse_mode=ParseMode.MARKDOWN

    )
