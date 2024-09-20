import unittest
from monitor_vitals import *

class MonitorTest(unittest.TestCase):
    monitor = Monitor_Vitals()

    def test_temperature_ok(self):
        self.assertIn("in der Nähe von Hyper", self.monitor.check_temperature(38.3, "C", 'de'))
        self.assertIn('гипотермия', self.monitor.check_temperature(34.4, "C", 'ru'))
        self.assertIn('φυσιολογική', self.monitor.check_temperature(98.6, language='el'))
        self.assertNotIn('Hyperthermia', self.monitor.check_temperature(102, "F"))
        self.assertIn('ハイパーサーミア', self.monitor.check_temperature(105, language='ja'))
        self.assertIn("critical", self.monitor.check_temperature(1002, language='en'))

    # def test_pulse_rate_ok(self):
    #     self.assertIn('нормальная', self.monitor.check_pulse_rate(65, 'ru'))
    #     self.assertIn('normal', self.monitor.check_pulse_rate(100, 'de'))
    #     self.assertIn('徐脈', self.monitor.check_pulse_rate(55, 'ja'))
    #     self.assertIn('tachycardia', self.monitor.check_pulse_rate(120))
    #     self.assertIn("κρίσιμος", self.monitor.check_pulse_rate(1002, language='el'))

    # def test_spo2_ok(self):
    #     self.assertIn('φυσιολογικό', self.monitor.check_spo2(95, 'el'))
    #     self.assertIn('hypoxemie', self.monitor.check_spo2(89, 'nl'))
    #     self.assertIn('hypoxemia', self.monitor.check_spo2(85, 'en'))
    #     self.assertIn('critique', self.monitor.check_spo2(102, 'fr'))
    #     self.assertNotIn('normal', self.monitor.check_spo2(100, 'ru'))

if __name__ == '__main__':
    unittest.main()