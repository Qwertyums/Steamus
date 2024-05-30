from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from buttons_name import *

button = KeyboardButton(text='Создать портфель')

button_1 = KeyboardButton(text='Цены')
button_2 = KeyboardButton(text='Портфели')

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_1, button_2]],
    resize_keyboard=True)

button_back = KeyboardButton(text='В начало')
button_back_step = KeyboardButton(text='Назад')

button_assault_rifles = KeyboardButton(text='Штурмовые винтовки')
button_sniper_rifles = KeyboardButton(text='Снайперские винтовки')
button_heavy_guns = KeyboardButton(text='Тяжелое оружие')
button_smgs = KeyboardButton(text='ПП')
button_pistols = KeyboardButton(text='Пистолеты')
button_knifes = KeyboardButton(text='Ножи')
button_gloves = KeyboardButton(text='Перчатки')

button_add = KeyboardButton(text='Добавить предмет')
button_remove = KeyboardButton(text='Удалить предмет')
portfel_keyboard = ReplyKeyboardBuilder()
portfel_keyboard.row(button_back)
portfel_keyboard.row(button_add, button_remove)
keyboard_portfel: ReplyKeyboardMarkup = portfel_keyboard.as_markup(resizresize_keyboard=True)

keyboard_class = ReplyKeyboardMarkup(keyboard=[[button_back],[button_assault_rifles, button_sniper_rifles, button_heavy_guns],
                                                [button_smgs, button_pistols, button_gloves], [button_knifes]])

buttons_as_rifl: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_assault_rifles
]
as_rifl_keyboard = ReplyKeyboardBuilder()
as_rifl_keyboard.row(button_back_step)
as_rifl_keyboard.row(*buttons_as_rifl, width=2)
keyboard_as_rifl: ReplyKeyboardMarkup = as_rifl_keyboard.as_markup(
    resize_keyboard=True
)

buttons_snip_rifl: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_sniper_rifles
]
snip_rifl_keyboard = ReplyKeyboardBuilder()
snip_rifl_keyboard.row(button_back_step)
snip_rifl_keyboard.row(*buttons_snip_rifl, width=2)
keyboard_snip_rifl: ReplyKeyboardMarkup = snip_rifl_keyboard.as_markup(
    resize_keyboard=True
)

buttons_heavy_guns: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_heavy
]
heavy_keyboard = ReplyKeyboardBuilder()
heavy_keyboard.row(button_back_step)
heavy_keyboard.row(*buttons_heavy_guns, width=2)
keyboard_heavy: ReplyKeyboardMarkup = heavy_keyboard.as_markup(
    resize_keyboard=True
)

buttons_pist: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_pistols
]
pistols_keyboard = ReplyKeyboardBuilder()
pistols_keyboard.row(button_back_step)
pistols_keyboard.row(*buttons_pist, width=2)
keyboard_pistols: ReplyKeyboardMarkup = pistols_keyboard.as_markup(
    resize_keyboard=True
)

buttons_knife: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_knifes
]
knifes_keyboard = ReplyKeyboardBuilder()
knifes_keyboard.row(button_back_step)
knifes_keyboard.row(*buttons_knife, width=2)
keyboard_knifes: ReplyKeyboardMarkup = knifes_keyboard.as_markup(
    resize_keyboard=True
)

buttons_SMGS: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_smgs
]
smgs_keyboard = ReplyKeyboardBuilder()
smgs_keyboard.row(button_back_step)
smgs_keyboard.row(*buttons_SMGS, width=2)
keyboard_smgs: ReplyKeyboardMarkup = smgs_keyboard.as_markup(
    resize_keyboard=True
)

buttons_glove: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_gloves
]
gloves_keyboard = ReplyKeyboardBuilder()
gloves_keyboard.row(button_back_step)
gloves_keyboard.row(*buttons_glove, width=2)
keyboard_gloves: ReplyKeyboardMarkup = gloves_keyboard.as_markup(
    resize_keyboard=True
)

buttons_ak: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_ak
]
ak_keyboard = ReplyKeyboardBuilder()
ak_keyboard.row(button_back_step)
ak_keyboard.row(*buttons_ak, width=2)
keyboard_ak: ReplyKeyboardMarkup = ak_keyboard.as_markup(
    resize_keyboard=True
)

buttons_m4a4: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_m4a4
]
m4a4_keyboard = ReplyKeyboardBuilder()
m4a4_keyboard.row(button_back_step)
m4a4_keyboard.row(*buttons_m4a4, width=2)
keyboard_m4a4: ReplyKeyboardMarkup = m4a4_keyboard.as_markup(
    resize_keyboard=True
)

buttons_m4a1: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_m4a1
]
m4a1_keyboard = ReplyKeyboardBuilder()
m4a1_keyboard.row(button_back_step)
m4a1_keyboard.row(*buttons_m4a1, width=2)
keyboard_m4a1: ReplyKeyboardMarkup = m4a1_keyboard.as_markup(
    resize_keyboard=True
)

buttons_aug: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_aug
]
aug_keyboard = ReplyKeyboardBuilder()
aug_keyboard.row(button_back_step)
aug_keyboard.row(*buttons_aug, width=2)
keyboard_aug: ReplyKeyboardMarkup = aug_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Sg553: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_sg553
]
sg553_keyboard = ReplyKeyboardBuilder()
sg553_keyboard.row(button_back_step)
sg553_keyboard.row(*buttons_Sg553, width=2)
keyboard_sg553: ReplyKeyboardMarkup = sg553_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Galil: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_galil
]
galil_keyboard = ReplyKeyboardBuilder()
galil_keyboard.row(button_back_step)
galil_keyboard.row(*buttons_Galil, width=2)
keyboard_galil: ReplyKeyboardMarkup = galil_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Famas: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_famas
]
famas_keyboard = ReplyKeyboardBuilder()
famas_keyboard.row(button_back_step)
famas_keyboard.row(*buttons_Famas, width=2)
keyboard_famas: ReplyKeyboardMarkup = famas_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Awp: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_awp
]
awp_keyboard = ReplyKeyboardBuilder()
awp_keyboard.row(button_back_step)
awp_keyboard.row(*buttons_Awp, width=2)
keyboard_awp: ReplyKeyboardMarkup = awp_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Ssg08: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_ssg08
]
ssg08_keyboard = ReplyKeyboardBuilder()
ssg08_keyboard.row(button_back_step)
ssg08_keyboard.row(*buttons_Ssg08, width=2)
keyboard_ssg08: ReplyKeyboardMarkup = ssg08_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Scar: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_scar
]
scar_keyboard = ReplyKeyboardBuilder()
scar_keyboard.row(button_back_step)
scar_keyboard.row(*buttons_Scar, width=2)
keyboard_scar: ReplyKeyboardMarkup = scar_keyboard.as_markup(
    resize_keyboard=True
)

buttons_G3sg1: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_g3sg1
]
g3sg1_keyboard = ReplyKeyboardBuilder()
g3sg1_keyboard.row(button_back_step)
g3sg1_keyboard.row(*buttons_G3sg1, width=2)
keyboard_g3sg1: ReplyKeyboardMarkup = g3sg1_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Sawed: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_sawed
]
sawed_keyboard = ReplyKeyboardBuilder()
sawed_keyboard.row(button_back_step)
sawed_keyboard.row(*buttons_Sawed, width=2)
keyboard_sawed: ReplyKeyboardMarkup = sawed_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Mag7: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_mag7
]
mag7_keyboard = ReplyKeyboardBuilder()
mag7_keyboard.row(button_back_step)
mag7_keyboard.row(*buttons_Mag7, width=2)
keyboard_mag7: ReplyKeyboardMarkup = mag7_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Nova: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_nova
]
nova_keyboard = ReplyKeyboardBuilder()
nova_keyboard.row(button_back_step)
nova_keyboard.row(*buttons_Nova, width=2)
keyboard_nova: ReplyKeyboardMarkup = nova_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Xm1014: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_xm1014
]
xm1014_keyboard = ReplyKeyboardBuilder()
xm1014_keyboard.row(button_back_step)
xm1014_keyboard.row(*buttons_Xm1014, width=2)
keyboard_xm1014: ReplyKeyboardMarkup = xm1014_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Negev: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_negev
]
negev_keyboard = ReplyKeyboardBuilder()
negev_keyboard.row(button_back_step)
negev_keyboard.row(*buttons_Negev, width=2)
keyboard_negev: ReplyKeyboardMarkup = negev_keyboard.as_markup(
    resize_keyboard=True
)

buttons_M249: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_m249
]
m249_keyboard = ReplyKeyboardBuilder()
m249_keyboard.row(button_back_step)
m249_keyboard.row(*buttons_M249, width=2)
keyboard_m249: ReplyKeyboardMarkup = m249_keyboard.as_markup(
    resize_keyboard=True
)

buttons_P90: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_p90
]
p90_keyboard = ReplyKeyboardBuilder()
p90_keyboard.row(button_back_step)
p90_keyboard.row(*buttons_P90, width=2)
keyboard_p90: ReplyKeyboardMarkup = p90_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Ump45: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_ump45
]
ump45_keyboard = ReplyKeyboardBuilder()
ump45_keyboard.row(button_back_step)
ump45_keyboard.row(*buttons_Ump45, width=2)
keyboard_ump45: ReplyKeyboardMarkup = ump45_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Mac10: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_mac10
]
mac10_keyboard = ReplyKeyboardBuilder()
mac10_keyboard.row(button_back_step)
mac10_keyboard.row(*buttons_Mac10, width=2)
keyboard_mac10: ReplyKeyboardMarkup = mac10_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Mp7: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_mp7
]
mp7_keyboard = ReplyKeyboardBuilder()
mp7_keyboard.row(button_back_step)
mp7_keyboard.row(*buttons_Mp7, width=2)
keyboard_mp7: ReplyKeyboardMarkup = mp7_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Mp9: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_mp9
]
mp9_keyboard = ReplyKeyboardBuilder()
mp9_keyboard.row(button_back_step)
mp9_keyboard.row(*buttons_Mp9, width=2)
keyboard_mp9: ReplyKeyboardMarkup = mp9_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Mp5: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_mp5
]
mp5_keyboard = ReplyKeyboardBuilder()
mp5_keyboard.row(button_back_step)
mp5_keyboard.row(*buttons_Mp5, width=2)
keyboard_mp5: ReplyKeyboardMarkup = mp5_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Bizon: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_bizon
]
bizon_keyboard = ReplyKeyboardBuilder()
bizon_keyboard.row(button_back_step)
bizon_keyboard.row(*buttons_Bizon, width=2)
keyboard_bizon: ReplyKeyboardMarkup = bizon_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Usp: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_usp
]
usp_keyboard = ReplyKeyboardBuilder()
usp_keyboard.row(button_back_step)
usp_keyboard.row(*buttons_Usp, width=2)
keyboard_usp: ReplyKeyboardMarkup = usp_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Glock: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_glock
]
glock_keyboard = ReplyKeyboardBuilder()
glock_keyboard.row(button_back_step)
glock_keyboard.row(*buttons_Glock, width=2)
keyboard_glock: ReplyKeyboardMarkup = glock_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Deagle: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_deagle
]
deagle_keyboard = ReplyKeyboardBuilder()
deagle_keyboard.row(button_back_step)
deagle_keyboard.row(*buttons_Deagle, width=2)
keyboard_deagle: ReplyKeyboardMarkup = deagle_keyboard.as_markup(
    resize_keyboard=True
)

buttons_P250: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_p250
]
p250_keyboard = ReplyKeyboardBuilder()
p250_keyboard.row(button_back_step)
p250_keyboard.row(*buttons_P250, width=2)
keyboard_p250: ReplyKeyboardMarkup = p250_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Fiveseven: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_fiveseven
]
fiveseven_keyboard = ReplyKeyboardBuilder()
fiveseven_keyboard.row(button_back_step)
fiveseven_keyboard.row(*buttons_Fiveseven, width=2)
keyboard_fiveseven: ReplyKeyboardMarkup = fiveseven_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Cz75: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_cz75
]
cz75_keyboard = ReplyKeyboardBuilder()
cz75_keyboard.row(button_back_step)
cz75_keyboard.row(*buttons_Cz75, width=2)
keyboard_cz75: ReplyKeyboardMarkup = cz75_keyboard.as_markup(
    resize_keyboard=True
)

buttons_P2000: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_p2000
]
p2000_keyboard = ReplyKeyboardBuilder()
p2000_keyboard.row(button_back_step)
p2000_keyboard.row(*buttons_P2000, width=2)
keyboard_p2000: ReplyKeyboardMarkup = p2000_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Tec9: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_tec9
]
tec9_keyboard = ReplyKeyboardBuilder()
tec9_keyboard.row(button_back_step)
tec9_keyboard.row(*buttons_Tec9, width=2)
keyboard_tec9: ReplyKeyboardMarkup = tec9_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Revolver: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_revolver
]
revolver_keyboard = ReplyKeyboardBuilder()
revolver_keyboard.row(button_back_step)
revolver_keyboard.row(*buttons_Revolver, width=2)
keyboard_revolver: ReplyKeyboardMarkup = revolver_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Berettas: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_berettas
]
berettas_keyboard = ReplyKeyboardBuilder()
berettas_keyboard.row(button_back_step)
berettas_keyboard.row(*buttons_Berettas, width=2)
keyboard_berettas: ReplyKeyboardMarkup = berettas_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Kukri: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_kukri
]
kukri_keyboard = ReplyKeyboardBuilder()
kukri_keyboard.row(button_back_step)
kukri_keyboard.row(*buttons_Kukri, width=2)
keyboard_kukri: ReplyKeyboardMarkup = kukri_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Karambit: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_karambit
]
karambit_keyboard = ReplyKeyboardBuilder()
karambit_keyboard.row(button_back_step)
karambit_keyboard.row(*buttons_Karambit, width=2)
keyboard_karambit: ReplyKeyboardMarkup = karambit_keyboard.as_markup(
    resize_keyboard=True
)

buttons_M9: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_m9
]
m9_keyboard = ReplyKeyboardBuilder()
m9_keyboard.row(button_back_step)
m9_keyboard.row(*buttons_M9, width=2)
keyboard_m9: ReplyKeyboardMarkup = m9_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Butterfly: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_butterfly
]
butterfly_keyboard = ReplyKeyboardBuilder()
butterfly_keyboard.row(button_back_step)
butterfly_keyboard.row(*buttons_Butterfly, width=2)
keyboard_butterfly: ReplyKeyboardMarkup = butterfly_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Talon: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_talon
]
talon_keyboard = ReplyKeyboardBuilder()
talon_keyboard.row(button_back_step)
talon_keyboard.row(*buttons_Talon, width=2)
keyboard_talon: ReplyKeyboardMarkup = talon_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Skeleton: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_skeleton
]
skeleton_keyboard = ReplyKeyboardBuilder()
skeleton_keyboard.row(button_back_step)
skeleton_keyboard.row(*buttons_Skeleton, width=2)
keyboard_skeleton: ReplyKeyboardMarkup = skeleton_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Classic: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_classic
]
classic_keyboard = ReplyKeyboardBuilder()
classic_keyboard.row(button_back_step)
classic_keyboard.row(*buttons_Classic, width=2)
keyboard_classic: ReplyKeyboardMarkup = classic_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Bayonet: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_bayonet
]
bayonet_keyboard = ReplyKeyboardBuilder()
bayonet_keyboard.row(button_back_step)
bayonet_keyboard.row(*buttons_Bayonet, width=2)
keyboard_bayonet: ReplyKeyboardMarkup = bayonet_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Stiletto: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_stiletto
]
stiletto_keyboard = ReplyKeyboardBuilder()
stiletto_keyboard.row(button_back_step)
stiletto_keyboard.row(*buttons_Stiletto, width=2)
keyboard_stiletto: ReplyKeyboardMarkup = stiletto_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Ursus: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_ursus
]
ursus_keyboard = ReplyKeyboardBuilder()
ursus_keyboard.row(button_back_step)
ursus_keyboard.row(*buttons_Ursus, width=2)
keyboard_ursus: ReplyKeyboardMarkup = ursus_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Paracord: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_paracord
]
paracord_keyboard = ReplyKeyboardBuilder()
paracord_keyboard.row(button_back_step)
paracord_keyboard.row(*buttons_Paracord, width=2)
keyboard_paracord: ReplyKeyboardMarkup = paracord_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Nomad: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_nomad
]
nomad_keyboard = ReplyKeyboardBuilder()
nomad_keyboard.row(button_back_step)
nomad_keyboard.row(*buttons_Nomad, width=2)
keyboard_nomad: ReplyKeyboardMarkup = nomad_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Survival: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_survival
]
survival_keyboard = ReplyKeyboardBuilder()
survival_keyboard.row(button_back_step)
survival_keyboard.row(*buttons_Survival, width=2)
keyboard_survival: ReplyKeyboardMarkup = survival_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Huntsman: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_huntsman
]
huntsman_keyboard = ReplyKeyboardBuilder()
huntsman_keyboard.row(button_back_step)
huntsman_keyboard.row(*buttons_Huntsman, width=2)
keyboard_huntsman: ReplyKeyboardMarkup = huntsman_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Flip: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_flip
]
flip_keyboard = ReplyKeyboardBuilder()
flip_keyboard.row(button_back_step)
flip_keyboard.row(*buttons_Flip, width=2)
keyboard_flip: ReplyKeyboardMarkup = flip_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Bowie: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_bowie
]
bowie_keyboard = ReplyKeyboardBuilder()
bowie_keyboard.row(button_back_step)
bowie_keyboard.row(*buttons_Bowie, width=2)
keyboard_bowie: ReplyKeyboardMarkup = bowie_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Falchion: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_falchion
]
falchion_keyboard = ReplyKeyboardBuilder()
falchion_keyboard.row(button_back_step)
falchion_keyboard.row(*buttons_Falchion, width=2)
keyboard_falchion: ReplyKeyboardMarkup = falchion_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Gut: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_gut
]
gut_keyboard = ReplyKeyboardBuilder()
gut_keyboard.row(button_back_step)
gut_keyboard.row(*buttons_Gut, width=2)
keyboard_gut: ReplyKeyboardMarkup = gut_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Navaja: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_navaja
]
navaja_keyboard = ReplyKeyboardBuilder()
navaja_keyboard.row(button_back_step)
navaja_keyboard.row(*buttons_Navaja, width=2)
keyboard_navaja: ReplyKeyboardMarkup = navaja_keyboard.as_markup(
    resize_keyboard=True
)

buttons_Shadow: list[KeyboardButton] = [
    KeyboardButton(text=i) for i in buttons_shadow
]
shadow_keyboard = ReplyKeyboardBuilder()
shadow_keyboard.row(button_back_step)
shadow_keyboard.row(*buttons_Shadow, width=2)
keyboard_shadow: ReplyKeyboardMarkup = shadow_keyboard.as_markup(
    resize_keyboard=True
)


start_port_keyboard = ReplyKeyboardMarkup(keyboard=[[button]], resize_keyboard=True)
