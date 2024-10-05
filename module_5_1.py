class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor >= 1 and new_floor <= self.number_of_floors:
            print(f"Мы на этаже {new_floor}")
        else:
            print("Нет такого этажа")


Home = House("Скибиди", 21)

print(Home.number_of_floors, Home.name)
Home.go_to(20)
Home.go_to(23)