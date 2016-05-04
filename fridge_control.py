#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import rrdtool

OutputPin = 40 #Physical PIN 40, NAME GPIO21

GPIO.setmode(GPIO.BOARD)          #Numbers GPIOs by physical location
GPIO.setup(OutputPin, GPIO.OUT)   #Set OutputPin's mode as output
GPIO.output(OutputPin, GPIO.LOW) #Set OutputPin as low (0V) to trun off the relais

fermentation_temp = 25  # Set Fermentation Temerapture 
hysteresis_temp   = 3   # Set Hysteresis Temperature for less switching of the comperssor
hys = 0 		# Marker for active hysteresis

try:
	while True:	
		info = rrdtool.info('fridge_control.rrd')
 		timestamp =  info['last_update']
		print timestamp
		value = info['ds[temp0].last_ds']
		print value
		#print type(value)

		value_f = float(value)
		#print value_f
		#print type(value_f)
				
		if hys:
			switch_temp = fermentation_temp - hysteresis_temp
		else:	
			switch_temp = fermentation_temp

	
		if value_f >= switch_temp:
			GPIO.output(OutputPin, GPIO.HIGH) #relais on
 		        print '1'
			hys = 1
		else:
			GPIO.output(OutputPin, GPIO.LOW) #relais off		
			print '0'
			hys = 0
			
		time.sleep(10)

except KeyboardInterrupt: #When 'Ctrl+C' is pressed, the following code will be executed	
	print 'end'
	GPIO.output(OutputPin, GPIO.LOW) #turn relais off
	GPIO.cleanup()		         #Release resource


