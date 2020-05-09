class ElectricCar:
    def __init__(self,range):
        self.range = range

    def drive(self,distance):
        remain_range = self.range
        if distance < remain_range:
            driven_distance = distance
            remain_range -= distance
        else:
            driven_distance = remain_range
            remain_range -= distance
        return driven_distance








class TestElectricCar:
    def test_init(self):
        car = ElectricCar(100)
        assert car
        assert car.range == 100
    def test_drive(self):
        car = ElectricCar(100)
        assert car.drive(70) == 70
        assert car.drive(50) == 30


