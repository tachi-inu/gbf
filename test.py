import numpy as np
import pandas as pd
from enum import Enum
#武器・スキル・キャラ名の中黒(・)は省略する

chara_type = Enum("種族",["ヒューマン", "エルーン", "ドラフ", "ハーヴィン", "星晶獣", "不明"])
elements = Enum("属性", ["火", "水", "土", "風", "光", "闇"])


skill_type = ["方陣_攻刃", "方陣_背水", "方陣_渾身", "方陣_技巧", "方陣_奥義", "方陣_属性", "方陣_奥義上限", 
            "通常_攻刃", "通常_背水", "通常_渾身","通常_技巧", "通常_奥義", "通常_属性", "通常_奥義上限",
            "unk_攻刃", "unk_与ダメ", "unk_通常上限", "unk_アビ上限", "unk_奥義上限", "unk_全体上限",
            "ex_攻撃", "ex_渾身", "ex_背水", "ex_奥義", "ex_属性", "ex_アビ上限", "ex_通常上限", "ex_奥義上限", 
            "通常_アビ与ダメ", "通常_通常与ダメ", "通常_奥義与ダメ",
            "ex_アビ与ダメ", "ex_奥義与ダメ"]

aura_type = ["方陣", "通常", "unk", "ex"]

effect_type = ["攻刃", "背水", "渾身", "技巧", "奥義", "属性",
            "アビ上限", "奥義上限", "通常上限", "全体上限",
            "二手", "三手",
            "アビ与ダメ", "通常与ダメ", "奥義与ダメ", "全体与ダメ"
            ]

aura_num = len(aura_type)
effect_num = len(effect_type)

class skill():
    def __init__(self, expl:str, effect:dict, aura=True):    #("説明文", {("方陣","攻刃"):24})
        self.expl = expl

        self.df = pd.DataFrame(np.zeros(aura_num*effect_num).reshape(aura_num, effect_num),
                columns=effect_type,
                index=aura_type)

        for skill_tuple in effect.keys():
            self.aura = skill_tuple[0]
            self.effect = skill_tuple[1]
            self.df.at[self.aura, self.effect] = effect[skill_tuple]

        self.aura = aura    #加護が乗るならTrue

class skill_if(skill):
    skill.__init__
    if (skill_num>=15):
        --




class weapon():
    def __init__(self, element:str, weapon_cat:str, hp:int, atk:int, skill_list:list, series=None, ):
        self.element = element
        self.weapon_cat = weapon_cat
        self.hp = hp
        self.atk = atk
        self.skill_list = skill_list
        self.series = series

劫風の攻刃 = skill("風属性の攻撃力上昇(特大)",{("通常","攻刃"):33}, aura=False)
翠の誓約 = skill("風属性キャラのアビリティの与ダメージ上昇", {("unk","アビ与ダメ"):100000})
乱気の攻刃Ⅲ = skill("風属性の攻撃力上昇(特大)", {("通常","攻刃"):22})
竜巻の無双 = skill("風属性キャラの攻撃力上昇(中)/ダブルアタック確率上昇(中)", {("通常","攻刃"):14.5, ("通常","二手"):5})
凪の果断 = skill("風属性キャラのHPが多いほど与ダメージ上昇", {("unk","全体与ダメ"):30000})

竜巻の進境 = skill("経過ターンに応じて風属性キャラの風属性攻撃力が上昇(中)")

イーウィヤビーク = weapon("風", "刀", 224, 3209, [劫風の攻刃, 翠の誓約], "アンセスタル")
