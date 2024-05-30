from data_base.data_set import *

LEXICON_RU: dict[str, str] = {
    'start': 'Привет, друг:) Я готов помочь тебе узнать цены на предметы в CS2. Выбери класс предметов',
    'skin': 'Выбери скин, цена которого тебя интересует'
}

LEXICON_RU_SKIN = {}
LEXICON_RU_GLOVES: dict[str, str] = {}

for key in gloves:
    LEXICON_RU_GLOVES[key] = dumps(gloves[key], ensure_ascii=False, indent=4).replace('{', '').replace('}', '')

for i in name_s:
    LEXICON_RU_SKIN[i] = {}


for i in range(len(name_list)):
    for key in name_list[i]:
        LEXICON_RU_SKIN[name_s[i]][key] = dumps(name_list[i][key], ensure_ascii=False, indent=4).replace('{', '').replace('}', '')
