import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIO.IN)

pwm1 = GPIO.PWM(26, 1)
pwm2 = GPIO.PWM(19, 1)
pwm3 = GPIO.PWM(13, 1)


def blink2():
  pwm2.start(0)
  while True:
    for dc in range(100, 0, -1):
      pwm2.ChangeDutyCycle(dc)
      sleep(.01)
    for dc in range(0, 100, 1):
      pwm2.ChangeDutyCycle(dc)
      sleep(.01)

try:
  GPIO.add_event_detect(20, GPIO.FALLING, callback=blink2, bouncetime=10)
  pwm1.start(0)
  while True:
    for dc in range(100, 0, -1):
      pwm1.ChangeDutyCycle(dc)
      sleep(.01)
    for dc in range(0, 100, 1):
      pwm1.ChangeDutyCycle(dc)
      sleep(.01)
except KeyboardInterrupt:
  print('\nExiting')

pwm1.stop()
pwm2.stop()
pwm3.stop()
GPIO.cleanup()