# from datetime import datetime

# from engine.willoughby_engine import WilloughbyEngine


# class Glissade(WilloughbyEngine):
#     def needs_service(self):
#         service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
#         if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
#             return True
#         else:
#             return False
    
from datetime import date, timedelta
from engine.willoughby_engine import WilloughbyEngine
class Car:
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    @classmethod
    def create_glissade(cls, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        days_since_last_service = (current_date - last_service_date).days
        miles_since_last_service = current_mileage - last_service_mileage
        miles_until_next_service = 60000 - miles_since_last_service

        days_until_next_service = (timedelta(days=miles_until_next_service/50) + last_service_date - current_date).days

        return cls(current_date, last_service_date, current_mileage, last_service_mileage), miles_until_next_service, days_until_next_service

car, miles_until_next_service, days_until_next_service = Car.create_glissade(date(2022, 3, 13), date(2021, 12, 1), 12000, 8000)
print(car.current_date) # 2022-03-13
print(car.last_service_date) # 2021-12-01
print(car.current_mileage) # 12000
print(car.last_service_mileage) # 8000
print(miles_until_next_service) # 8000
print(days_until_next_service) # 158    
        
