from tires.base import Tires
from base_exceptions import ArrayLengthException, InvalidDataPointException


class CarriganTires(Tires):
    def __init__(self, sensor_data):
        self.sensor_data = sensor_data

    def needs_service(self):
        if len(self.sensor_data) != 4:
            raise ArrayLengthException

        for data_point in self.sensor_data:
            if data_point < 0 or data_point > 1:
                raise InvalidDataPointException
            if data_point >= 0.9:
                return True
        return False
