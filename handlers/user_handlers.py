from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.keyboards import *
from lexicon.lexicon_ru import LEXICON_RU, LEXICON_RU_SKIN, LEXICON_RU_GLOVES
from user_portfolios import user_portfolios
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    portfolio_name = State()
    add_item = State()
    item_quality = State()
    delete_item = State()
    delete_item_quality = State()

router = Router()


def create_handler(weapon, skin):
    @router.message(F.text == weapon+'|'+skin)
    async def skin_command(message: Message):
        await message.answer(text=LEXICON_RU_SKIN[weapon][skin])

for weapon, skins in LEXICON_RU_SKIN.items():
    for skin in skins.keys():
        create_handler(weapon, skin)

def create_handler(text):
    @router.message(F.text == text)
    async def scin_command(message: Message):
        await message.answer(text=LEXICON_RU_GLOVES[text])

for key in LEXICON_RU_GLOVES.keys():
    create_handler(key)

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text=LEXICON_RU['start'], reply_markup=start_keyboard)

@router.message(F.text == 'Портфели')
async def show_portfolios(message: Message):
    user_id = str(message.from_user.id)
    kb = ReplyKeyboardBuilder()
    kb.row(KeyboardButton(text='Создать портфель'), KeyboardButton(text='В начало'), width=2)
    if user_id in user_portfolios:
        for portfolio_name in user_portfolios[user_id]:
            kb.row(KeyboardButton(text=portfolio_name), width=2)
    port_keyboard: ReplyKeyboardMarkup = kb.as_markup(resize_keyboard=True)
    await message.answer('Выберите действие:', reply_markup=port_keyboard)

@router.message(F.text == 'Создать портфель')
async def create_portfolio(message: Message):
    user_id = str(message.from_user.id)
    if user_id not in user_portfolios:
        user_portfolios[user_id] = {}
    portfolio_name = f'Портфель {len(user_portfolios[user_id]) + 1}'
    user_portfolios[user_id][portfolio_name] = {}
    await message.answer(f'Портфель "{portfolio_name}" создан!')

    await show_portfolios(message)

@router.message(F.text.startswith('Портфель'))
async def handle_portfolio(message: Message, state: FSMContext):
    user_id = str(message.from_user.id)
    portfolio_name = message.text
    if user_id in user_portfolios and portfolio_name in user_portfolios[user_id]:
        bk = ReplyKeyboardBuilder()
        bk.row(button_back)
        bk.row(KeyboardButton(text='Добавить предмет'), KeyboardButton(text='Удалить предмет'), KeyboardButton(text='Прислать портфель'), width=2)
        keyboard: ReplyKeyboardMarkup = bk.as_markup(resize_keyboard=True)
        await message.answer(f'Выбран {portfolio_name}. Выберите действие:', reply_markup=keyboard)
        await state.update_data(portfolio_name=portfolio_name)
        await state.set_state(Form.portfolio_name)
    else:
        await message.answer(f'Портфель "{portfolio_name}" не найден.')

@router.message(Form.portfolio_name, F.text == 'Добавить предмет')
async def prompt_add_item(message: Message, state: FSMContext):
    await message.answer('Введите данные предмета в формате: название предмета название скина вид(Basic, Statrack™, Souvenir) цена кол-во')
    await state.set_state(Form.add_item)

@router.message(Form.add_item)
async def add_item(message: Message, state: FSMContext):
    try:
        item_details = message.text.split(' ')
        if len(item_details) != 5:
            raise ValueError
        item_name, item_skin, item_type, item_price, item_quantity = item_details
        item_price = float(item_price)
        item_quantity = int(item_quantity)
        await state.update_data(item_name=item_name, item_skin=item_skin, item_type=item_type, item_price=item_price, item_quantity=item_quantity)
        await message.answer('Введите качество предмета:')
        await state.set_state(Form.item_quality)
    except ValueError:
        await message.answer('Неправильный формат ввода. Попробуйте снова. Введите данные предмета в формате: название предмета название скина вид(Basic, Statrack™, Souvenir) цена кол-во')

@router.message(Form.item_quality)
async def add_item_quality(message: Message, state: FSMContext):
    user_id = str(message.from_user.id)
    data = await state.get_data()
    portfolio_name = data['portfolio_name']
    item_name = data['item_name']
    item_skin = data['item_skin']
    item_price = data['item_price']
    item_quantity = data['item_quantity']
    item_quality = message.text
    item_key = f"{item_name} {item_skin}({item_quality})"
    if item_key in user_portfolios[user_id][portfolio_name]:
        if item_price in user_portfolios[user_id][portfolio_name][item_key]:
            user_portfolios[user_id][portfolio_name][item_key][item_price] += item_quantity
        else:
            user_portfolios[user_id][portfolio_name][item_key][item_price] = item_quantity
    else:
            user_portfolios[user_id][portfolio_name][item_key] = {item_price: item_quantity}
    await message.answer(f'Добавлен новый предмет в портфель "{portfolio_name}": {item_key} - {item_quantity} шт. по цене {item_price} за штуку.')
    await state.set_state(Form.portfolio_name)

@router.message(Form.portfolio_name, F.text == 'Прислать портфель')
async def send_portfolio(message: Message, state: FSMContext):
    user_id = str(message.from_user.id)
    data = await state.get_data()
    portfolio_name = data['portfolio_name']
    if user_id in user_portfolios and portfolio_name in user_portfolios[user_id]:
        portfolio = user_portfolios[user_id][portfolio_name]
        text = f'Портфель "{portfolio_name}":\n\n'
        total_value = 0
        for item_key, prices in portfolio.items():
            for price, quantity in prices.items():
                total_price = price * quantity
                text += f'{item_key} - {quantity} шт. по цене {price} за штуку. Общая стоимость: {total_price}\n'
                total_value += total_price
        await message.answer(text)
    else:
        await message.answer(f'Портфель "{portfolio_name}" не найден.')

@router.message(Form.portfolio_name, F.text == 'Удалить предмет')
async def prompt_delete_item(message: Message, state: FSMContext):
    await message.answer('Введите данные предмета в формате: название предмета название скина вид(Basic, Statrack™, Souvenir) цена кол-во')
    await state.set_state(Form.delete_item)

@router.message(Form.delete_item)
async def delete_item(message: Message, state: FSMContext):
    try:
        item_details = message.text.split(' ')
        if len(item_details) != 5:
            raise ValueError
        item_name, item_skin, item_type, item_price, item_quantity = item_details
        item_price = float(item_price)
        item_quantity = int(item_quantity)
        await state.update_data(item_name=item_name, item_skin=item_skin, item_type=item_type, item_price=item_price, item_quantity=item_quantity)
        await message.answer('Введите качество предмета:')
        await state.set_state(Form.delete_item_quality)
    except ValueError:
        await message.answer('Неправильный формат ввода. Попробуйте снова. Введите данные предмета в формате: название предмета название скина вид(Basic, Statrack™, Souvenir) цена кол-во')

@router.message(Form.delete_item_quality)
async def delete_item_quality(message: Message, state: FSMContext):
    user_id = str(message.from_user.id)
    data = await state.get_data()
    portfolio_name = data['portfolio_name']
    item_name = data['item_name']
    item_skin = data['item_skin']
    item_price = data['item_price']
    item_quantity = data['item_quantity']
    item_quality = message.text
    item_key = f"{item_name} {item_skin}({item_quality})"
    if item_key in user_portfolios[user_id][portfolio_name] and item_price in user_portfolios[user_id][portfolio_name][item_key]:
        if user_portfolios[user_id][portfolio_name][item_key][item_price] > item_quantity:
            user_portfolios[user_id][portfolio_name][item_key][item_price] -= item_quantity
            await message.answer(f'Удалено {item_quantity} шт. предмета {item_key} по цене {item_price} из портфеля "{portfolio_name}".')
        elif user_portfolios[user_id][portfolio_name][item_key][item_price] == item_quantity:
            del user_portfolios[user_id][portfolio_name][item_key][item_price]
            if not user_portfolios[user_id][portfolio_name][item_key]:
                del user_portfolios[user_id][portfolio_name][item_key]
            await message.answer(f'Предмет {item_key} по цене {item_price} полностью удален из портфеля "{portfolio_name}".')
        else:
            await message.answer(f'В портфеле "{portfolio_name}" недостаточно предметов {item_key} по цене {item_price} для удаления.')
    else:
        await message.answer(f'Предмет {item_key} по цене {item_price} не найден в портфеле "{portfolio_name}".')

    await state.set_state(Form.portfolio_name)

@router.message(F.text == 'В начало')
async def back(message: Message):
    await message.answer(text='Возвращаемся в начало', reply_markup=start_keyboard)

@router.message(F.text == 'Назад')
async def back_step(message: Message):
    await message.answer(text='Выберите класс', reply_markup=keyboard_class)

@router.message(F.text == 'Цены')
async def class_command(message: Message):
    await message.answer(text='Выберите класс ', reply_markup=keyboard_class)

@router.message(F.text == 'Портфели')
async def class_command(message: Message):
    await message.answer(text='Работаю над реализацией ')

@router.message(F.text == 'Штурмовые винтовки')
async def class_command(message: Message):
    await message.answer(text='Выберите класс ', reply_markup=keyboard_as_rifl)

@router.message(F.text == 'Снайперские винтовки')
async def class_command(message: Message):
    await message.answer(text='Выберите класс ', reply_markup=keyboard_snip_rifl)

@router.message(F.text == 'Тяжелое оружие')
async def class_command(message: Message):
    await message.answer(text='Выберите класс ', reply_markup=keyboard_heavy)

@router.message(F.text == 'ПП')
async def class_command(message: Message):
    await message.answer(text='Выберите класс ', reply_markup=keyboard_smgs)

@router.message(F.text == 'Пистолеты')
async def class_command(message: Message):
    await message.answer(text='Выберите класс ', reply_markup=keyboard_pistols)

@router.message(F.text == 'Ножи')
async def class_command(message: Message):
    await message.answer(text='Выберите класс ', reply_markup=keyboard_knifes)

@router.message(F.text == 'Перчатки')
async def class_command(message: Message):
    await message.answer(text='Выберите класс ', reply_markup=keyboard_gloves)

@router.message(F.text == 'AK-47')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_ak)

@router.message(F.text == 'M4A4')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_m4a4)

@router.message(F.text == 'M4A1-S')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_m4a1)

@router.message(F.text == 'AUG')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_aug)

@router.message(F.text == 'SG 553')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_sg553)

@router.message(F.text == 'Galil-AR')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_galil)

@router.message(F.text == 'FAMAS')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_famas)

@router.message(F.text == 'AWP')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_awp)

@router.message(F.text == 'SSG 08')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_ssg08)

@router.message(F.text == 'SCAR-20')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_scar)

@router.message(F.text == 'G3SG1')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_g3sg1)

@router.message(F.text == 'Sawed-Off')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_sawed)

@router.message(F.text == 'Mag-7')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_mag7)

@router.message(F.text == 'Nova')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_nova)

@router.message(F.text == 'Xm1014')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_xm1014)

@router.message(F.text == 'Negev')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_negev)

@router.message(F.text == 'M249')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_m249)

@router.message(F.text == 'P90')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_p90)

@router.message(F.text == 'UMP-45')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_ump45)

@router.message(F.text == 'MAC-10')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_mac10)

@router.message(F.text == 'MP7')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_mp7)

@router.message(F.text == 'MP9')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_mp9)

@router.message(F.text == 'MP5-SD')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_mp5)

@router.message(F.text == 'PP-Bizon')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_bizon)

@router.message(F.text == 'USP-S')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_usp)

@router.message(F.text == 'Glock-18')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_glock)

@router.message(F.text == 'Desert Eagle')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_deagle)

@router.message(F.text == 'P250')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_p250)

@router.message(F.text == 'Five-Seven')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_fiveseven)

@router.message(F.text == 'CZ75-Auto')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_cz75)

@router.message(F.text == 'P2000')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_p2000)

@router.message(F.text == 'Tec-9')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_tec9)

@router.message(F.text == 'R9 Revolver')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_revolver)

@router.message(F.text == 'Dual Berettas')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_berettas)

@router.message(F.text == 'Kukri')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_kukri)

@router.message(F.text == 'Karambit')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_karambit)

@router.message(F.text == 'M9 Bayonet')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_m9)

@router.message(F.text == 'Butterfly')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_butterfly)

@router.message(F.text == 'Talon')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_talon)

@router.message(F.text == 'Skeleton')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_skeleton)

@router.message(F.text == 'Classic')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_classic)

@router.message(F.text == 'Bayonet')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_bayonet)

@router.message(F.text == 'Stiletto')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_stiletto)

@router.message(F.text == 'Ursus')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_ursus)

@router.message(F.text == 'Paracord')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_paracord)

@router.message(F.text == 'Nomad')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_nomad)

@router.message(F.text == 'Survival')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_survival)

@router.message(F.text == 'Huntsman')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_huntsman)

@router.message(F.text == 'Flip')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_flip)

@router.message(F.text == 'Bowie')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_bowie)

@router.message(F.text == 'Falchion')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_falchion)

@router.message(F.text == 'Gut')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_gut)

@router.message(F.text == 'Navaja')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_navaja)

@router.message(F.text == 'Shadow Daggers')
async def skin_command(message: Message):
    await message.answer(text='Выберите скин ', reply_markup=keyboard_shadow)
