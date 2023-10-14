from battery.base import Battery
from base_exceptions import NegativeTimeException


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        if self.current_date < self.last_service_date:
            raise NegativeTimeException
        return self.current_date >= self.last_service_date.replace(
            year=self.last_service_date.year + 4
        )
