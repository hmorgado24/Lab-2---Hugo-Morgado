import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pwm1 = GPIO.PWM(26, 100)
pwm2 = GPIO.PWM(19, 100)
pwm3 = GPIO.PWM(13, 100)
pwm2.start(100)
pwm3.start(100)

def blink(self):
  try:
    while True:
      if GPIO.input(25) == GPIO.HIGH:
        for dc in range(100, 0, -1):
          pwm2.ChangeDutyCycle(dc)
          sleep(.01)
        for dc in range(0, 100, 1):
          pwm2.ChangeDutyCycle(dc)
          sleep(.01)
      if GPIO.input(21) == GPIO.HIGH:
        for dc in range(100, 0, -1):
          pwm3.ChangeDutyCycle(dc)
          sleep(.01)
        for dc in range(0, 100, 1):
          pwm3.ChangeDutyCycle(dc)
          sleep(.01)
  except KeyboardInterrupt:
    print('\nExiting')
    pwm2.stop()
    pwm3.stop()
    GPIO.cleanup()

try:
  GPIO.add_event_detect(25, GPIO.RISING, callback=blink, bouncetime=200)
  GPIO.add_event_detect(21, GPIO.RISING, callback=blink, bouncetime=200)
  while True:
    GPIO.output(26, 0)
    sleep(.5)
    GPIO.output(26, 1)
    sleep(.5)
except KeyboardInterrupt:
  print('\nExiting')
  pwm1.stop()
  GPIO.cleanup()