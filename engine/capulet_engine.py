from engine.base import Engine
from base_exceptions import NegativeMileageException


class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        if self.current_mileage < self.last_service_mileage:
            raise NegativeMileageException
        return self.current_mileage >= self.last_service_mileage + 30000
