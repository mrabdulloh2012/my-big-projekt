from aiogram import Dispatcher, Bot , filters, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from aiogram.fsm.state import State , StatesGroup
from aiogram.fsm.context import FSMContext
import telebot

bot = Bot(token="6415541239:AAEowfmKX-6LVe97XU9K8UB50eUyLGefhTE")
dp = Dispatcher(bot = bot)


class Registration(StatesGroup):
    first_name = State()
    last_name = State()
    number = State()
    
class Cart(StatesGroup):
    cart_number = State()
    
class Cart_ru(StatesGroup):
    cart_number = State()
    
    
contact_button = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Kontakt jo'natish", request_contact=True)]
], resize_keyboard=True)

contact_button_rus = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Отправить контакт", request_contact=True)]
], resize_keyboard=True)
    
    
uzb_rus_keyboard_uzb = [
    [KeyboardButton(text='uzb'),KeyboardButton(text='rus')]
]

uzb_rus_button_uzb = ReplyKeyboardMarkup(keyboard=uzb_rus_keyboard_uzb,resize_keyboard=True)

uzb_rus_keyboard_rus = [
    [KeyboardButton(text='узб '),KeyboardButton(text='рус')]
]

uzb_rus_button_rus = ReplyKeyboardMarkup(keyboard=uzb_rus_keyboard_rus,resize_keyboard=True)


uzb_rus_keyboard_uzb_two = [
    [KeyboardButton(text='ozbek'),KeyboardButton(text='rus tili')]
]

uzb_rus_button_uzb_two = ReplyKeyboardMarkup(keyboard=uzb_rus_keyboard_uzb_two,resize_keyboard=True)

uzb_rus_keyboard_rus_two = [
    [KeyboardButton(text='узбекски'),KeyboardButton(text='русский')]
]

uzb_rus_button_rus_two = ReplyKeyboardMarkup(keyboard=uzb_rus_keyboard_rus_two,resize_keyboard=True)


big_menu_keyboard_uzb = [
    [KeyboardButton(text='menu 📖'),KeyboardButton(text='korzinka 🛒'),KeyboardButton(text='biz haqida')],
    [KeyboardButton(text='sizning malumotiz 🫵'),KeyboardButton(text='yordam 🆘'),KeyboardButton(text='tilni ozgartirish')]
]

big_menu_button_uzb = ReplyKeyboardMarkup(keyboard=big_menu_keyboard_uzb,resize_keyboard=True)


big_menu_keyboard_rus = [
    [KeyboardButton(text='меню 📖'),KeyboardButton(text='корзинка 🛒'),KeyboardButton(text='о нас')],
    [KeyboardButton(text='ваша информация 🫵'),KeyboardButton(text='поддержка 🆘'),KeyboardButton(text='поменять язык')]
]

big_menu_button_rus = ReplyKeyboardMarkup(keyboard=big_menu_keyboard_rus,resize_keyboard=True)



menu_keyboard_uzb = [
    [KeyboardButton(text='ovqat 🍔'),KeyboardButton(text='ichimlik 🍹')],
    [KeyboardButton(text='⬅️ ortga')]
]

menu_button_uzb = ReplyKeyboardMarkup(keyboard=menu_keyboard_uzb,resize_keyboard=True)



menu_keyboard_rus = [
    [KeyboardButton(text='еда 🍔'),KeyboardButton(text='напиток 🍹')],
    [KeyboardButton(text='⬅️ назад')]
]

menu_button_rus = ReplyKeyboardMarkup(keyboard=menu_keyboard_rus,resize_keyboard=True)
















menu_food_keyboard_uzb = [
    [KeyboardButton(text='lavash 🌯'),KeyboardButton(text='burger 🍔'),KeyboardButton(text='fri 🍟')],
    [KeyboardButton(text='xotdog 🌭'),KeyboardButton(text='sendvich 🥪'),KeyboardButton(text='qanotchalar 🍗')],
    [KeyboardButton(text='ortga ⬅️')]
]

menu_food_button_uzb = ReplyKeyboardMarkup(keyboard=menu_food_keyboard_uzb,resize_keyboard=True)

menu_food_keyboard_rus= [
    [KeyboardButton(text='лаваш 🌯'),KeyboardButton(text='бургер 🍔'),KeyboardButton(text='фри 🍟')],
    [KeyboardButton(text='хотдог 🌭'),KeyboardButton(text='сэндвич 🥪'),KeyboardButton(text='крылижки 🍗')],
    [KeyboardButton(text='назад ⬅️')]
]
    
menu_food_button_rus = ReplyKeyboardMarkup(keyboard=menu_food_keyboard_rus,resize_keyboard=True)    










keyboards_lavash_uzb = [
    [KeyboardButton(text="goshli lavash"),KeyboardButton(text="pishloqli lavash"),KeyboardButton(text="tovuqli lavash")],
    [KeyboardButton(text="ortga ⬅️")]
]

lavash_button_uzb = ReplyKeyboardMarkup(keyboard=keyboards_lavash_uzb,resize_keyboard=True)

keyboards_burger_uzb = [
    [KeyboardButton(text="standart burger"),KeyboardButton(text="hamburger"),KeyboardButton(text="chizburger")],
    [KeyboardButton(text="ortga ⬅️")]
]

burger_button_uzb = ReplyKeyboardMarkup(keyboard=keyboards_burger_uzb,resize_keyboard=True)

keyboards_fri_uzb = [
    [KeyboardButton(text="kichik fri"),KeyboardButton(text="ortacha fri"),KeyboardButton(text="katta fri")],
    [KeyboardButton(text="ortga ⬅️")]
]

fri_button_uzb = ReplyKeyboardMarkup(keyboard=keyboards_fri_uzb,resize_keyboard=True)

keyboards_xotdog_uzb = [
    [KeyboardButton(text="oddiy xotdog"),KeyboardButton(text="ikkitali xotdog")],
    [KeyboardButton(text="ortga ⬅️")]
]

xotdog_button_uzb = ReplyKeyboardMarkup(keyboard=keyboards_xotdog_uzb,resize_keyboard=True)

keyboards_sendvich_uzb = [
    [KeyboardButton(text="tovuqli sendvich"),KeyboardButton(text="mol goshli sendvich")],
    [KeyboardButton(text="ortga ⬅️")]
]

sendvich_button_uzb = ReplyKeyboardMarkup(keyboard=keyboards_sendvich_uzb,resize_keyboard=True)


keyboards_krilijki_uzb = [
    [KeyboardButton(text="achchiq krilijki"),KeyboardButton(text="krilijki")],
    [KeyboardButton(text="ortga ⬅️")]
]

krilijki_button_uzb = ReplyKeyboardMarkup(keyboard=keyboards_krilijki_uzb,resize_keyboard=True)












keyboards_yes_no_goshli_lavash_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="goshli lavash sotib olish",callback_data="goshli lavash sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 

keyboards_yes_no_pishloqli_lavash_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="pishloqli lavash sotib olish",callback_data="pishloqli lavash sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 

keyboards_yes_no_tovuqli_lavash_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="tovuqli lavash sotib olish",callback_data="tovuqli lavash sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 





keyboards_yes_no_standart_burger_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="standart burger sotib olish",callback_data="standart burger sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 

keyboards_yes_no_hamburger_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="hamburger sotib olish",callback_data="hamburger sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 

keyboards_yes_no_chizburger_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="chizburger sotib olish",callback_data="chizburger sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
])








keyboards_yes_no_fri_kichik_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="kichik fri sotib olish",callback_data="kichik fri sotib olish"),InlineKeyboardButton(text='imkor qilish',callback_data='imkor qilish')]
    
    
]) 

keyboards_yes_no_fri_ortacha_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ortacha fri sotib olish',callback_data='ortacha fri sotib olish'),InlineKeyboardButton(text='imkor qilish',callback_data='imkor qilish')]
    
    
]) 

keyboards_yes_no_fri_katta_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='katta fri sotib olish',callback_data='katta fri sotib olish'),InlineKeyboardButton(text='imkor qilish',callback_data='imkor qilish')]
    
]) 









keyboards_yes_no_xotdog_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="xotdog sotib olish",callback_data="xotdog sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 

keyboards_yes_no_xotdog_ikkitali_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="ikkitali xotdog sotib olish",callback_data="ikkitali xotdog sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 







keyboards_yes_no_sendvich_tovuqli_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="tovuqli sendvich sotib olish",callback_data="tovuqli sendvich sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
]) 

keyboards_yes_no_sendvich_mol_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="mol goshli sendvich sotib olish",callback_data="mol goshli sendvich sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
    
]) 






keyboards_yes_no_qanotchalar_achchiq_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="achchiq qanotchalar 3d sotib olish",callback_data="achchiq qanotchalar 3d sotib olish")],
    [InlineKeyboardButton(text="achchiq qanotchalar 5d sotib olish",callback_data="achchiq qanotchalar 5d sotib olish")],
    [InlineKeyboardButton(text="achchiq qanotchalar 7d sotib olish",callback_data="achchiq qanotchalar 7d sotib olish")],
    [InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 

keyboards_yes_no_qanotchalar_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="qanotchalar 3d sotib olish",callback_data="qanotchalar 3d sotib olish")],
    [InlineKeyboardButton(text="qanotchalar 5d sotib olish",callback_data="qanotchalar 5d sotib olish")],
    [InlineKeyboardButton(text="qanotchalar 7d sotib olish",callback_data="qanotchalar 7d sotib olish")],
    [InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 






keyboards_lavash_rus = [
    [KeyboardButton(text="мясной лаваш"),KeyboardButton(text="лаваш с сыром"),KeyboardButton(text="куриный лаваш")],
    [KeyboardButton(text="назад ⬅️")]
]

lavash_button_rus = ReplyKeyboardMarkup(keyboard=keyboards_lavash_rus,resize_keyboard=True)

keyboards_burger_rus = [
    [KeyboardButton(text="стандартный бургер"),KeyboardButton(text="гамбургер"),KeyboardButton(text="чизбургер")],
    [KeyboardButton(text="назад ⬅️")]
]

burger_button_rus = ReplyKeyboardMarkup(keyboard=keyboards_burger_rus,resize_keyboard=True)

keyboards_fri_rus = [
    [KeyboardButton(text="картошка фри"),KeyboardButton(text="средний картофель фри"),KeyboardButton(text="большая картошка фри")],
    [KeyboardButton(text="назад ⬅️")]
]

fri_button_rus = ReplyKeyboardMarkup(keyboard=keyboards_fri_rus,resize_keyboard=True)

keyboards_xotdog_rus = [
    [KeyboardButton(text="простой хот-дог"),KeyboardButton(text="двойной хот-дог")],
    [KeyboardButton(text="назад ⬅️")]
]

xotdog_button_rus = ReplyKeyboardMarkup(keyboard=keyboards_xotdog_rus,resize_keyboard=True)

keyboards_sendvich_rus = [
    [KeyboardButton(text="куриный сендвич"),KeyboardButton(text="сэндвич с говядиной")],
    [KeyboardButton(text="назад ⬅️")]
]

sendvich_button_rus = ReplyKeyboardMarkup(keyboard=keyboards_sendvich_rus,resize_keyboard=True)


keyboards_krilijki_rus = [
    [KeyboardButton(text="острые крылижки"),KeyboardButton(text="крылижки")],
    [KeyboardButton(text="назад ⬅️")]
]

krilijki_button_rus = ReplyKeyboardMarkup(keyboard=keyboards_krilijki_rus,resize_keyboard=True)












keyboards_yes_no_goshli_lavash_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="купить мясной лаваш",callback_data="купить мясной лаваш"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
]) 

keyboards_yes_no_pishloqli_lavash_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="купить лаваш с сыром",callback_data="купить лаваш с сыромh"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
]) 

keyboards_yes_no_tovuqli_lavash_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="купить куриный лаваш",callback_data="купить куриный лаваш"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
]) 





keyboards_yes_no_standart_burger_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="купи стандартный бургер",callback_data="купи стандартный бургер"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
]) 

keyboards_yes_no_hamburger_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="купить гамбургер",callback_data="купить гамбургер"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
]) 

keyboards_yes_no_chizburger_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="покупка чизбургера",callback_data="покупка чизбургера"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
])








keyboards_yes_no_fri_kichik_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="купить картошку фри",callback_data="купить картошку фри"),InlineKeyboardButton(text='отрицать',callback_data='отрицать')]
    
    
]) 

keyboards_yes_no_fri_ortacha_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='покупаю средний картофель фри',callback_data='покупаю средний картофель фри'),InlineKeyboardButton(text='отрицать',callback_data='отрицать')]
    
    
]) 

keyboards_yes_no_fri_katta_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='покупаю большую картошку фри',callback_data='покупаю большую картошку фри'),InlineKeyboardButton(text='отрицать',callback_data='отрицать')]
    
]) 









keyboards_yes_no_xotdog_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="покупка хот-дога",callback_data="xotdog sotib olish"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
]) 

keyboards_yes_no_xotdog_ikkitali_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="покупка двойных хот-догов",callback_data="покупка двойных хот-догов"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
]) 







keyboards_yes_no_sendvich_tovuqli_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="купить сэндвич с курицей",callback_data="купить сэндвич с курицей"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
]) 

keyboards_yes_no_sendvich_mol_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="покупка сэндвича с говядиной",callback_data="покупка сэндвича с говядиной"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
    
]) 






keyboards_yes_no_qanotchalar_achchiq_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купите 3 острых крылышка.",callback_data="Купите 3 острых крылышка.")],
    [InlineKeyboardButton(text="Купите 5 острых крылышка.",callback_data="Купите 5 острых крылышка.")],
    [InlineKeyboardButton(text="Купите 7 острых крылышка.",callback_data="Купите 7 острых крылышка.")],
    [InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
]) 

keyboards_yes_no_qanotchalar_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купите 3 крылышка.",callback_data="Купите 3 крылышка.")],
    [InlineKeyboardButton(text="Купите 5 крылышка.",callback_data="Купите 5 крылышка.")],
    [InlineKeyboardButton(text="Купите 7 крылышка.",callback_data="Купите 7 крылышка.")],
    [InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
]) 






menu_drink_keyboard_uzb = [
    [KeyboardButton(text='cola'),KeyboardButton(text='royal'),KeyboardButton(text='fanta')],
    [KeyboardButton(text='sprite'),KeyboardButton(text='moxito'),KeyboardButton(text='pepsi')],
    [KeyboardButton(text='ortga ⬅️')]
]

menu_drink_button_uzb = ReplyKeyboardMarkup(keyboard=menu_drink_keyboard_uzb,resize_keyboard=True)

menu_drink_keyboard_rus= [
    [KeyboardButton(text='кола'),KeyboardButton(text='роял'),KeyboardButton(text='фанта')],
    [KeyboardButton(text='спрайт'),KeyboardButton(text='мохито'),KeyboardButton(text='пепси')],
    [KeyboardButton(text='назад ⬅️')]
]
    
menu_drink_button_rus = ReplyKeyboardMarkup(keyboard=menu_drink_keyboard_rus,resize_keyboard=True)    




keyboards_yes_no_cola_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="cola sotib olish",callback_data="cola sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 

keyboards_yes_no_royal_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="royal sotib olish",callback_data="royal sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 

keyboards_yes_no_fanta_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="fanta sotib olish",callback_data="fanta sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 

keyboards_yes_no_sprite_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="sprite sotib olish",callback_data="sprite sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 

keyboards_yes_no_moxito_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="moxito sotib olish",callback_data="moxito sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 

keyboards_yes_no_pepsi_uzb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="pepsi sotib olish",callback_data="pepsi sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 







keyboards_yes_no_cola_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="купить колу",callback_data="купить колу"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
]) 

keyboards_yes_no_royal_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="купить роял",callback_data="купить роял"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
]) 

keyboards_yes_no_fanta_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="купить фанту",callback_data="купить фанту"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
]) 

keyboards_yes_no_sprite_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="купить спрайт",callback_data="купить спрайт"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
]) 

keyboards_yes_no_moxito_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="купить мохито",callback_data="купить мохито"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
]) 

keyboards_yes_no_pepsi_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="купить пепси",callback_data="купить пепси"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
]) 



menu_korzinka_keyboard_uzb = [
    [KeyboardButton(text='barcha mahsulotni sotib olish'),KeyboardButton(text='barcha mahsulotlarni olib tashlash'),KeyboardButton(text='yana mahsulot qoshish')],
    [KeyboardButton(text='ortga ⬅️')]
]

menu_korzinka_button_uzb = ReplyKeyboardMarkup(keyboard=menu_korzinka_keyboard_uzb,resize_keyboard=True)


menu_korzinka_keyboard_rus = [
    [KeyboardButton(text='купить все товары'),KeyboardButton(text='удалить все товары'),KeyboardButton(text='добавить больше продуктов')],
    [KeyboardButton(text='назад ⬅️')]
]

menu_korzinka_button_rus = ReplyKeyboardMarkup(keyboard=menu_korzinka_keyboard_rus,resize_keyboard=True)




cart_keyboard_uzb = [
    [KeyboardButton(text='Humo'),KeyboardButton(text='Uzcard')]
]

cart_button_uzb = ReplyKeyboardMarkup(keyboard=cart_keyboard_uzb,resize_keyboard=True)

cart_keyboard_rus = [
    [KeyboardButton(text='Хумо'),KeyboardButton(text='Узкард')]
]

cart_button_rus = ReplyKeyboardMarkup(keyboard=cart_keyboard_rus,resize_keyboard=True)













    
@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    await message.answer('tilni tanlang',reply_markup=uzb_rus_button_uzb)
    
    
    

def regestratsiya_uzb():
    @dp.message(Registration.first_name)
    async def first_name_function(message: types.Message, state: FSMContext):
        await state.update_data(first_name=message.text)
        await state.set_state(Registration.last_name)
        await message.answer("Yaxshi endi familya kiriting: ")


    @dp.message(Registration.last_name)
    async def last_name_function(message: types.Message, state: FSMContext):
        await state.update_data(last_name=message.text)
        await state.set_state(Registration.number)
        await message.answer("Yaxshi endi nomerizni kiriting: ", reply_markup=contact_button)


    @dp.message(Registration.number)
    async def phone_function(message: types.Message, state: FSMContext):
        await state.update_data(number=message.contact.phone_number)
        data = await state.get_data()
        await message.answer(f"ismingiz: {data['first_name']}\nfamilyangiz: {data['last_name']}\nnomeringiz: {data['number']}", reply_markup=types.ReplyKeyboardRemove())
        await state.clear()
        await message.answer('menu',reply_markup=big_menu_button_uzb)
    
    
    
def regestratsiya_rus():    


    @dp.message(Registration.first_name)
    async def first_name_function(message: types.Message, state: FSMContext):
        await state.update_data(first_name=message.text)
        await state.set_state(Registration.last_name)
        await message.answer("Хорошо, теперь введите свою фамилию:")


    @dp.message(Registration.last_name)
    async def last_name_function(message: types.Message, state: FSMContext):
        await state.update_data(last_name=message.text)
        await state.set_state(Registration.number)
        await message.answer("Хорошо, теперь введите номер:", reply_markup=contact_button_rus)


    @dp.message(Registration.number)
    async def phone_function(message: types.Message, state: FSMContext):
        await state.update_data(number=message.contact.phone_number)
        data = await state.get_data()
        await message.answer(f"имя:{data['first_name']}\nфамилия: {data['last_name']}\nномер: {data['number']}", reply_markup=types.ReplyKeyboardRemove())
        await state.clear()
        await message.answer('меню',reply_markup=big_menu_button_rus)
 
 
    
@dp.message(F.text == "menu 📖")
async def menu_uzb(message: types.Message):
    await message.answer('menu',reply_markup=menu_button_uzb)   



@dp.message(F.text == "меню 📖")
async def menu_rus(message: types.Message):
    await message.answer('меню',reply_markup=menu_button_rus)    
    
@dp.message(F.text == "ovqat 🍔")
async def menu_food_uzb(message: types.Message):
    await message.answer('ovqat',reply_markup=menu_food_button_uzb)
                         
@dp.message(F.text == "еда 🍔")
async def menu_food_rus(message: types.Message):
    await message.answer('еда',reply_markup=menu_food_button_rus)

korzinka_uzb_list = []
korzinka_rus_list = []


korzinka_uzb_list.clear()
korzinka_rus_list.clear()



@dp.message(F.text == "lavash 🌯")
async def lavash(message: types.Message):
    await message.answer('lavash',reply_markup=lavash_button_uzb)   
    
@dp.message(F.text == "burger 🍔")
async def burger(message: types.Message):
    await message.answer('burger',reply_markup=burger_button_uzb)   
    
@dp.message(F.text == "fri 🍟")
async def fri(message: types.Message):
    await message.answer('fri',reply_markup=fri_button_uzb)   
    
@dp.message(F.text == "xotdog 🌭")
async def xotdog(message: types.Message):
    await message.answer('xotdog',reply_markup=xotdog_button_uzb)   
    
@dp.message(F.text == "sendvich 🥪")
async def sendvich(message: types.Message):
    await message.answer('sendvich',reply_markup=sendvich_button_uzb)   
    
@dp.message(F.text == "qanotchalar 🍗")
async def qanotchalar(message: types.Message):
    await message.answer('qanotchalar',reply_markup=krilijki_button_uzb)   




@dp.message(F.text == "goshli lavash")
async def lavash_oddiy_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4fikHKsb7lpQ8_BJVuUfwHp021iI7vLruxA&s",caption='goshli lavash',reply_markup=keyboards_yes_no_goshli_lavash_uzb)         
    
@dp.message(F.text == "pishloqli lavash")
async def lavash_pishloq_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROweC0I1Y3A70ccFprzK00dTllOeEXnWL79g&s",caption='pishloqli lavash',reply_markup=keyboards_yes_no_pishloqli_lavash_uzb)                   
    
@dp.message(F.text == "tovuqli lavash")
async def lavash_tovuqli_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUKVp7dSWxB9r6buzP62A5I7SZlhKyQiDkWA&s",caption='tovuqli lavash',reply_markup=keyboards_yes_no_tovuqli_lavash_uzb)         
    
    
    
    

@dp.message(F.text == "standart burger")
async def standart_burger_function_uzb(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPz-LNhaGDVkpfS7dB3OQhALi5ZsvWoxrpBg&s",caption='burger',reply_markup=keyboards_yes_no_standart_burger_uzb)     
    
@dp.message(F.text == "hamburger")
async def hamburger_function_uzb(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQElpavZnBQwnBjLid9VidYUzse-VnPuL-Wrg&s",caption='hamburger',reply_markup=keyboards_yes_no_hamburger_uzb)     
    
@dp.message(F.text == "chizburger")
async def chizburger_function_uzb(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXIkusJx-NqQm7iOQCWvHiRNQoqHmGnr6mzQ&s",caption='chizburger',reply_markup=keyboards_yes_no_chizburger_uzb)         
      
      
      
      
      
@dp.message(F.text == "kichik fri")
async def fri_kichik_function_uzb(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=c22a4313664f18815aa232b2f13e2715acd57bdd-12363187-images-thumbs&n=13",caption='kichik fri',reply_markup=keyboards_yes_no_fri_kichik_uzb)
    
@dp.message(F.text == "ortacha fri")
async def fri_ortacha_function_uzb(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=e22bfebe3ee1d21c370386f29dfc0ebe36d708b2-5338563-images-thumbs&n=13",caption='ortacha fri',reply_markup=keyboards_yes_no_fri_ortacha_uzb)
    
@dp.message(F.text == "katta fri")
async def fri_katta_function_uzb(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=f7222539321bdd8a239042ae872adf24058568bd-12319966-images-thumbs&n=13",caption='katta fri',reply_markup=keyboards_yes_no_fri_katta_uzb)
 
 
 
 

 

 
@dp.message(F.text == "oddiy xotdog")
async def oddiy_xotdog_function_uzb(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=1a5a2698b55bf34098d6ebac3248d80cbe34da8ae0ea16ab-12421362-images-thumbs&n=13",caption='xotdog',reply_markup=keyboards_yes_no_xotdog_uzb)
    
@dp.message(F.text == "ikkitali xotdog")
async def ikkitali_xotdog_function_uzb(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=cdc7d1c610cd1327d130b35a61d93c554acf07b7942c0bf0-10869598-images-thumbs&n=13",caption='ikkitali xotdog',reply_markup=keyboards_yes_no_xotdog_ikkitali_uzb)
    
 
 
 
    
@dp.message(F.text == "tovuqli sendvich")
async def tovuzli_sendvich_function_uzb(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=2626e4e1e72b2d1140d96165d5c4c70290bc6276-6873210-images-thumbs&n=13",caption='tovuqli sendvich',reply_markup=keyboards_yes_no_sendvich_tovuqli_uzb)
    
@dp.message(F.text == "mol goshli sendvich")
async def mol_sendvich_function_uzb(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=62079d540c4503c5ae11a0624a06bec10b8adae9-8819379-images-thumbs&n=13",caption='mol goshli sendvich',reply_markup=keyboards_yes_no_sendvich_mol_uzb)
    
    
    
    
    
@dp.message(F.text == "achchiq krilijki")
async def krilijki_achchiq_function_uzb(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=223dff190d8a996ace42e826b0a8fdfe52d72091a87c8294-12936542-images-thumbs&n=13",caption='achchiq krilijki',reply_markup=keyboards_yes_no_qanotchalar_achchiq_uzb)
    
@dp.message(F.text == "krilijki")
async def krilijki_function_uzb(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=223dff190d8a996ace42e826b0a8fdfe52d72091a87c8294-12936542-images-thumbs&n=13",caption='krilijki',reply_markup=keyboards_yes_no_qanotchalar_uzb)











@dp.callback_query(F.data == 'goshli lavash sotib olish')
async def goshli_lavash_sotib_olish_function(callback: types.CallbackQuery):
    korzinka_uzb_list.append('goshli lavash')
    korzinka_rus_list.append('мясной лаваш')
    await callback.answer('siz goshli lavash sotib oldis') 
    
@dp.callback_query(F.data == "pishloqli lavash sotib olish")
async def buy_pishloqli_lavash(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('pishloqli lavash') 
    korzinka_rus_list.append('лаваш с сыром') 
    await callback.answer('siz pishloqli lavash sotib oldiz')
    
@dp.callback_query(F.data == 'tovuqli lavash sotib olish')
async def tovuqli_lavash_sotib_olish_function(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('tovuqli lavash')
    korzinka_rus_list.append('куриный лаваш')
    await callback.answer('siz tovuqli lavash sotib oldis') 





@dp.callback_query(F.data == 'standart burger sotib olish')
async def standart_burger_sotib_olish_function(callback: types.CallbackQuery):
    korzinka_uzb_list.append('standart burger')
    korzinka_rus_list.append('стандартный бургер')   
    await callback.answer('siz standart burger sotib oldis') 
    
@dp.callback_query(F.data == "hamburger sotib olish")
async def buy_hamburger(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('hamburger')
    korzinka_rus_list.append('гамбургер') 
    await callback.answer('siz hamburger sotib oldiz')
    
@dp.callback_query(F.data == 'chizburger sotib olish')
async def tovuqli_lavash_sotib_olish_function(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('chizburger')
    korzinka_rus_list.append('чизбургер') 
    await callback.answer('siz chizburger sotib oldis')   
    




@dp.callback_query(F.data == 'kichik fri sotib olish')
async def buy_mini_fri(callback: types.CallbackQuery):
    korzinka_uzb_list.append('kichik fri')
    korzinka_rus_list.append('картошка фри')   
    await callback.answer('siz kichik frir sotib oldis') 
    
@dp.callback_query(F.data == "ortacha fri sotib olish")
async def buy_big_fri(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('ortacha fri')
    korzinka_rus_list.append('средний картофель фри') 
    await callback.answer('siz ortacha fri sotib oldiz')
    
@dp.callback_query(F.data == 'katta fri sotib olish')
async def buy_biggest_fri(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('katta fri')
    korzinka_rus_list.append('большая картошка фри') 
    await callback.answer('siz katta fri sotib oldis')   





@dp.callback_query(F.data == 'xotdog sotib olish')
async def buy_xotdog(callback: types.CallbackQuery):
    korzinka_uzb_list.append('xotdog')
    korzinka_rus_list.append('хот-дог')   
    await callback.answer('siz xotdog sotib oldis') 
    
@dp.callback_query(F.data == "ikkitali xotdog sotib olish")
async def buy_double_xotdog(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('ikkitali xotdog')
    korzinka_rus_list.append('двойной хот-дог') 
    await callback.answer('siz ikkitali xotdog sotib oldiz')
   
   
    
    
@dp.callback_query(F.data == 'tovuqli sendvich sotib olish')
async def buy_xotdog(callback: types.CallbackQuery):
    korzinka_uzb_list.append('tovuqli sendvich')
    korzinka_rus_list.append('куриный сендвич')   
    await callback.answer('siz tovuqli sendvich sotib oldis') 
    
@dp.callback_query(F.data == "mol goshli sendvich sotib olish")
async def buy_double_xotdog(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('mol goshli sendvich')
    korzinka_rus_list.append('сэндвич с говядиной') 
    await callback.answer('siz mol goshli sendvich sotib oldiz')
    
    
    
    
    
@dp.callback_query(F.data == 'qanotchalar 3d sotib olish')
async def buy_krilijki_3d(callback: types.CallbackQuery):
    korzinka_uzb_list.append('qanotchalar 3d')
    korzinka_rus_list.append('крилижки 3 ш')   
    await callback.answer('siz qanotchalar 3d sotib oldis') 
    
@dp.callback_query(F.data == "qanotchalar 5d sotib olish")
async def buy_krilijki_5d(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('qanotchalar 5d')
    korzinka_rus_list.append('крилижки 5 шг') 
    await callback.answer('siz qanotchalar 5d sotib oldiz')   
    
@dp.callback_query(F.data == "qanotchalar 7d sotib olish")
async def buy_krilijki_7d(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('qanotchalar 7d')
    korzinka_rus_list.append('крилижки 7 ш') 
    await callback.answer('siz qanotchalar 7d sotib oldiz')      
    
    
@dp.callback_query(F.data == 'achchiq qanotchalar 3d sotib olish')
async def buy_achchiq_krilijki_3d(callback: types.CallbackQuery):
    korzinka_uzb_list.append('achchiq qanotchalar 3d')
    korzinka_rus_list.append('острый крилижки 3 ш')   
    await callback.answer('siz achchiq qanotchalar 3d sotib oldis') 
    
@dp.callback_query(F.data == "achchiq qanotchalar 5d sotib olish")
async def buy_achchiq_krilijki_5d(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('achchiq qanotchalar 5d')
    korzinka_rus_list.append('острый крилижки 5 шг') 
    await callback.answer('siz achchiq qanotchalar 5d sotib oldiz')   
    
@dp.callback_query(F.data == "achchiq qanotchalar 7d sotib olish")
async def buy_achchiq_krilijki_7d(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('achchiq qanotchalar 7d')
    korzinka_rus_list.append('острый крилижки 7 ш') 
    await callback.answer('siz achchiq qanotchalar 7d sotib oldiz')      
    


    














@dp.message(F.text == "лаваш 🌯")
async def lavash_rus(message: types.Message):
    await message.answer('лаваш',reply_markup=lavash_button_rus)   
    
@dp.message(F.text == "бургер 🍔")
async def burger_rus(message: types.Message):
    await message.answer('бургер',reply_markup=burger_button_rus)   
    
@dp.message(F.text == "фри 🍟")
async def fri_rus(message: types.Message):
    await message.answer('фри',reply_markup=fri_button_rus)   
    
@dp.message(F.text == "хотдог 🌭")
async def xotdog_rus(message: types.Message):
    await message.answer('хотдог',reply_markup=xotdog_button_rus)   
    
@dp.message(F.text == "сэндвич 🥪")
async def sendvich_rus(message: types.Message):
    await message.answer('сэндвич',reply_markup=sendvich_button_rus)   
    
@dp.message(F.text == "крылижки 🍗")
async def qanotchalar_rus(message: types.Message):
    await message.answer('крылижки',reply_markup=krilijki_button_rus)   




@dp.message(F.text == "мясной лаваш")
async def lavash_oddiy_function_rus(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4fikHKsb7lpQ8_BJVuUfwHp021iI7vLruxA&s",caption='мясной лаваш',reply_markup=keyboards_yes_no_goshli_lavash_rus)         
    
@dp.message(F.text == "лаваш с сыром")
async def lavash_pishloq_function_rus(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROweC0I1Y3A70ccFprzK00dTllOeEXnWL79g&s",caption='лаваш с сыром',reply_markup=keyboards_yes_no_pishloqli_lavash_rus)                   
    
@dp.message(F.text == "куриный лаваш")
async def lavash_tovuqli_function_rus(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUKVp7dSWxB9r6buzP62A5I7SZlhKyQiDkWA&s",caption='куриный лаваш',reply_markup=keyboards_yes_no_tovuqli_lavash_rus)         
    
    
    
    

@dp.message(F.text == "стандартный бургер")
async def standart_burger_function_rus_rus(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPz-LNhaGDVkpfS7dB3OQhALi5ZsvWoxrpBg&s",caption='стандартный бургер',reply_markup=keyboards_yes_no_standart_burger_rus)     
    
@dp.message(F.text == "гамбургер")
async def hamburger_function_rus_rus(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQElpavZnBQwnBjLid9VidYUzse-VnPuL-Wrg&s",caption='гамбургер',reply_markup=keyboards_yes_no_hamburger_rus)     
    
@dp.message(F.text == "чизбургер")
async def chizburger_function_rus_rus(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXIkusJx-NqQm7iOQCWvHiRNQoqHmGnr6mzQ&s",caption='чизбургер',reply_markup=keyboards_yes_no_chizburger_rus)         
      
      
      
      
      
@dp.message(F.text == "картошка фри")
async def fri_kichik_function_rus_rus(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=c22a4313664f18815aa232b2f13e2715acd57bdd-12363187-images-thumbs&n=13",caption='картошка фри',reply_markup=keyboards_yes_no_fri_kichik_rus)
    
@dp.message(F.text == "средний картофель фри")
async def fri_ortacha_function_rus_rus(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=e22bfebe3ee1d21c370386f29dfc0ebe36d708b2-5338563-images-thumbs&n=13",caption='средний картофель фри',reply_markup=keyboards_yes_no_fri_ortacha_rus)
    
@dp.message(F.text == "большая картошка фри")
async def fri_katta_function_rus_rus(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=f7222539321bdd8a239042ae872adf24058568bd-12319966-images-thumbs&n=13",caption='большая картошка фри',reply_markup=keyboards_yes_no_fri_katta_rus)
 
 
 
 

 

 
@dp.message(F.text == "простой хот-дог")
async def oddiy_xotdog_function_rus_rus(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=1a5a2698b55bf34098d6ebac3248d80cbe34da8ae0ea16ab-12421362-images-thumbs&n=13",caption='простой хот-дог',reply_markup=keyboards_yes_no_xotdog_rus)
    
@dp.message(F.text == "двойной хот-дог")
async def ikkitali_xotdog_function_rus_rus(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=cdc7d1c610cd1327d130b35a61d93c554acf07b7942c0bf0-10869598-images-thumbs&n=13",caption='двойной хот-дог',reply_markup=keyboards_yes_no_xotdog_ikkitali_rus)
    
 
 
 
    
@dp.message(F.text == "куриный сендвич")
async def tovuzli_sendvich_function_rus_rus(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=2626e4e1e72b2d1140d96165d5c4c70290bc6276-6873210-images-thumbs&n=13",caption='куриный сендвич',reply_markup=keyboards_yes_no_sendvich_tovuqli_rus)
    
@dp.message(F.text == "сэндвич с говядиной")
async def mol_sendvich_function_rus_rus(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=62079d540c4503c5ae11a0624a06bec10b8adae9-8819379-images-thumbs&n=13",caption='сэндвич с говядиной',reply_markup=keyboards_yes_no_sendvich_mol_rus)
    
    
    
    
    
@dp.message(F.text == "острые крылижки")
async def krilijki_achchiq_function_rus_rus(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=223dff190d8a996ace42e826b0a8fdfe52d72091a87c8294-12936542-images-thumbs&n=13",caption='острые крылижки',reply_markup=keyboards_yes_no_qanotchalar_achchiq_rus)
    
@dp.message(F.text == "крылижки")
async def krilijki_function_rus_rus(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=223dff190d8a996ace42e826b0a8fdfe52d72091a87c8294-12936542-images-thumbs&n=13",caption='крылижки',reply_markup=keyboards_yes_no_qanotchalar_rus)



# keyboards_yes_no_goshli_lavash_rus = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="купить мясной лаваш",callback_data="купить мясной лаваш"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
# ]) 

# keyboards_yes_no_pishloqli_lavash_rus = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="купить лаваш с сыром",callback_data="купить лаваш с сыром"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
# ]) 

# keyboards_yes_no_tovuqli_lavash_rus = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="купить куриный лаваш",callback_data="купить куриный лаваш"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
# ]) 





# keyboards_yes_no_standart_burger_rus = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="купи стандартный бургер",callback_data="купи стандартный бургер"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
# ]) 

# keyboards_yes_no_hamburger_rus = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="купить гамбургер",callback_data="купить гамбургер"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
# ]) 

# keyboards_yes_no_chizburger_rus = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="покупка чизбургера",callback_data="покупка чизбургера"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
# ])








# keyboards_yes_no_fri_kichik_rus = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="купить картошку фри",callback_data="купить картошку фри"),InlineKeyboardButton(text='отрицать',callback_data='отрицать')]
    
    
# ]) 

# keyboards_yes_no_fri_ortacha_rus = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='покупаю средний картофель фри',callback_data='покупаю средний картофель фри'),InlineKeyboardButton(text='отрицать',callback_data='отрицать')]
    
    
# ]) 

# keyboards_yes_no_fri_katta_rus = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='покупаю большую картошку фри',callback_data='покупаю большую картошку фри'),InlineKeyboardButton(text='отрицать',callback_data='отрицать')]
    
# ]) 









# keyboards_yes_no_xotdog_rus = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="покупка хот-дога",callback_data="xotdog sotib olish"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
# ]) 

# keyboards_yes_no_xotdog_ikkitali_rus = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="покупка двойных хот-догов",callback_data="покупка двойных хот-догов"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
# ]) 







# keyboards_yes_no_sendvich_tovuqli_rus = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="купить сэндвич с курицей",callback_data="купить сэндвич с курицей"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
# ]) 

# keyboards_yes_no_sendvich_mol_rus = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="покупка сэндвича с говядиной",callback_data="покупка сэндвича с говядиной"),InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
    
# ]) 






# keyboards_yes_no_qanotchalar_achchiq_rus = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="Купите 3 острых крылышка.",callback_data="Купите 3 острых крылышка.")],
#     [InlineKeyboardButton(text="Купите 5 острых крылышка.",callback_data="Купите 5 острых крылышка.")],
#     [InlineKeyboardButton(text="Купите 7 острых крылышка.",callback_data="Купите 7 острых крылышка.")],
#     [InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
# ]) 

# keyboards_yes_no_qanotchalar_rus = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="Купите 3 крылышка.",callback_data="Купите 3 крылышка.")],
#     [InlineKeyboardButton(text="Купите 5 крылышка.",callback_data="Купите 5 крылышка.")],
#     [InlineKeyboardButton(text="Купите 7 крылышка.",callback_data="Купите 7 крылышка.")],
#     [InlineKeyboardButton(text="отрицать",callback_data="отрицать")]
    
# ]) 


@dp.callback_query(F.data == 'купить мясной лаваш')
async def goshli_lavash_sotib_olish_function_rus(callback: types.CallbackQuery):
    korzinka_uzb_list.append('goshli lavash')
    korzinka_rus_list.append('мясной лаваш')
    await callback.answer('вы купили мясной лаваш') 
    
@dp.callback_query(F.data == 'купить лаваш с сыром')
async def buy_pishloqli_lavash_rus(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('pishloqli lavash') 
    korzinka_rus_list.append('лаваш с сыром') 
    await callback.answer('вы купили лаваш с сыром')
    
@dp.callback_query(F.data == 'купить куриный лаваш')
async def tovuqli_lavash_sotib_olish_function_rus(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('tovuqli lavash')
    korzinka_rus_list.append('куриный лаваш')
    await callback.answer('вы купили куриный лаваш') 







@dp.callback_query(F.data == 'купи стандартный бургер')
async def standart_burger_sotib_olish_function_rus(callback: types.CallbackQuery):
    korzinka_uzb_list.append('standart burger')
    korzinka_rus_list.append('стандартный бургер')   
    await callback.answer('вы купили стандартный бургер') 
    
@dp.callback_query(F.data == "купить гамбургер")
async def buy_hamburger_rus(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('hamburger')
    korzinka_rus_list.append('гамбургер') 
    await callback.answer('вы купили гамбургер')
    
@dp.callback_query(F.data == 'покупка чизбургера')
async def tovuqli_lavash_sotib_olish_function_rus(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('chizburger')
    korzinka_rus_list.append('чизбургер') 
    await callback.answer('вы купили чизбургер')   
    





@dp.callback_query(F.data == 'купить картошку фри')
async def buy_mini_fri_rus(callback: types.CallbackQuery):
    korzinka_uzb_list.append('kichik fri')
    korzinka_rus_list.append('картошка фри')   
    await callback.answer('вы купили картошку фри') 
    
@dp.callback_query(F.data == "покупаю средний картофель фри")
async def buy_big_fri_rus(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('ortacha fri')
    korzinka_rus_list.append('средний картофель фри') 
    await callback.answer('вы купили средний картофель фри')
    
@dp.callback_query(F.data == 'покупаю большую картошку фри')
async def buy_biggest_fr_rus(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('katta fri')
    korzinka_rus_list.append('большая картошка фри') 
    await callback.answer('вы купили большую картошку фри')   





@dp.callback_query(F.data == 'покупка хот-дога')
async def buy_xotdog_rus(callback: types.CallbackQuery):
    korzinka_uzb_list.append('xotdog')
    korzinka_rus_list.append('хот-дог')   
    await callback.answer('вы купили хот-дога') 
    
@dp.callback_query(F.data == "покупка двойных хот-догов")
async def buy_double_xotdog_rus(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('ikkitali xotdog')
    korzinka_rus_list.append('двойной хот-дог') 
    await callback.answer('вы купили двойных хот-догов')
   



    
@dp.callback_query(F.data == 'купить сэндвич с курицей')
async def buy_xotdog_rus(callback: types.CallbackQuery):
    korzinka_uzb_list.append('tovuqli sendvich')
    korzinka_rus_list.append('куриный сендвич')   
    await callback.answer('вы купили сэндвич с курицей') 
    
@dp.callback_query(F.data == "покупка сэндвича с говядиной")
async def buy_double_xotdog_rus(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('mol goshli sendvich')
    korzinka_rus_list.append('сэндвич с говядиной') 
    await callback.answer('вы купили сэндвича с говядиной')
    
    
    

    
@dp.callback_query(F.data == 'Купите 3 крылышка')
async def buy_krilijki_3d_rus(callback: types.CallbackQuery):
    korzinka_uzb_list.append('qanotchalar 3d')
    korzinka_rus_list.append('крилижки 3 ш')   
    await callback.answer('вы купили 3 крылышка') 
    
@dp.callback_query(F.data == "Купите 5 крылышка")
async def buy_krilijki_5d_rus(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('qanotchalar 5d')
    korzinka_rus_list.append('крилижки 5 шг') 
    await callback.answer('вы купили 5 крылышка')   
    
@dp.callback_query(F.data == "Купите 7 крылышка")
async def buy_krilijki_7d_rus(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('qanotchalar 7d')
    korzinka_rus_list.append('крилижки 7 ш') 
    await callback.answer('вы купили 7 крылышка')      
    
    
@dp.callback_query(F.data == 'Купите 3 острых крылышка')
async def buy_achchiq_krilijki_3d_rus(callback: types.CallbackQuery):
    korzinka_uzb_list.append('achchiq qanotchalar 3d')
    korzinka_rus_list.append('острый крилижки 3 ш')   
    await callback.answer('вы купили 3 острых крылышка') 
    
@dp.callback_query(F.data == "Купите 5 острых крылышка")
async def buy_achchiq_krilijki_5d_rus(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('achchiq qanotchalar 5d')
    korzinka_rus_list.append('острый крилижки 5 шг') 
    await callback.answer('вы купили 5 острых крылышка')   
    
@dp.callback_query(F.data == "Купите 7 острых крылышка")
async def buy_achchiq_krilijki_7d_rus(callback: types.CallbackQuery):  
    korzinka_uzb_list.append('achchiq qanotchalar 7d')
    korzinka_rus_list.append('острый крилижки 7 ш') 
    await callback.answer('вы купили 7 острых крылыш')












@dp.message(F.text == "ichimlik 🍹")
async def menu_drink_uzb(message: types.Message):
    await message.answer('ichimlik',reply_markup=menu_drink_button_uzb)
                         
@dp.message(F.text == "напиток 🍹")
async def menu_drink_rus(message: types.Message):
    await message.answer('напиток',reply_markup=menu_drink_button_rus)




@dp.message(F.text == "cola")
async def cola(message: types.Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=755d66ae3065e813db07ee21541f6b039b846a42-9857741-images-thumbs&n=13',caption='cola',reply_markup=keyboards_yes_no_cola_uzb)   
    
@dp.message(F.text == "royal")
async def royal(message: types.Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=8a440284c90ee57532599add5297d224f705cca7-11506583-images-thumbs&n=13',caption='royal',reply_markup=keyboards_yes_no_royal_uzb)   
    
@dp.message(F.text == "fanta")
async def fanta(message: types.Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=5fc9cb4714124ffb409d80175e1313585d45d256-12301937-images-thumbs&n=13',caption='fanta',reply_markup=keyboards_yes_no_fanta_uzb)   
    
@dp.message(F.text == "sprite")
async def sprite(message: types.Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=68b8fc99bb615b6142b4ce1b504a6bd4c54761d2-5220334-images-thumbs&n=13',caption='sprite',reply_markup=keyboards_yes_no_sprite_uzb)   
    
@dp.message(F.text == "moxito")
async def moxito(message: types.Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=194c48502f510520df0aff4f715288c1fe606ced-12490006-images-thumbs&n=13',caption='moxito',reply_markup=keyboards_yes_no_moxito_uzb)   
    
@dp.message(F.text == "pepsi")
async def pepsi(message: types.Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=fddeab27b2ade1df8a3722f00f7ed46392004db0-10807079-images-thumbs&n=13',caption='pepsi',reply_markup=keyboards_yes_no_pepsi_uzb)   




@dp.callback_query(F.data == 'cola sotib olish')
async def buy_cola_uzb(callback: types.CallbackQuery):
    korzinka_uzb_list.append('cola')
    korzinka_rus_list.append('кола')
    await callback.answer('siz cola sotib oldis')
    
@dp.callback_query(F.data == 'royal sotib olish')
async def buy_royal_uzb(callback: types.CallbackQuery):
    korzinka_uzb_list.append('royal')
    korzinka_rus_list.append('роял')
    await callback.answer('siz royal sotib oldis')
    
@dp.callback_query(F.data == 'fanta sotib olish')
async def buy_fanta_uzb(callback: types.CallbackQuery):
    korzinka_uzb_list.append('fanta')
    korzinka_rus_list.append('фанта')
    await callback.answer('siz fanta sotib oldis')
    
@dp.callback_query(F.data == 'sprite sotib olish')
async def buy_sprite_uzb(callback: types.CallbackQuery):
    korzinka_uzb_list.append('sprite')
    korzinka_rus_list.append('спрайт')
    await callback.answer('siz sprite sotib oldis')
    
@dp.callback_query(F.data == 'moxito sotib olish')
async def buy_moxito_uzb(callback: types.CallbackQuery):
    korzinka_uzb_list.append('moxito')
    korzinka_rus_list.append('мохито')
    await callback.answer('siz moxito sotib oldis')
    
@dp.callback_query(F.data == 'pepsi sotib olish')
async def buy_pepsi_uzb(callback: types.CallbackQuery):
    korzinka_uzb_list.append('pepsi')
    korzinka_rus_list.append('пепси')
    await callback.answer('siz pepsi sotib oburger')















@dp.message(F.text == "кола")
async def cola_rus(message: types.Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=755d66ae3065e813db07ee21541f6b039b846a42-9857741-images-thumbs&n=13',caption='cola',reply_markup=keyboards_yes_no_cola_rus)   
    
@dp.message(F.text == "роял")
async def royal_rus(message: types.Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=8a440284c90ee57532599add5297d224f705cca7-11506583-images-thumbs&n=13',caption='royal',reply_markup=keyboards_yes_no_royal_rus)   
    
@dp.message(F.text == "фанта")
async def fanta_rus(message: types.Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=5fc9cb4714124ffb409d80175e1313585d45d256-12301937-images-thumbs&n=13',caption='fanta',reply_markup=keyboards_yes_no_fanta_rus)   
    
@dp.message(F.text == "спрайт")
async def sprite_rus(message: types.Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=68b8fc99bb615b6142b4ce1b504a6bd4c54761d2-5220334-images-thumbs&n=13',caption='sprite',reply_markup=keyboards_yes_no_sprite_rus)   
    
@dp.message(F.text == "мохито")
async def moxito_rus(message: types.Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=194c48502f510520df0aff4f715288c1fe606ced-12490006-images-thumbs&n=13',caption='moxito',reply_markup=keyboards_yes_no_moxito_rus)   
    
@dp.message(F.text == "пепси")
async def pepsi_rus(message: types.Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=fddeab27b2ade1df8a3722f00f7ed46392004db0-10807079-images-thumbs&n=13',caption='pepsi',reply_markup=keyboards_yes_no_pepsi_rus)   




@dp.callback_query(F.data == 'купить колу')
async def buy_cola_rus(callback: types.CallbackQuery):
    korzinka_uzb_list.append('cola')
    korzinka_rus_list.append('кола')
    await callback.answer('вы купили колу')
    
@dp.callback_query(F.data == 'купить роял')
async def buy_royal_rus(callback: types.CallbackQuery):
    korzinka_uzb_list.append('royal')
    korzinka_rus_list.append('роял')
    await callback.answer('вы купили роял')
    
@dp.callback_query(F.data == 'купить фанту')
async def buy_fanta_rus(callback: types.CallbackQuery):
    korzinka_uzb_list.append('fanta')
    korzinka_rus_list.append('фанта')
    await callback.answer('вы купили фанту')
    
@dp.callback_query(F.data == 'купить спрайт')
async def buy_sprite_rus(callback: types.CallbackQuery):
    korzinka_uzb_list.append('sprite')
    korzinka_rus_list.append('спрайт')
    await callback.answer('вы купили спрайт')
    
@dp.callback_query(F.data == 'купить мохито')
async def buy_moxito_rus(callback: types.CallbackQuery):
    korzinka_uzb_list.append('moxito')
    korzinka_rus_list.append('мохито')
    await callback.answer('вы купили мохито')
    
@dp.callback_query(F.data == 'купить пепси')
async def buy_pepsi_rus(callback: types.CallbackQuery):
    korzinka_uzb_list.append('pepsi')
    korzinka_rus_list.append('пепси')
    await callback.answer('вы купили пепси')















@dp.message(F.text == 'korzinka 🛒')
async def korzinka_uzb(message: types.Message):
    if korzinka_uzb_list:   
        # await message.answer(f'korzinka {korzinka_uzb_list}',reply_markup=menu_korzinka_button_uzb)
        result = "\n".join([f"{key}" for key in korzinka_uzb_list])
        await message.answer(f'{result}',reply_markup=menu_korzinka_button_uzb)   
    else:
        await message.answer('siz hali hech narsa sotib omadis')
    
@dp.message(F.text == 'корзинка 🛒')
async def korzinka_rus(message: types.Message):
    if korzinka_rus_list:   
        # await message.answer('корзинка',str(korzinka_rus_list),reply_markup=menu_korzinka_button_uzb)
        result = "\n".join([f"{key}" for key in korzinka_rus_list])
        await message.answer(f'{result}',reply_markup=menu_korzinka_button_rus)   
    else:
        await message.answer('Вы еще ничего не купили')




@dp.message(F.text == 'barcha mahsulotni sotib olish')
async def buy_products(message: types.Message):
    await message.answer('barcha mahsuotni sotib olish',reply_markup=cart_button_uzb)
    
@dp.message(F.text == 'купить все товары')
async def buy_products_rus(message: types.Message):
    await message.answer('купить все товары',reply_markup=cart_button_rus)
    
    
    
humo_list = []
uzcard_list = []    
    
    
    
    
    
    
    
    
    
    
    
        
@dp.message(F.text == 'Humo')
async def humo(message: types.Message, state: FSMContext):
    await state.set_state(Cart.cart_number)
    await message.answer('cartani nomereni kiriting',reply_markup=ReplyKeyboardRemove())


@dp.message(Cart.cart_number)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit():
        await state.update_data(cart_number=text)
        await message.answer('xarid qiganinggiz uchun raxmat',reply_markup=big_menu_button_uzb)
        korzinka_rus_list.clear()
        korzinka_uzb_list.clear()
    else:
        await message.answer('siz carta raqamini kiritmadiz')
    await state.clear()
        
            
     
@dp.message(F.text == 'Uzcard')
async def uzcard(message: types.Message, state: FSMContext):
    await state.set_state(Cart.cart_number)
    await message.answer('cartani nomereni kiriting',reply_markup=ReplyKeyboardRemove())


@dp.message(Cart.cart_number)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit():
        await state.update_data(cart_number=text)
        await message.answer('xarid qiganinggiz uchun raxmat',reply_markup=big_menu_button_uzb)
        korzinka_rus_list.clear()
        korzinka_uzb_list.clear()
    else:
        await message.answer('siz carta raqamini kiritmadiz')
    await state.clear()




@dp.message(F.text == 'Хумо')
async def humo_rus(message: types.Message, state: FSMContext):
    await state.set_state(Cart_ru.cart_number)
    await message.answer('введите номер карты',reply_markup=ReplyKeyboardRemove())


@dp.message(Cart_ru.cart_number)
async def card_number_function_rus(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit():
        await state.update_data(cart_number=text)
        await message.answer('Спасибо за покупку',reply_markup=big_menu_button_rus)
        korzinka_rus_list.clear()
        korzinka_uzb_list.clear()
    else:
        await message.answer('вы не ввели номер карты')
    await state.clear()
        
            
     

@dp.message(F.text == 'Узкард')
async def uzcard_rus(message: types.Message, state: FSMContext):
    await state.set_state(Cart_ru.cart_number)
    await message.answer('введите номер карты',reply_markup=ReplyKeyboardRemove())
    
    
    
@dp.message(Cart_ru.cart_number)
async def card_number_function_rus(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit():
        
        await state.update_data(cart_number=text)
        await message.answer('Спасибо за покупку',reply_markup=big_menu_button_rus)
        korzinka_rus_list.clear()
        korzinka_uzb_list.clear()
    else:
        await message.answer('вы не ввели номер карты')
    await state.clear()


        



@dp.message(F.text == 'yana mahsulot qoshish')
async def add_new_products(message: types.Message):
    await message.answer('yana mahsulot qoshish',reply_markup=big_menu_button_uzb)

@dp.message(F.text == 'добавить больше продуктов')
async def add_new_products_rus(message: types.Message):
    await message.answer('добавить больше продуктов',reply_markup=big_menu_button_rus)






# menu_korzinka_keyboard_uzb = [
#     [KeyboardButton(text='barcha mahsulotni sotib olish'),KeyboardButton(text='barcha mahsulotlarni olib tashlash'),KeyboardButton(text='yana mahsulot qoshish')],
#     [KeyboardButton(text='ortga')]
# ]

# menu_korzinka_button_uzb = ReplyKeyboardMarkup(keyboard=menu_korzinka_keyboard_uzb,resize_keyboard=True)


# menu_korzinka_keyboard_rus = [
#     [KeyboardButton(text='купить все товары'),KeyboardButton(text='удалить все товары'),KeyboardButton(text='добавить больше продуктов')],
#     [KeyboardButton(text='назад')]
# ]

# menu_korzinka_button_rus = ReplyKeyboardMarkup(keyboard=menu_korzinka_keyboard_rus,resize_keyboard=True)



@dp.message(F.text == 'barcha mahsulotlarni olib tashlash')
async def remove_products_uzbb(message: types.Message):
    korzinka_uzb_list.clear()
    korzinka_uzb_list.clear()
    await message.answer('menu',reply_markup=big_menu_button_uzb)

@dp.message(F.text == 'удалить все товары')
async def remove_products_uzbb(message: types.Message):
    korzinka_uzb_list.clear()
    korzinka_uzb_list.clear()
    await message.answer('menu',reply_markup=big_menu_button_rus)





@dp.callback_query(F.data == "imkor qilish")
async def imkor(callback: types.CallbackQuery):
    await callback.answer('siz tovar imkor qildiz')  
    
@dp.callback_query(F.data == "отрицать")
async def imkor_rus(callback: types.CallbackQuery):
    await callback.answer('вы отказались от товара')  
    










@dp.message(F.text == "ortga ⬅️")
async def ortga(message: types.Message):
    await message.answer('menu',reply_markup=menu_button_uzb)   



@dp.message(F.text == "назад ⬅️")
async def ortga_rus(message: types.Message):
    await message.answer('меню',reply_markup=menu_button_rus)
    
@dp.message(F.text == "⬅️ ortga")
async def ortga(message: types.Message):
    await message.answer('menu',reply_markup=big_menu_button_uzb)   



@dp.message(F.text == "⬅️ назад")
async def ortga_rus(message: types.Message):
    await message.answer('меню',reply_markup=big_menu_button_rus)



@dp.message(F.text == "biz haqida")
async def about_we(message: types.Message):
    await message.answer('2000 - yilda ochilgan fast foodlarni sotishlarga asoslangan')    
    
@dp.message(F.text == "о нас")
async def about_we_rus(message: types.Message):
    await message.answer('По данным продаж магазинов быстрого питания, открытых в 2000 г')    





    
@dp.message(F.text == "sizning malumotiz 🫵")
async def about_you(message: types.Message):
    await message.answer(f'full name: {message.from_user.full_name}\nuser name: {message.from_user.username}\nID: {message.from_user.id}')    
    
@dp.message(F.text == "ваша информация 🫵")
async def yo(message: types.Message):
    await message.answer(f'full name: {message.from_user.full_name}\nuser name: {message.from_user.username}\nID: {message.from_user.id}')    
    
    
    


@dp.message(F.text == "yordam 🆘")
async def start(message: types.Message):
    await message.answer('yordam kerak bolsa shu nomerni kiriting \n +99502150')
    
@dp.message(F.text == "поддержка 🆘")
async def start(message: types.Message):
    await message.answer('если вам нужна помощь, введите этот номер \n +99502150')

    
    
@dp.message(F.text == "rus")
async def start_rus(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name)
    await message.answer("Добро пожаловать\nВведите ваше имя:", reply_markup=ReplyKeyboardRemove())
    regestratsiya_rus()
    
@dp.message(F.text == "uzb")
async def start_uzb(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name)
    await message.answer("Xush kelibsiz\nIsmingizni kiriting: ", reply_markup=ReplyKeyboardRemove())
    regestratsiya_uzb()
    
        
    
@dp.message(F.text == "tilni ozgartirish")
async def new_laungvich(message: types.Message):
    await message.answer('tilni tanlang',reply_markup=uzb_rus_button_uzb_two)    
    
@dp.message(F.text == "поменять язык")
async def nev_laungvich(message: types.Message):
    await message.answer('tilni tanlang',reply_markup=uzb_rus_button_rus_two)
    
@dp.message(F.text == "ozbek")
async def uzb_uzb(message: types.Message):
    await message.answer('menu',reply_markup=big_menu_button_uzb)
    
@dp.message(F.text == 'узбекски')
async def rus_uzb(message: types.Message):
    await message.answer('menu',reply_markup=big_menu_button_uzb)
    
@dp.message(F.text == "rus tili")
async def rus_rus(message: types.Message):
    await message.answer('menu',reply_markup=big_menu_button_rus)
    
@dp.message(F.text == 'русский')
async def uzb_rus(message: types.Message):
    await message.answer('menu',reply_markup=big_menu_button_rus)
    
    
    
    
async def main():
    await dp.start_polling(bot)
    
    
    
if __name__== '__main__':
    asyncio.run(main())