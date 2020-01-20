import RPi.GPIO as GPIO
import time

control = [5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
servo = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(servo, GPIO.OUT)

p = GPIO.PWM(servo, 50)
p.start(1.5)

p.ChangeDutyCycle(control[0])
time.sleep(1)

print("Lights OFF")

GPIO.cleanup()
