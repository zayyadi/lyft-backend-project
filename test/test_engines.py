import unittest
from base_exceptions import NegativeMileageException

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def test_mileage_under_threshold(self):
        """
        Test that it will return False
        when the mileage difference is under the threshold
        """
        current_mileage = 50428
        last_service_mileage = 28019
        test_engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(test_engine.needs_service())

    def test_mileage_over_threshold(self):
        """
        Test that it will return True
        when the mileage difference is over the threshold
        """
        current_mileage = 80428
        last_service_mileage = 28019
        test_engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(test_engine.needs_service())

    def test_mileage_at_threshold(self):
        """
        Test that it will return True
        when the mileage difference is at the threshold
        """
        current_mileage = 58019
        last_service_mileage = 28019
        test_engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(test_engine.needs_service())

    def test_mileage_is_negative(self):
        """
        Test that it will raise an exception
        when the mileage difference is negative
        """
        current_mileage = 23954
        last_service_mileage = 28019
        test_engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertRaises(NegativeMileageException, test_engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_mileage_under_threshold(self):
        """
        Test that it will return False
        when the mileage difference is under the threshold
        """
        current_mileage = 50428
        last_service_mileage = 28019
        test_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(test_engine.needs_service())

    def test_mileage_over_threshold(self):
        """
        Test that it will return True
        when the mileage difference is over the threshold
        """
        current_mileage = 101428
        last_service_mileage = 28019
        test_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(test_engine.needs_service())

    def test_mileage_at_threshold(self):
        """
        Test that it will return True
        when the mileage difference is at the threshold
        """
        current_mileage = 88019
        last_service_mileage = 28019
        test_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(test_engine.needs_service())

    def test_mileage_is_negative(self):
        """
        Test that it will raise an exception
        when the mileage difference is negative
        """
        current_mileage = 23954
        last_service_mileage = 28019
        test_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertRaises(NegativeMileageException, test_engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_warning_light_on(self):
        """
        Test that it will return True
        when the warning light is on
        """
        test_engine = SternmanEngine(True)
        self.assertTrue(test_engine.needs_service())

    def test_warning_light_off(self):
        """
        Test that it will return False
        when the warning light is off
        """
        test_engine = SternmanEngine(False)
        self.assertFalse(test_engine.needs_service())


if __name__ == "__main__":
    unittest.main()
