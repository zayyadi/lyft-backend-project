from abc import ABC, abstractmethod
from datetime import date


class Service(ABC):
    def __init__(self, last_service_date: str) -> None:
        """
        Initializes a car object with the provided `last_service_date`.

        Args:
            last_service_date (str): The date of the last service for the car.
        """
        self.last_service_date = date.fromisoformat(last_service_date)

    @abstractmethod
    def need_service():
        pass
