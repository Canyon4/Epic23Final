import RPi.GPIO as GPIO
import time 
# imports GPIO and time to code
green1 = 11
green2 = 22
blue1 = 15
blue2 = 13
red1 = 26
red2 = 16 # sets up GPIO pins for lights

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)	
GPIO.setup(green1,GPIO.OUT)
GPIO.setup(green2,GPIO.OUT)
GPIO.setup(blue1,GPIO.OUT)
GPIO.setup(blue2,GPIO.OUT)
GPIO.setup(red1, GPIO.OUT)
GPIO.setup(red2,GPIO.OUT)

while True: # runs a infinite loop
	GPIO.output(blue1,GPIO.HIGH)
	GPIO.output(blue2,GPIO.HIGH) # turns on blue lights
	time.sleep(0.5) # wait time
	GPIO.output(blue1,GPIO.LOW)
	GPIO.output(blue2,GPIO.LOW) # turns off blue lights
	GPIO.output(green1,GPIO.HIGH) 
	GPIO.output(green2,GPIO.HIGH) # turns on green lights
	time.sleep(0.5) # wait time
	GPIO.output(green1,GPIO.LOW) # turns off green lights
	GPIO.output(green2,GPIO.LOW)
	GPIO.output(red1, GPIO.HIGH) # turns on red lights
	GPIO.output(red2, GPIO.HIGH)
	time.sleep(0.5) # wait time
	GPIO.output(red1,GPIO.LOW) # turn off red lights
	GPIO.output(red2,GPIO.LOW)
