#hardware platform: FireBeetle-ESP8266

from machine import Pin,Timer

led=Pin(16,Pin.OUT)              #create LED object
tim = Timer(1)                  #create tim object

def blink(t):
  led.value(not led.value())    #the value of led is opposite of the previous

tim.init(period=1000,mode=Timer.PERIODIC, callback=blink)   #tim init,callback blink() per second

#Catch exceptions,stop program if interrupted accidentally in the 'try'
try:
  while True:
    pass
except:
  tim.deinit()
