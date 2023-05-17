import numpy as np
import pandas as pd

chara_type = ["ヒューマン", "エルーン", "ドラフ", "ハーヴィン", "星晶獣", "不明"]
elements = ["火", "水", "土", "風", "光", "闇"]

skill_type = ["方陣_攻刃", "方陣_背水", "方陣_渾身", "方陣_技巧", "方陣_奥義", "方陣_属性", "方陣_奥義上限", 
            "通常_攻刃", "通常_背水", "通常_渾身","通常_技巧", "通常_奥義", "通常_属性", "通常_奥義上限",
            "unk_攻刃", "unk_与ダメ", "unk_通常上限", "unk_アビ上限", "unk_奥義上限", "unk_全体上限",
            "ex_攻撃", "ex_渾身", "ex_背水", "ex_奥義", "ex_属性", "ex_アビ上限", "ex_通常上限", "ex_奥義上限", 
            "通常_アビ与ダメ", "通常_通常与ダメ", "通常_奥義与ダメ",
            "ex_アビ与ダメ", "ex_奥義与ダメ"]

aura_type = ["方陣", "通常", "unk", "ex"]

effect_type = ["攻刃", "背水", "渾身", "技巧", "奥義", "属性",
            "アビ上限", "奥義上限", "通常上限", "全体上限",
            "アビ与ダメ", "通常与ダメ", "奥義与ダメ", "全体与ダメ"
            ]

aura_num = len(aura_type)
effect_num = len(effect_type)

class skill():
    def __init__(self, expl:str, kwargs:dict):    #("説明文", ("方陣","攻刃")=24)
        self.df = pd.DataFrame(np.zeros(aura_num*effect_num).reshape(aura_num, effect_num),
                columns=effect_type,
                index=aura_type)
        
        for skill_tuple in kwargs.keys():
            self.aura = skill_tuple[0]
            self.effect = skill_tuple[1]
            self.df.at[self.aura, self.effect] = kwargs[skill_tuple]
        self.expl = expl

方陣刹那中 = skill("風属性の攻撃力上昇(中)",{("方陣","攻刃"):16, ("方陣","技巧"):15})