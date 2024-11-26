class Hero:
    def __init__(self, hero_name: str = '', max_health: int  = 30, type: str = '', hero_power: str = ''):
        self.hero_name = hero_name
        self.max_health = max_health
        self.type = type
        self.hero_power = hero_power
    
    def __str__(self):
        return f"{self.hero_name, self.max_health, self.type, self.hero_power}"
