import os
import telebot
from dotenv import load_dotenv
from telegram import MessageEntity, ReplyKeyboardMarkup, ReplyMarkup

load_dotenv()

bot = telebot.TeleBot(os.environ['TOKEN'])

@bot.message_handler(commands=['start'])
def start(message):

    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('مأكولات الشام (Facebook)')
    keyboard.row('الطعام', 'أرقام الأفرع')
    keyboard.row('جديدنا', 'قوالب للمناسبات')
    keyboard.row('من نحن؟', 'إدارة وشكاوي')
    bot.send_message(message.chat.id, 'مرحبا بك في مأكولات الشام', reply_markup=keyboard)
    

@bot.message_handler(func = lambda m: True)
def send_text(message):

    if message.text.lower() == 'أرقام الأفرع':
        keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard2.row('مأكولات الشام _ شارع بغداد', 'مأكولات الشام _ عين الكرش')
        keyboard2.row('مأكولات الشام _ التضامن', 'مأكولات الشام _ السادات')
        keyboard2.row('مأكولات الشام _ كشكول', 'مأكولات الشام _ دويلعة')
        keyboard2.row('مأكولات الشام _ دويلعة قريبا', 'مأكولات الشام _ مليحة قريبا')
        keyboard2.row('مأكولات الشام _ عين ترما', 'مأكولات الشام _ الصناعة')
        keyboard2.row('رجوع',)
        bot.send_message(message.chat.id, 'أختار الفرع الذي تريده :', reply_markup=keyboard2)
    elif message.text == 'مأكولات الشام (Facebook)':
        who_i_am23 = ''' صفحتنا على ال(Facebook) لمتابعة كل جديد وعروضنا المغرية
         https://www.facebook.com/%D9%85%D8%A3%D9%83%D9%88%D9%84%D8%A7%D8%AA-%D8%A7%D9%84%D8%B4%D8%A7%D9%85-%D8%A7%D9%84%D9%81%D8%B1%D8%B9-%D8%A7%D9%84%D8%B1%D8%A6%D9%8A%D8%B3%D9%8A-654805151316348/?ti=as'''
        bot.send_message(message.chat.id, who_i_am23,)
    elif message.text.lower() == 'الطعام':
        keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard3.row('شاورما دجاج', 'فتايل مطفاية', 'فروج')
        keyboard3.row('سناك', 'وجبات سناك', 'مقبلات')
        keyboard3.row('وجبات مميزة')
        keyboard3.row('رجوع')
        bot.send_message(message.chat.id, 'أختار ما تريد :',  reply_markup=keyboard3)
    elif message.text.lower() == 'قوالب للمناسبات':
        keyboard11 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard11.row('قالب حسب الطلب', 'قالب 3 أشخاص')
        keyboard11.row('قالب 5 أشخاص', 'قالب 8 أشخاص')
        keyboard11.row('قالب 10 أشخاص', 'قالب 15 شخص')
        keyboard11.row('رجوع')
        Photo2 = 'Image/photo_2022-03-04_18-34-17.jpg'
        bot.send_photo(message.chat.id, photo=open(Photo2, 'rb'), reply_markup=keyboard11)
    elif message.text == 'جديدنا':
        keyboard12 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard12.row('وجبة عريس')
        keyboard12.row('رجوع')
        bot.send_message(message.chat.id, 'كل ما هو جديد تجده هنا : ', reply_markup = keyboard12)
    elif message.text.lower() == 'من نحن؟':
        Photo = 'Image/photo_2022-03-12_20-47-03.jpg'
        who_i_am = ''' تم تأسيس المطعم في عام 1989 من قبل الأخويين محمد أسعد اللحام ومحي الدين اللحام المشهوران أبو أسعد اللحام وأبو عمار اللحام تم تأسيس أول فرع في مدينة دمشق شارع بغداد حي عين الكرش'''
        bot.send_photo(message.chat.id, photo=open(Photo, 'rb'), caption=who_i_am)
    elif message.text == 'إدارة وشكاوي':
        who_i_am22 = '''للاستفسار عن أي ملاحظة أو شكوى التواصل على الرقم التالي :
        واتس أب : 0940840001
        الرقم المباشر : '''
        bot.send_message(message.chat.id, who_i_am22)
    elif message.text.lower() == 'رجوع':
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('مأكولات الشام عين الكرش (Facebook)')
        keyboard.row('الطعام', 'أرقام الأفرع')
        keyboard.row('جديدنا', 'قوالب للمناسبات')
        keyboard.row('من نحن؟', 'إدارة وشكاوي')
        bot.send_message(message.chat.id, ' القائمة الرئيسية :', reply_markup= keyboard)
    elif message.text.lower() == 'شاورما دجاج':
        keyboard4 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard4.row('سندويشة شاورما صغيرة', 'سندويشة شاورما كبيرة', 'وجبة شاورما عربي')
        keyboard4.row('سندويشة شاورما اكسترا', 'وجبة شاروما اكسترا', 'وجبة فرط')
        keyboard4.row('سندويشة سمون', 'سمون عربي', 'نصف كيلو')
        keyboard4.row('ماريا حد', 'ماريا قشقوان', 'ماريا خضار')
        keyboard4.row('ماريا الشام', 'بيتزا الشام', 'سندويش مع كبة')
        keyboard4.row('رجوع؟')
        bot.send_message(message.chat.id, ' الأصناف :', reply_markup= keyboard4)
    elif message.text.lower() == 'فتايل مطفاية':
        keyboard5 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard5.row('سندويشة وسط فتايل', 'سندويشة كبيرة فتايل', 'وجبة فتايل عربي')
        keyboard5.row('سندويشة سمون فتايل', ' فتايل نصف كيلو', 'وجبة فتايل فرط')
        keyboard5.row('عربي فتايل اكسترا', 'سندويشة فتايل اكسترا')
        keyboard5.row('سندويشة فتايل كبيرة مع بطاطا')
        keyboard5.row('رجوع؟')
        bot.send_message(message.chat.id, 'الأصناف : ', reply_markup=keyboard5)
    elif message.text.lower() == 'سناك':
        keyboard6 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard6.row('سندويشة اسكالوب', 'سندويشة كريسبي', 'سندويشة شيش طاووق')
        keyboard6.row('سندويشة همبرغر', 'سندويشة تشيز برغر', 'سندويشة فاهيتا')
        keyboard6.row('سندويشة فرانشيسكو', 'سندويشة مكسيكي', 'سندويشة ناغيت')
        keyboard6.row('سندويشة زنجر', 'سندويشة توستر', 'سندويشة ماليبو')
        keyboard6.row('سندويشة سوبريم', 'سندويشة  بولونيز', 'سندويشة ماكنوم')
        keyboard6.row('بطاط سياحي', 'بطاطا سمون', 'بطاطا تشيز', 'بطاطا الشام')
        keyboard6.row('رجوع؟')
        bot.send_message(message.chat.id, 'الأصناف :', reply_markup=keyboard6)
    elif message.text.lower() == 'وجبات سناك':
        keyboard7 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard7.row('وجبة كريسبي 5 قطع', 'وجبة اسكالوب 5 قطع')
        keyboard7.row('وجبة فرانشيسكو', 'وجبة مكسيكي', 'وجبة كرنشي')
        keyboard7.row('وجبة فاهينا', 'وجبة ناغيت', 'وجبة ماليبو')
        keyboard7.row('وجبة ماكنوم', 'وجبة توستر', 'وجبة همبرغر')
        keyboard7.row('وجبة شيش طاووق 3 سياخ', 'وجبة زنجر')
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
    elif message.text.lower() == 'وجبات مميزة':
        keyboard10 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard10.row('ماريا الشام', 'ماريا حد', 'ماريا خضار')
        keyboard10.row('ماريا قشقوان', 'كبة محشية شاورما', 'سندويشة كبة')
        keyboard10.row('سندويشة اكسترا', 'سندويشة فتايل اكسترا')
        keyboard10.row('وجبة عربي اكسترا', 'عربي فتايل اكسترا')
        keyboard10.row('قالب حسب الطلب', 'قالب 3 أشخاص', 'وجبة عريس')
        keyboard10.row('قالب 5 أشخاص', 'قالب 8 أشخاص', 'قالب 10 أشخاص')
        keyboard10.row('قالب 15 شخص')
        keyboard10.row('رجوع؟')
        bot.send_message(message.chat.id, 'الأصناف', reply_markup=keyboard10)
    elif message.text.lower() == 'رجوع؟':
        keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard3.row('شاورما دجاج', 'فتايل مطفاية', 'فروج')
        keyboard3.row('سناك', 'وجبات سناك', 'مقبلات')
        keyboard3.row('وجبات مميزة')
        keyboard3.row('رجوع')
        bot.send_message(message.chat.id, 'أختار ما تريد :',  reply_markup=keyboard3)
    elif message.text.lower() == 'وجبة عريس':
        who_i_am = '''الأسم : وجبة عريس
 الوصف : نصف فروج بروستد و3 قطع كريسبي و3 قطع اسكالوب وسيخ شيش ,
          وجبة شاورما و2 قطع فتايل وبطاطا وحبش مدخن وسلامي وجبنة شيدر وسلطة روسية وسلطة معكرونة وثوم
           أبيض وثوم حد مع فنجان حد ودبس و2 خبز سياحي و2 بيبسي كولا تنك
                                                                        '''
        Photo3 = 'Image/photo_2022-03-04_18-34-03.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo3, 'rb'), caption = who_i_am)
    elif message.text.lower() == 'سندويشة شاورما صغيرة':
        Photo4 = 'Image/photo_2022-03-04_18-33-57.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo4, 'rb'), caption ='''الأسم :سندويشة شاورما صغيرة
الوصف : قطعة من خبزة المشروح مع ثوم ومخلل وشرائح شاورما 
                                            ٍ''')
    elif message.text.lower() == 'فتايل نصف كيلو':
        who_i_am2 = '''الأسم : فتايل نصف كيلو
الوصف : نصف كيلو فتايل
 مطهي على الجريل مع صلصة وحمض
  مع علبتين ثوم وعلبة مخلل وفنجان حد وفنجان دبس'''
        Photo5 = 'Image/photo_2022-03-04_18-32-05.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo5, 'rb'), caption = who_i_am2)
    elif message.text.lower() == 'وجبة فتايل عربي':
        who_i_am3 = '''الأسم : وجبة فتايل
الوصف : سندويشة فتايل مقطعة
 مع 2 قطع محمرة وبطاطا وعلبة سرفيس'''
        Photo6 = 'Image/photo_2022-03-04_18-32-17.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo6, 'rb'), caption = who_i_am3)
    elif message.text.lower() == 'وجبة شاورما عربي':
        who_i_am4 = '''الأسم : وجبة شاورما عربي
الوصف : سندويشة شاورما كبيرة مقطعة
 مع 2 قطع محمرة وعلبة سرفيس'''
        Photo7 = 'Image/photo_2022-03-04_18-32-21.jpg'
        bot.send_photo(message.chat.id, photo=open(Photo7, 'rb'), caption=who_i_am4)
    elif message.text.lower() == 'وجبة فرط':
        who_i_am5 = '''الأسم : وجبة فرط
الوصف : وجبة شاورما 200 غرام مع بطاطا
و2 قطع محمرة و 2 علب ثوم
  وعلبة مخلل وفنجان حد وفنجان دبس'''
        Photo8 = 'Image/photo_2022-03-04_18-32-25.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo8, 'rb'), caption = who_i_am5)
    elif message.text.lower() == 'نصف كيلو':
        who_i_am6 = '''الأسم : نصف كيلو شاورما
الوصف : نصف كيلو من شرحات الشاورما مع 4 قطع محمرة
و2 علب ثوم وعلبة مخلل وفنجان حد وفنجان دبس'''
        Photo9 = 'Image/photo_2022-03-04_18-32-35.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo9, 'rb'), caption = who_i_am6)
    elif message.text.lower() == 'وجبة كريسبي 5 قطع':
        who_i_am7 = '''الأسم : وحبة كريسبي 5 قطع
الوصف : سمون كشف داخلها بطاطا  مع 5 قطع كريسبي
 فوقهاو علبة سلطة صغيرة وعلبة معكرونة صغيرة وفنجان صوص'''
        Photo10 = 'Image/photo_2022-03-04_18-32-39.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo10, 'rb'), caption = who_i_am7)
    elif message.text.lower()  == 'ماريا الشام':
        who_i_am8 = '''الأسم : ماريا الشام
الوصف : رغيفين من الخبز محتواهما
فطر وقشقوان وذرة وشرائح شاورما مع بطاطا
 وعلبة ثوم وعلبة مخلل وفنجان حد وفنجان دبس'''
        Photo11 = 'Image/photo_2022-03-04_18-33-02.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo11, 'rb'), caption = who_i_am8)
    elif message.text.lower() == 'وجبة شيش طاووق 3 سياخ':
        who_i_am9 = '''الأسم : وجبة شيش طاووق 3 سياخ
الوصف : سمون كشف داخلها بطاطا وفوقها
 3 سياخ شيش طاووق
 مع علبة سلطة وعلبة معكرونة وفنجان ثوم حد و2 ظرف كتشب'''
        Photo12 = 'Image/photo_2022-03-04_18-32-46.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo12, 'rb'), caption = who_i_am9)
    elif message.text.lower() == 'سندويشة اسكالوب':
        who_i_am10 = '''الأسم : سندويشة اسكالوب
الوصف : سمون مع ثوم وسلطة وكتشب
داخلها بطاطا وقطع كريسبي'''
        Photo13 = 'Image/photo_2022-03-04_18-32-42.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo13, 'rb'), caption = who_i_am10)
    elif message.text.lower() == 'سندويشة ناغيت':
        who_i_am11 = '''الأسم : سندويشة ناغيت
الوصف : سمون مع ثوم وسلطة
وبطاطا وخس وقطع الناغيت مع جبنة الشيدر'''
        Photo14 = 'Image/photo_2022-03-04_18-33-17.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo14, 'rb'), caption = who_i_am11)
    elif message.text == 'وجبة ناغيت':
        who_i_am12 = '''الأسم : وجبة ناغيت
الوصف : سمون كشف مع بطاطا وقطع الناغيت
مع جبنة الشيدر وعلبة سلطة
و 2 قطع خبز وفنجان ثوم حد وظرف كتشب'''
        Photo15 = 'Image/photo_2022-03-04_18-33-06.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo15, 'rb'), caption = who_i_am12)
    elif message.text == 'وجبة فتايل فرط':
        who_i_am13 = '''الأسم : وجبة فتايل فرط
الوصف : وجبة فتايل 200 غرام مع بطاطا
و2 قطع خبز وعلبة ثوم وعلبة مخلل
وفنجان حد وفنجان دبس'''
        Photo16 = 'Image/photo_2022-03-04_18-32-31.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo16, 'rb'), caption = who_i_am13)
    elif message.text == 'عربي فتايل اكسترا':
        who_i_am14 = '''الأسم : عربي فتايل اكسترا
الوصف : سندويشة فتايل اكسترا مقطعة مع بطاطا
و2 قطع محمرة و3 قطع فتايل وعلبة
سلطة وعلبة نص بنص وفنجان حد وفنجان دبس'''
        Photo17 = 'Image/photo_2022-03-04_18-32-50.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo17, 'rb'), caption = who_i_am14)
    elif message.text == 'سندويشة زنجر':
        who_i_am15 = '''الأسم : سندويشة زنجر
الوصف : سمون مع بطاطا قطع زنجر
مع حبش وجبنة الشيدر '''
        Photo18 = 'Image/photo_2022-03-04_18-33-30.jpg'
        bot.send_photo(message.chat.id,photo = open(Photo18, 'rb'), caption = who_i_am15)
    elif message.text == 'وجبة زنجر':
        who_i_am16 = '''الأسم : وجبة زنجر
الوصف : بطاطا وقطع الزنجر فوقها قطع الحبش
وجبنة الشيدر مع علبة سلطة و 2 قطع خبز وفنجان ثوم حد و 2 ظرف كتشب'''
        Photo19 = 'Image/photo_2022-03-04_18-33-10.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo19, 'rb'), caption = who_i_am16)
    elif message.text == 'سندويشة كريسبي':
        who_i_am17 = '''الأسم : سندويشة كريسبي
الوصف : سمون مع بطاطا
وسلطة وكتشب وثوم وخس وقطع الكريسبي'''
        Photo20 = 'Image/photo_2022-03-04_18-33-34.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo20, 'rb'), caption = who_i_am17)
    elif message.text == 'سندويشة توستر':
        who_i_am18 = '''الأسم : سندويشة توستر
الوصف : سمون مع بطاطا وخس وسلطة
وثوم وذرة مع حبش وجبنة الشيدر وقطع التوستر '''
        Photo21 = 'Image/photo_2022-03-04_18-33-13.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo21, 'rb'), caption = who_i_am18)
    elif message.text == 'قالب 5 أشخاص':
        who_i_am19 = '''الأسم : قالب 5 أشخاص
الوصف : 14 سندويشة شاورما
 مع بطاطا وسرفيس
'''
        Photo22 = 'Image/photo_2022-03-04_18-34-20.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo22, 'rb'), caption = who_i_am19)
    elif message.text == 'قالب 8 أشخاص':
        who_i_am20 = '''الأسم : قالب 8 أشخاص
الوصف : 20 سندويشة شاورما
مع بطاطا وسرفيس'''
        Photo23 = 'Image/photo_2022-03-04_18-34-48.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo23, 'rb'), caption = who_i_am20)
    elif message.text == 'قالب 10 أشخاص':
        who_i_am21 = '''الأسم : قالب 10 أشخاص'''
        Photo24 = 'Image/photo_2022-03-04_18-34-10.jpg'
        bot.send_photo(message.chat.id, photo = open(Photo24, 'rb'), caption = who_i_am21)
    elif message.text.lower() == 'مأكولات الشام _ عين الكرش':
        bot.send_location(message.chat.id, 33.520175,36.298052)
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (1)
مكان التواجد: شارع بغداد _ عين الكرش _ جانب المشفى العربي 
                        رقم التواصل : 2319300 \ 231324 \ 2319069 \ 0940840001''')

    elif message.text.lower() == 'مأكولات الشام _ شارع بغداد':
        bot.send_location(message.chat.id, 33.520175,36.298052)
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (2)
مكان التواجد: عين الكرش _ مقابل حلويات شيخ الحارة 
                        رقم التواصل : 2319300 \ 2313245 \ 2319069 \ 0940840001''')

    elif message.text.lower() == 'مأكولات الشام _ السادات':
        bot.send_location(message.chat.id, 33.51851,36.31033)
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (3)
مكان التواجد: شارع بغداد _ موقف السادات   
                        رقم التواصل : 4464440 \ 4444914 \ 4441155''')

    elif message.text.lower() == 'مأكولات الشام _ التضامن':
        bot.send_location(message.chat.id, 33.48146,36.30776)
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (4)
مكان التواجد: التضامن _ شارع نسرين _ مقابل مدرسة اسكندرون    
                        رقم التواصل : 6383333 \ 6382222''')

    elif message.text.lower() == 'مأكولات الشام _ دويلعة':
        bot.send_location(message.chat.id, 33.50412,36.31985)
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (5)
مكان التواجد: مفرق دويلعة _ بعد كنيسة مارلياس _ مقابل بن حسيب   
                        رقم التواصل :  4735558 \ 4735556''')

    elif message.text.lower() == 'مأكولات الشام _ كشكول':
        bot.send_location(message.chat.id, 33.49860,36.33405)
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (6)
مكان التواجد:  كشكول _ بناء الفارس   
                        رقم التواصل : 4736555 \ 4736444''')

    elif message.text.lower() == 'مأكولات الشام _ مليحة قريبا':
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (7)
مكان التواجد: المليحة _ قريبا   
                        ''')

    elif message.text.lower() == 'مأكولات الشام _ دويلعة قريبا':
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (8)
مكان التواجد: دويلعة _ قريبا   
                        ''')

    elif message.text.lower() == 'مأكولات الشام _ الصناعة':
        bot.send_location(message.chat.id, 33.50025,36.31063)
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (10)
مكان التواجد: الصناعة _ مقابل كراجات الست   
                        رقم التواصل : 5444156 \ 5444155 \ 5442236''')

    elif message.text.lower() == 'مأكولات الشام _ عين ترما':
        bot.send_location(message.chat.id, 33.51485,36.35198)
        bot.send_message(message.chat.id, '''الأسم: مأكولات الشام (11)
مكان التواجد: عين ترما _ ساحة الخزان   
                        رقم التواصل : 2319300 \ 2313245 \ 2319069 \ 0940840001''')


bot.polling()

