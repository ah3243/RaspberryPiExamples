import RPi.GPIO as GPIO
import time

# define pins and frequency
pin1 = 3
pin2 = 5
pin3 = 7
pin4 = 8

freq = 200
bottomLimit = 0
topLimit = 100
increment = 5

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

GPIO.setwarnings(False)

# set PWM Pins and frequency
a = GPIO.PWM(pin1, freq)
b = GPIO.PWM(pin2, freq)
c = GPIO.PWM(pin3, freq)
d = GPIO.PWM(pin4, freq)

# initialise PWM values
a.start(0)
b.start(0)
c.start(0)
d.start(0)


try:
	while True:
		# increment up
		for i in range(bottomLimit, topLimit+increment, increment):
			a.ChangeDutyCycle(i)
			b.ChangeDutyCycle(i)
			c.ChangeDutyCycle(i)
			d.ChangeDutyCycle(i)
			print("Incrementing UP - DutyCycle: {}\n".format(i))
			time.sleep(0.2)

		# increment down
		for i in range(bottomLimit, topLimit+increment, increment):
			a.ChangeDutyCycle(topLimit - i)
			b.ChangeDutyCycle(topLimit - i)
			c.ChangeDutyCycle(topLimit - i)
			d.ChangeDutyCycle(topLimit - i)
			print("Incrementing DOWN - DutyCycle: {}\n".format(topLimit - i))
			time.sleep(0.2)

except KeyboardInterrupt:
	pass

# cleanup 
print("\nCleaning up")
a.stop()
b.stop()
c.stop()
d.stop()
print("\nExiting")


