from tires.base import Tires
from base_exceptions import ArrayLengthException, InvalidDataPointException


class OctoprimeTires(Tires):
    def __init__(self, sensor_data):
        self.sensor_data = sensor_data

    def needs_service(self):
        if len(self.sensor_data) != 4:
            raise ArrayLengthException

        total_wear = 0
        for data_point in self.sensor_data:
            if data_point < 0 or data_point > 1:
                raise InvalidDataPointException
            total_wear += data_point
        return total_wear >= 3
