from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.current_speed = 0

    def start_engine(self):
        return "Car started"

    def stop_engine(self):
        return "Car stopped"
        self.current_speed = 0

class SportCar(Car):
    def start_engine(self):
        parent_result = super().start_engine()
        return f"{parent_result} with max speed of {self.max_speed} mph"

    def stop_engine(self):
        parent_result = super().stop_engine()
        self.current_speed = 0
        return parent_result

if __name__ == "__main__":
    car = SportCar(210)  
    print(car.start_engine())  
    print(car.stop_engine())
    print(f"Current Speed: {car.current_speed}")
