import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
pwm = GPIO.PWM(26, 1)
try:
  pwm.start(50)
  while true:
    pass
except KeyboardInterrupt:
    print('\nExiting')

pwm.stop()
GPIO.cleanup()