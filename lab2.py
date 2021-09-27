import RPi.GPIO as GPIO
import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
pwm = GPIO.PWM(26, 1)

try:
  pwm.start(0)
  while True:
    for dc in range(100, 0, -1):
      sleep(.01)
except KeyboardInterrupt:
  print('\nExiting')

pwm.stop()
GPIO.cleanup()