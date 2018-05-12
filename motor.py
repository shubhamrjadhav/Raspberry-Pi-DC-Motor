import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

def init():
    gpio.output(20,gpio.HIGH) #ENABLE 1
    #sleep(0.0001)
    gpio.output(21,gpio.HIGH) #ENABLE 2
    gpio.output(4,True)   #INPUT 1
    gpio.output(14,False) #INPUT 2
    gpio.output(17,True)  #INPUT 3
    gpio.output(18,False) #INPUT 4
def pinset():
    gpio.setup(4,gpio.OUT)
    gpio.setup(14,gpio.OUT)
    gpio.setup(17,gpio.OUT)
    gpio.setup(18,gpio.OUT)
    gpio.setup(21,gpio.OUT) 
    gpio.setup(20,gpio.OUT)
    
def fwdmot():
    gpio.output(20,True)
    gpio.output(21,True)
    gpio.output(4,True)
    gpio.output(14,False)
    gpio.output(17,True)
    gpio.output(18,False)

def stopmot():
    gpio.output(21,gpio.LOW)
    gpio.output(20,gpio.LOW)
    gpio.output(4,True)
    gpio.output(14,True)
    gpio.output(17,True)
    gpio.output(18,True)
    #pwm.stop()
    #pwm1.stop()
def motor():
    
    pinset()
    pwm  = gpio.PWM(21,100)
    pwm1 = gpio.PWM(20,100)
    pwm.start(40)
    pwm1.start(80)
    init()
    while True:
        fwdmot()
        sleep(10)
        stopmot()
        print("Stop")
            
motor()
gpio.cleanup()



	
