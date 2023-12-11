import RPi.GPIO as GPIO
import time 
green1 = 11
green2 = 22
blue1 = 15
blue2 = 13
red1 = 26
red2 = 16
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)	
GPIO.setup(green1,GPIO.OUT)
GPIO.setup(green2,GPIO.OUT)
GPIO.setup(blue1,GPIO.OUT)
GPIO.setup(blue2,GPIO.OUT)
GPIO.setup(red1, GPIO.OUT)
GPIO.setup(red2,GPIO.OUT)
while True:
	GPIO.output(blue1,GPIO.HIGH)
	GPIO.output(blue2,GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(blue1,GPIO.LOW)
	GPIO.output(blue2,GPIO.LOW)
	GPIO.output(green1,GPIO.HIGH)
	GPIO.output(green2,GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(green1,GPIO.LOW)
	GPIO.output(green2,GPIO.LOW)
	GPIO.output(red1, GPIO.HIGH)
	GPIO.output(red2, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(red1,GPIO.LOW)
	GPIO.output(red2,GPIO.LOW)
