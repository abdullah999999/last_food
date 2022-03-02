import os
import telebot
from telegram import MessageEntity, ReplyKeyboardMarkup, ReplyMarkup
from telegram.ext import Updater


token = '5202377147:AAFc5vd0EaG_DlOgFca4iqXHqxuHqx1mRoI'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):

    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('الطعام', 'أرقام الأفرع')
    keyboard.row('جديدنا', 'قوالب للمناسبات')
    bot.send_message(message.chat.id, 'مرحبا بك في مأكولات الشام', reply_markup=keyboard)
    

@bot.message_handler(func = lambda m: True)
def send_text(message):

    if message.text.lower() == 'أرقام الأفرع':
        keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard2.row('مأكولات الشام(2)', 'مأكولات الشام(1)')
        keyboard2.row('مأكولات الشام(4)', 'مأكولات الشام(3)')
        keyboard2.row('مأكولات الشام(6)', 'مأكولات الشام(5)')
        keyboard2.row('مأكولات الشام(8)', 'مأكولات الشام(7)')
        keyboard2.row('مأكولات الشام(11)', 'مأكولات الشام(10)')
        keyboard2.row('رجوع',)
        bot.send_message(message.chat.id, 'أختار الفرع الذي تريده :', reply_markup=keyboard2)
    elif message.text.lower() == 'الطعام':
        keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard3.row('شاورما', 'فتايل', 'فروج')
        keyboard3.row('سناك', 'وجبات سناك', 'مقبلات')
        keyboard3.row('رجوع')
        bot.send_message(message.chat.id, 'أختار ما تريد :',  reply_markup=keyboard3)
    elif message.text.lower() == 'رجوع':
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('الطعام', 'أرقام الأفرع')
        keyboard.row('جديدنا', 'قوالب للمناسبات')
        bot.send_message(message.chat.id, ' القائمة الرئيسية :', reply_markup= keyboard)
    elif message.text.lower() == 'شاورما':
        keyboard4 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard4.row('سندويشة شاورما صغيرة', 'سندويشة شاورما عادية', 'سندويشة شاورما كبيرة')
        keyboard4.row('سندويشة شاورما اكسترا', 'وجبة شاورما عربي', 'وجبة شاروما اكسترا')
        keyboard4.row('سندويشة سمون', 'سمون عربي', 'وجبة شاورما 200 غرام')
        keyboard4.row('وجبة شاورما 250 غرام', 'وحبة شاورما 300 غرام', '2 وقية شاورما')
        keyboard4.row('نصف كيلو شاورما', '3 واق شاورما', '3.5 ,وقية شاورما')
        keyboard4.row('4 واق شاورما', '3 أرباع الكيلو شاورما', 'عربي اكسترا')
        keyboard4.row('ماريا حد', 'ماريا قشقوان', 'ماريا خضار')
        keyboard4.row('ماريا الشام', 'بيتزا الشام', 'سندويش مع كبة')
        keyboard4.row('رجوع؟')
        bot.send_message(message.chat.id, ' الأصناف :', reply_markup= keyboard4)
    elif message.text.lower() == 'فتايل':
        keyboard5 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard5.row('سندويشة وسط فتايل', 'سندويشة كبيرة فتايل', 'وجبة فتايل عربي')
        keyboard5.row('سندويشة سمون فتايل', 'وجبة فتايل نصف كيلو', 'وجبةفتايل فرط')
        keyboard5.row('سندويشة فتايل كبيرة مع بطاطا')
        keyboard5.row('رجوع؟')
        bot.send_message(message.chat.id, 'الأصناف : ', reply_markup=keyboard5)
    elif message.text.lower() == 'سناك':
        keyboard6 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard6.row('سندويشة اسكالوب', 'سندويشة كريسبي', 'سندويشة شيش')
        keyboard6.row('سندويشة همبرغر', 'سندويشة تشيز برغر', 'سندويشة فاهيتا')
        keyboard6.row('سندويشة فرانشيسكو', 'سندويشة مكسيكي', 'سندويشة ناغيت')
        keyboard6.row('سندويشة زنجر', 'سندويشة توستر', 'سندويشة ماليبو')
        keyboard6.row('سندويشة سوبريم', 'سندويشة  اسكالوب', 'سندويشة ماكنوم')
        keyboard6.row('بطاط سياحي', 'بطاطا سمون', 'بطاطا تشيز', 'بطاطا الشام')
        keyboard6.row('رجوع؟')
        bot.send_message(message.chat.id, 'الأصناف :', reply_markup=keyboard6)
    elif message.text.lower() == 'وجبات سناك':
        keyboard7 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard7.row('وجبة كريسبي 5 قطع', 'وجبة اسكالوب 3 قطع', 'وجبة كريسبي 3 قطع')
        keyboard7.row('وجبة اسكالوب 5 قطع', 'وجبة فرانشيسكو', 'وجبة مكسيكي')
        keyboard7.row('وجبة فاهينا', 'وجبة ناغيت', 'وجبة ماليبو')
        keyboard7.row('وجبة ماكنوم', 'وجبة توستر', 'وجبة همبرغر')
        keyboard7.row('رجوع؟')
        bot.send_message(message.chat.id, 'الأصناف :', reply_markup=keyboard7)
    elif message.text.lower()  == 'فروج':
        keyboard8 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard8.row('نصف فروج بروستد', 'فروج بروستد', 'نصف فروج مشوي')
        keyboard8.row('فروج مشوي', 'نصف فروج مسحب', 'فروج مسحب', 'وجبة بروستد')
        keyboard8.row('رجوع؟')
        bot.send_message(message.chat.id, 'الأصناف :', reply_markup=keyboard8)
    elif message.text.lower() == 'مقبلات':
        keyboard9 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard9.row('سلطة كول سلو', 'سلطة معكرونة', 'سلطة معكرونة هوت دوغ')
        keyboard9.row('سلطة سيزر', 'سلطة ذرة', 'علبة بطاطا')
        keyboard9.row('صحن بطاطا', 'علبة ثوم', 'علبة مخلل')
        keyboard9.row('نصف كيلو ثوم', 'خبزة محمرة', 'فنجان حد')
        keyboard9.row('فنجان دبس', 'خبز سياحي صغير', 'خبز سياحي كبير')
        keyboard9.row('رجوع؟')
        bot.send_message(message.chat.id, 'الأصناف :', reply_markup=keyboard9)
    elif message.text.lower() == 'رجوع؟':
        keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard3.row('شاورما', 'فتايل', 'فروج')
        keyboard3.row('سناك', 'وجبات سناك', 'مقبلات')
        keyboard3.row('رجوع')
        bot.send_message(message.chat.id, 'أختار ما تريد :',  reply_markup=keyboard3)
    elif message.text.lower() == 'سندويشة شاورما صغيرة':
        bot.send_photo(message.chat.id, 'https://imgur.com/gallery/2TAYV', '''الأسم: سندويشة شاورما صغيرة
مكونات: قطعة من الخبز المشروح مع الثوم والمخلل وشرائح الشاورما 
السعر: 2000
بعض الناس تسميها الفشكة ''')
    elif message.text.lower() == 'مأكولات الشام(1)':
        bot.send_location(message.chat.id, 33.520175,36.298052)
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (1)
مكان التواجد: شارع بغداد _ عين الكرش _ جانب المشفى العربي 
                        رقم التواصل : 2319300\ 2313245\ 2319069\ 0940840001''')

    elif message.text.lower() == 'مأكولات الشام(2)':
        bot.send_location(message.chat.id, 33.520175,36.298052)
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (2)
مكان التواجد: عين الكرش _ مقابل حلويات شيخ الحارة 
                        رقم التواصل : 2319300\ 2313245\ 2319069\ 0940840001''')

    elif message.text.lower() == 'مأكولات الشام(3)':
        bot.send_location(message.chat.id, 33.51851,36.31033)
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (3)
مكان التواجد: شارع بغداد _ موقف السادات   
                        رقم التواصل : 2319300\ 2313245\ 2319069\ 0940840001''')

    elif message.text.lower() == 'مأكولات الشام(4)':
        bot.send_location(message.chat.id, 33.48146,36.30776)
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (4)
مكان التواجد: التضامن _ شارع نسرين _ مقابل مدرسة اسكندرون    
                        رقم التواصل : 2319300\ 2313245\ 2319069\ 0940840001''')

    elif message.text.lower() == 'مأكولات الشام(5)':
        bot.send_location(message.chat.id, 33.50412,36.31985)
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (5)
مكان التواجد: مفرق دويلعة _ بعد كنيسة مارلياس _ مقابل بن حسيب   
                        رقم التواصل : 2319300\ 2313245\ 2319069\ 0940840001''')

    elif message.text.lower() == 'مأكولات الشام(6)':
        bot.send_location(message.chat.id, 33.49860,36.33405)
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (6)
مكان التواجد:  كشكول _ بناء الفارس   
                        رقم التواصل : 2319300\ 2313245\ 2319069\ 0940840001''')

    elif message.text.lower() == 'مأكولات الشام(7)':
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (7)
مكان التواجد: المليحة _ قريبا   
                        ''')

    elif message.text.lower() == 'مأكولات الشام(8)':
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (8)
مكان التواجد: دويلعة _ قريبا   
                        ''')

    elif message.text.lower() == 'مأكولات الشام(10)':
        bot.send_location(message.chat.id, 33.50025,36.31063)
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (10)
مكان التواجد: الصناعة _ مقابل كراجات الست   
                        رقم التواصل : 2319300\ 2313245\ 2319069\ 0940840001''')

    elif message.text.lower() == 'مأكولات الشام(11)':
        bot.send_location(message.chat.id, 33.51485,36.35198)
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (11)
مكان التواجد: عين ترما _ ساحة الخزان   
                        رقم التواصل : 2319300\ 2313245\ 2319069\ 0940840001''')



bot.polling()
