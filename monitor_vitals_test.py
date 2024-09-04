import unittest
from monitor_vitals import *

class MonitorTest(unittest.TestCase):
    monitor = Monitor_Vitals()
    def test_temperature_ok(self):
        self.assertTrue(self.monitor.is_temperature_ok(101))
        self.assertFalse(self.monitor.is_temperature_ok(94))

    def test_pulse_rate_ok(self):
        self.assertTrue(self.monitor.is_pulse_rate_ok(65))
        self.assertFalse(self.monitor.is_pulse_rate_ok(100))

    def test_spo2_ok(self):
        self.assertTrue(self.monitor.is_spo2_ok(89))
        self.assertFalse(self.monitor.is_spo2_ok(90))


if __name__ == '__main__':
    unittest.main()