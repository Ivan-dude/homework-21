class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors) #атрибут определяющий этажность здания
        self.buildingType = str(buildingType) #атрибут определяющий тип здания
    def __eq__(self, other): #оператор прегрузки проверяющий одинаковость 2 - х атрибутов объектов между собой
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType #строгое условие
num_floor = Building(100, 'skyscraper')
type_building = Building(100, 'skyscraper')
print(num_floor == type_building, ', т.к. объекты абсолютно идентичны по значениям атрибутов')

num_floor = Building(100, 'skyscraper')
type_building = Building(88, 'skyscraper')
print(num_floor == type_building, ', т.к. значения атрибута numberOfFloors отличаются')


