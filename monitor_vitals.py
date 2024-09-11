from monitor_vitals_util import *

class Monitor_Vitals(MonitorVitalsUtil):  
    def __init__(self):
        super().__init__()

    def check_temperature(self, temperature, unit='F', language='en'):
        if unit == 'C':
            temperature = self.celsius_to_fahrenheit(temperature)

        for temperature_key, (min_val, max_val) in self.temp_range.items():
            if min_val <= temperature <= max_val:
                message = self.get_temperature_message(temperature_key)
                return self.translate_message(message, language)
        self.print_loading_message()
        message = self.get_temperature_message("CRITICAL")
        return self.translate_message(message, language)

    def check_pulse_rate(self, pulseRate, language='en'):
        for pulse_key, (min_val, max_val) in self.pulse_range.items():
            if min_val <= pulseRate <= max_val:
                message = self.get_pulse_rate_message(pulse_key)
                return self.translate_message(message, language)
        self.print_loading_message()
        message = self.get_pulse_rate_message("CRITICAL")
        return self.translate_message(message, language)

    def check_spo2(self, spo2, language='en'):
        for spo2_key, (min_val, max_val) in self.spo2_range.items():
            if min_val <= spo2 <= max_val:
                message = self.get_spo2_message(spo2_key)
                return self.translate_message(message, language)
        self.print_loading_message()
        message = self.get_spo2_message("CRITICAL")
        return self.translate_message(message, language)
