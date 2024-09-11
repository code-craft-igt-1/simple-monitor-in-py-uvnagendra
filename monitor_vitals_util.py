from googletrans import Translator
from time import sleep
import sys

class MonitorVitalsUtil:
    def __init__(self):
        self.temp_range = {
            "HYPO_THERMIA": (0, 95),
            "NEAR_HYPO": (95, 96.53),
            "NORMAL": (96.54, 100.47),
            "NEAR_HYPER": (100.48, 102),
            "HYPER_THERMIA": (102, 1000)
        }
        self.pulse_range = {
            "BRADYCARDIA": (0, 60),
            "NORMAL": (60, 100),
            "TACHYCARDIA": (100, 1000)
        }
        self.spo2_range = {
            "HYPOXEMIA": (0, 90),
            "NORMAL": (90, 100)
        }

    def get_temperature_message(self, criticality):
        messages = {
            "NORMAL": "Temperature is normal",
            "HYPO_THERMIA": "Temperature is in warning state: hypo thermia",
            "NEAR_HYPO": "Temperature is in warning state: near hypo",
            "NEAR_HYPER": "Temperature is in warning state: near hyper",
            "HYPER_THERMIA": "Temperature is in warning state: hyper thermia",
            "CRITICAL": "Temperature is critical!"
        }
        return self.return_criticality_message(criticality, messages)

    def get_pulse_rate_message(self, criticality):
        messages = {
            "NORMAL": "Pulse Rate is normal",
            "BRADYCARDIA": "Pulse Rate is in warning state: bradycardia",
            "TACHYCARDIA": "Pulse Rate is in warning state: tachycardia",
            "CRITICAL": "Pulse Rate is critical!"
        }
        return self.return_criticality_message(criticality, messages)

    def get_spo2_message(self, criticality):
        messages = {
            "NORMAL": "SpO2 is normal",
            "HYPOXEMIA": "SpO2 is in warning state: hypoxemia",
            "CRITICAL": "SpO2 is critical!"
        }
        return self.return_criticality_message(criticality, messages)
    
    def return_criticality_message(self, criticality, messages):
        if criticality in messages:
            return messages[criticality]
        else:
            return "Invalid message!"
        
    def translate_message(self, message, dest_language):
        translator = Translator()
        translated = translator.translate(message, dest=dest_language)
        print(translated)
        return translated.text
        
    def check_temperature_unit(self, unit, temp):
        if unit == 'C':
            return (temp * 9/5) + 32
        else:
            return temp
    
    def return_critical_message(self, vital, language):
        self.print_loading_message()
        message = "{} is critical!".format(vital)
        return self.translate_message(message, language)
    
    def print_loading_message(self):
        print('\rLoading', end='\n')
        for i in range(6):
            print('\r* ', end='')
            sys.stdout.flush()
            sleep(1)
            print('\r *', end='')
            sys.stdout.flush()
            sleep(1)
