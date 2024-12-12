class Hero:
    def __init__(self, hero_name: str = '', type: str = '', hero_class: str = '', max_health: int  = 30, hero_power: str = ''):
        self.hero_name = hero_name
        self.type = type
        self.hero_class = hero_class
        self.max_health = max_health
        self.hero_power = hero_power
    
    def __repr__(self):
        return f"name='{self.hero_name}', type='{self.type}', class='{self.hero_class}', health={self.max_health}, ability='{self.hero_power}')"
