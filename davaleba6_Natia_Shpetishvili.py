class Heart:
    def __init__(self, heart_pressure):
        self.state = "high blood pressure" if heart_pressure > 0.7 else "feeling good"

class Brain:
    def __init__(self, brain_load):
        self.state = "tired" if brain_load > 0.9 else "rested"

class Person:
    def __init__(self, heart_pressure, brain_load):
        self.heart_instance = Heart(heart_pressure)
        self.brain_instance = Brain(brain_load)

class Leg:
    def run(self, person):
        print(f"Running with heart state: {person.heart_instance.state}")
        print(f"Running with brain state: {person.brain_instance.state}")


if __name__ == "__main__":
    person = Person(0.8, 0.85) 
    leg = Leg()
    leg.run(person)