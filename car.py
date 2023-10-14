from datetime import date
from abc import ABC, abstractmethod
from engine.base import Engine
from battery.base import Battery


class Car(ABC):
    """
    The `Car` class is an abstract base class that represents a car.
    It has a single abstract method called `needs_service()`.
    """

    def __init__(
        self,
        engine: Engine,
        battery: Battery,
    ) -> None:
        self.engine = engine
        self.battery = battery
        self.last_service_date = date.fromisoformat(last_service_date)

    @abstractmethod
    def needs_service(self) -> bool:
        """
        An abstract method that needs to be implemented by any class that inherits from
        `Car`.
        It represents the logic for determining if a car needs service.

        Returns:
            bool: True if the car needs service, False otherwise.
        """
        return any(
            self.engine.needs_service(),
            self.battery.needs_service(),
        )
