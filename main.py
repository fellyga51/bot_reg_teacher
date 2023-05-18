from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import Database
from config import TOKEN

bot = Bot(TOKEN)
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)

database = Database()

# Форма для пользователя (последовательное заполнение полей через handler)
class Form(StatesGroup):
    fullname = State()
    subject = State()
    grade = State()

@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    # проверка препода на наличие в БД
    user_id = message.from_user.id
    exist = database.check_teacher(user_id)
    print(exist)

    if not exist:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton("Зарегистироваться")
        markup.add(btn)
        await message.answer(f"Здравствуйте, {message.from_user.first_name}, сейчас вам надо пройти регистрацию", reply_markup=markup)

    else:
        markup = types.ReplyKeyboardRemove()
        await message.answer('Извините, вы уже зарегистрированы!', reply_markup=markup)

@dispatcher.message_handler(state=Form.fullname)
async def process_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text
    await Form.next()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Биология")
    btn2 = types.KeyboardButton("Математика")
    btn3 = types.KeyboardButton("Химия")
    btn4 = types.KeyboardButton("Информатика")
    markup.add(btn1, btn2, btn3, btn4)
    await message.answer("Отлично, укажите теперь предмет", reply_markup=markup)

@dispatcher.message_handler(state=Form.subject)
async def process_subject(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['subject'] = message.text
    await Form.next()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("5")
    btn2 = types.KeyboardButton("6")
    btn3 = types.KeyboardButton("7")
    btn4 = types.KeyboardButton("8")
    btn5 = types.KeyboardButton("9")
    btn6 = types.KeyboardButton("10")
    btn7 = types.KeyboardButton("11")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    await message.answer("Выберите класс", reply_markup=markup)

@dispatcher.message_handler(state=Form.grade)
async def process_grade(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['grade'] = message.text
        database.add_teacher(message.from_user.id, data["fullname"], data["subject"], data["grade"])
        markup = types.ReplyKeyboardRemove()
        await message.answer('Вы зарегистрированы как ' + data['fullname'] + "\nВыбранный предмет - " + data['subject'] + "\nКласс - " + data["grade"], reply_markup=markup)
    await state.finish()

@dispatcher.message_handler(content_types=["text"])
async def bot_message(message: types.Message):

    if message.text == "Зарегистироваться":
        await Form.fullname.set()
        markup = types.ReplyKeyboardRemove()
        await message.answer("Введите ФИО", reply_markup=markup)

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)