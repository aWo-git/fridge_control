# fridge_control
Rudimentary temperature Control and Data Log of a fridge using a Raspberry Pi, 1-Wire Temperature Sensor and normal relay.
These rudimentary control is used for controlling the temperature of a fridge to be able to brew beer with bottom-fermenting yeast like pilsener.  

The file gettemp.py is copied from "https://www.kompf.de/weather/pionewiremini.html" and a little bit adapted to my needs. The setup of the raspberry pi and how to connect the 1-Wire Temperature Sensor can also be seen there. 

The shellscript gettemp.sh calls the gettemp.py script every 10 seconds to get a current temperature value. Cronjob couldn't be used here, since minimum time intervall for cronjob is 1 minute. 

The fridge_control.rrd file is the round robin database file and can contain 10 days of temperature reading. See "http://oss.oetiker.ch/rrdtool/" for more information about these database format and what you can do with it. 

The relay was connected to the raspberry pi according to "http://ras-pi.de/2014/07/relaisboard-per-raspberry-schalten/" (website in german) but can also be seen in the documentation of the "http://www.sainsmart.com" 5V relays. The relay is connected to a standard power outlet, where the fridge is plugged in. These basic methode was used, so that no modification on the fridge has to be done. 

The file fridge_control.py contains a very basic control of a fridge by turning the compressor on and off, according to the current temperatures. The hysteresis was implemented to go easy on the fridge compressor. 

To use these files you need to setup the raspberry pi, temperature sensor and relay according to the afore mentioned webpages. 
Copy the files to a directory of your choice and make them executable. 
Start the gettemp.sh in the background with the command: "nohup ./gettemp.sh >/dev/null 2>&1 &" to get the temperature reading and datalogging. 
Start the fridge_control.py with the command: "nohup ./fridge_control.py >/dev/null 2>&1 &" to start the control of the fridge
Both nohup commands are used to run the scripts in the background. See man page for more information. 

Congratulations your done with a rudimentary control of your fridge, happy brewing ;)

If you are looking for something more comprehensive check out "http://www.brewpi.com" 

aWo @ 04.05.2016

Things I'd like to improve when I have time:
- change the round-robin database to something longer-lasting
- add more temperature sensors, also to measure how good the insulation of the fridge is
- add the possibilty to define time-temperature curves for the control. Currently I do this manually
- create a nice way to plot the temperatures and define the time vs temperature curve (no web frontend, native mac app or matlab app)
- look into the possibility to use this setup also for mash control with my brewing system.
