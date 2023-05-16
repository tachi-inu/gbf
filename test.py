import numpy
import pandas

chara_type = ["ヒューマン", "エルーン", "ドラフ", "ハーヴィン", "星晶獣", "不明"]

skill_type = ["方陣_攻刃", "方陣_背水", "方陣_渾身", "方陣_技巧", "方陣_奥義", "方陣_属性", "方陣_奥義上限", 
            "通常_攻刃", "通常_背水", "通常_渾身","通常_技巧", "通常_奥義", "通常_属性", "通常_奥義上限",
            "unk",
            "ex_攻撃", "ex_渾身", "ex_背水", "ex_奥義", "ex_属性", "ex_アビ上限", "ex_通常上限", "ex_奥義上限", 
            "通常_アビ与ダメ", "通常_通常与ダメ", "通常_奥義与ダメ",
            "ex_アビ与ダメ", "ex_奥義与ダメ"]

class skill():
    def __init__(self, name:str, category, limit:int, aura:bool):
        self.name = name
        self.cat = category
        self.limit = limit
        self.aura = aura

valuable = skill()

def 先制(turn, value):
    if turn <= 10:
        return value
    else:
        return 0
    
def ヴァリュアブル(skill_num, value):
    if skill_num >= 15:
        return value
    else:
        return 0