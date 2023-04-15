aura_type = ["Omega", "Optimus", "Optimus_unaura"]
skill_type = ["Verity", "Might", "Enmity", "Stamina", "Aegies", "Dual", "Trium"]
class skill():
    def __init__(self, name:str, category, limit:int, aura:bool):
        self.name = name
        self.cat = category
        self.limit = limit
        self.aura = aura

valuable = skill()