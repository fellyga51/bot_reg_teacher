import telebot;
from telebot import types
from app import database as db
# from setting import TG_TOKEN
# import os

# token = os.getenv("TOKEN")
bot = telebot.TeleBot('5866264930:AAFmDI5lRH38gO3oDndaB-aeFAsEoCRxzxs')


@bot.message_handler(commands=['start'])
def start(message):
    # проверка препода на наличие в БД
    # people_id =  message.chat.id
    # db.cursor.execute(f"SELECT user_id FROM teacher WHERE user_id = {people_id}")
    # data_id = db.cur.fetchone()

    # if data_id is None:
        teacher_id = message.chat.id
        username_teacher = message.from_user.username
        db.cur.execute('INSERT INTO teacher (teacher_id, username) VALUES (?, ?)', (teacher_id, username_teacher))
        db.commit()
        mess = f"Здравствуйте, <b>{message.from_user.first_name}</b>, сейчас вам надо пройти регистрацию, пропишите команду /reg"
        bot.send_message(message.chat.id, mess, parse_mode='html')

    # else:
    #     bot.send_message(message.chat.id, 'Извините, вы уже зарегестрированы!', message.text)
    

@bot.message_handler(commands=['reg'])
    
def start_reg(message):
    msg = bot.send_message(message.chat.id, 'Добро пожаловать в бот, вам щас нужно написать свое ФИО без ошибок')
    bot.register_next_step_handler(msg, save_name)

def save_name(message):
    user_name = message.text
    db.cur.execute('INSERT INTO teacher (user_name) VALUES (?)', (user_name))
    db.commit()
    bot.send_message(message.chat.id, 'Ваше ФИО было сохранено! Теперь напишите /choice')

@bot.message_handler(commands=['choice'])

def choice(message):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
     lesson1 = types.KeyboardButton('Математика')
     lesson2 = types.KeyboardButton('Информатика')
     lesson3 = types.KeyboardButton('Химия')
     lesson4 = types.KeyboardButton('Биология')     
     markup.add(lesson1, lesson2, lesson3, lesson4)
     bot.send_message(message.chat.id, 'Теперь вам нужно выбрать предметы по которым вы готовы работать!', reply_markup=markup)



#     markup_inline = types.InlineKeyboardMarkup(row_width=2)
#     item = types.InlineKeyboardButton(text='Химия', callback_data='test')
#     item1 = types.InlineKeyboardButton(text='Русский', callback_data='test1')
#     item2 = types.InlineKeyboardButton(text='Матан', callback_data='test2')
#     item3 = types.InlineKeyboardButton(text='Прочая шняга', callback_data='test3')
#     item4 = types.InlineKeyboardButton(text='Прочая шняга2', callback_data='test4')
#     item5 = types.InlineKeyboardButton(text='ещё что-то номер 2', callback_data='test5')
#     markup_inline.add(item, item1, item2, item3, item4, item5)
#     bot.send_message(message.chat.id, 'Выберите предмет',reply_markup=markup_inline)

# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
        
#     markup_inline = types.InlineKeyboardMarkup(row_width=3)
#     button = types.InlineKeyboardButton(text='1', callback_data='Class0')
#     button1 = types.InlineKeyboardButton(text='2', callback_data='Class1')
#     button2 = types.InlineKeyboardButton(text='3', callback_data='Class2')
#     button3 = types.InlineKeyboardButton(text='4', callback_data='Class3')
#     button4 = types.InlineKeyboardButton(text='5', callback_data='Class4')
#     button5 = types.InlineKeyboardButton(text='6', callback_data='Class5')
#     button6 = types.InlineKeyboardButton(text='7', callback_data='Class6')
#     button7 = types.InlineKeyboardButton(text='8', callback_data='Class7')
#     button8 = types.InlineKeyboardButton(text='9', callback_data='Class8')
#     button9 = types.InlineKeyboardButton(text='10', callback_data='Class9')
#     button10 = types.InlineKeyboardButton(text='11', callback_data='Class10')
#     markup_inline.add(button, button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)
#     bot.send_message(message.chat.id, 'Выберите класс',reply_markup=markup_inline)


bot.polling(none_stop=True)

# if __name__ == '__main__':
#     bot.polling(none_stop=True)