import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pwm1 = GPIO.PWM(26, 100)
# pwm3 = GPIO.PWM(13, 100)

def blink():
  pwm2 = GPIO.PWM(19, 100)
  pwm2.start(0)a
  try:
    while True:
      if GPIO.input(pwm1) == GPIO.HIGH:
        for dc in range(100, 0, -1):
          pwm2.ChangeDutyCycle(dc)
          sleep(.01)
        for dc in range(0, 100, 1):
          pwm2.ChangeDutyCycle(dc)
          sleep(.01)
  except KeyboardInterrupt:
    print('\nExiting')
  pwm2.stop()

GPIO.add_event_detect(25, GPIO.RISING, callback=blink, bouncetime=200)

try:
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
# pwm3.stop()
GPIO.cleanup()