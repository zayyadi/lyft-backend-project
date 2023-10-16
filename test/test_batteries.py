import unittest
from datetime import datetime
from base_exceptions import NegativeTimeException
from battery.nubbin import NubbinBattery

from battery.spindler import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_date_under_threshold(self):
        """
        Test that it will return False
        when the time difference is under the threshold
        """
        current_date = datetime.today().date()
        last_service_date = current_date.replace(
            year=current_date.year - 3, day=current_date.day + 5
        )
        test_battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(test_battery.needs_service())

    def test_date_over_threshold(self):
        """
        Test that it will return True
        when the time difference is over the threshold
        """
        current_date = datetime.today().date()
        last_service_date = current_date.replace(
            year=current_date.year - 3, day=current_date.day - 5
        )
        test_battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(test_battery.needs_service())

    def test_date_at_threshold(self):
        """
        Test that it will return True
        when the time difference is at the threshold
        """
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        test_battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(test_battery.needs_service())

    def test_date_is_negative(self):
        """
        Test that it will raise an exception
        when the time difference is negative
        """
        current_date = datetime.today().date()
        last_service_date = current_date.replace(day=current_date.day + 5)
        test_battery = SpindlerBattery(last_service_date, current_date)
        self.assertRaises(NegativeTimeException, test_battery.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_date_under_threshold(self):
        """
        Test that it will return False
        when the time difference is under the threshold
        """
        current_date = datetime.today().date()
        last_service_date = current_date.replace(
            year=current_date.year - 4, day=current_date.day + 5
        )
        test_battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(test_battery.needs_service())

    def test_date_over_threshold(self):
        """
        Test that it will return True
        when the time difference is over the threshold
        """
        current_date = datetime.today().date()
        last_service_date = current_date.replace(
            year=current_date.year - 4, day=current_date.day - 5
        )
        test_battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(test_battery.needs_service())

    def test_date_at_threshold(self):
        """
        Test that it will return True
        when the time difference is at the threshold
        """
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        test_battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(test_battery.needs_service())

    def test_date_is_negative(self):
        """
        Test that it will raise an exception
        when the time difference is negative
        """
        current_date = datetime.today().date()
        last_service_date = current_date.replace(day=current_date.day + 5)
        test_battery = NubbinBattery(last_service_date, current_date)
        self.assertRaises(NegativeTimeException, test_battery.needs_service())


if __name__ == "__main__":
    unittest.main()
