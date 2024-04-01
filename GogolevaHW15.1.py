class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Создаём объект Autobus с помощью класса Transport
autobus = Transport('Renaul Logan', 180, 12)

print('Название автомобиля:', autobus.name, 'Скорость:', autobus.max_speed, 'Пробег:', autobus.mileage)
