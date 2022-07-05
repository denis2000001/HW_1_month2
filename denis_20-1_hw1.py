class Car:
    def __init__(self,title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color
    def start_engine(self):
        print(f'{self.title} {self.model} engine started!')
    def stop_engine(self):
        print(f'{self.title} {self.model} engine stopped!')
    def info(self):
        print(f'All info:{BMW.title} {BMW.model} {BMW.weight} {BMW.hp} {BMW.nm} {BMW.max_speed} {BMW.color}\n')
BMW=Car('BMW','f32',1530,184,850, 250,'white')
BMW.start_engine()
BMW.stop_engine()
BMW.info()