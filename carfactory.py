from car import Car
from engine import Engine, CapuletEngine, WilloughbyEngine, SternmanEngine 
from battery import battery, SpindleBattery, NubbinBattery
from datetime import date

class CarFactory(Car):
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindleBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindleBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool):
        engine = SternmanEngine(warning_light_on)
        battery = SpindleBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

if __name__ == "__main__":
    pass

