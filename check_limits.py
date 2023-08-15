
from time import sleep
import sys


def vitals_ok(temperature, pulseRate, spo2):
  if temperature > 102 or temperature < 95:
    print('Temperature critical!')
    for i in range(6):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(1)
      print('\r *', end='')
      sys.stdout.flush()
      sleep(1)
    return False
  elif pulseRate < 60 or pulseRate > 100:
    print('Pulse Rate is out of range!')
    for i in range(6):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(1)
      print('\r *', end='')
      sys.stdout.flush()
      sleep(1)
    return False
  elif spo2 < 90:
    print('Oxygen Saturation out of range!')
    for i in range(6):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(1)
      print('\r *', end='')
      sys.stdout.flush()
      sleep(1)
    return False
  return True


if __name__ == '__main__':
  assert(vitals_ok(99, 102, 70) is False)
  assert(vitals_ok(98.1, 70, 98) is True)
  print('Done')
