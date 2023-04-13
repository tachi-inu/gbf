chara_type = ["Human", "Erune", "Draph", "Harvin", "Primal", "Other"]
skill_type = ["omega_atk", "omega_enm", "omega_stm", "omega_vrt", "omega_ex", "opt_atk", "opt_enm", "opt_stm",
              "opt_ex", "unk"]
class skill():
    def __init__(self, name:str, category, limit:int, aura:bool):
        self.name = name
        self.cat = category
        self.limit = limit
        self.aura = aura

valuable = skill()