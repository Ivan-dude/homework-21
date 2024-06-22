class Building:
    def __init__(self):
        self.numberOfFloors = int #атрибут определяющий этажность здания
        self.buildingType = str #атрибут определяющий тип здания
    def __eq__(self, other): #оператор прегрузки проверяющий одинаковость 2 - х атрибутов объектов между собой
        return self.numberOfFloors == self.buildingType
num_floor = Building()
building = Building()
print(num_floor.numberOfFloors == building.buildingType, ',т.к. атрибуты объектов имеют разные типы данных')

