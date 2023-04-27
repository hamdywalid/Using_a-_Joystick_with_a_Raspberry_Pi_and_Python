###https://www.youtube.com/watch?v=j8-2drJMrf4
import RPi.GPIO as GPIO
from time import sleep
from smbus import SMBus

ads7830_commands = (0x84, 0xc4, 0x94, 0xd4, 0xa4, 0xe4, 0xb4, 0xf4)

def read_ads7830(input):
    bus.write_byte(0x4b, ads7830_commands[input])
    return bus.read_byte(0x4b)

GPIO.setmode(GPIO.BCM)
delayTime = 0.1

bus = SMBus(1)

# Setup the GPIO pin for the button on the joystick
buttonPin = 26
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

buttonPrevious = 1
LEDState = True

LED1 = 24
LED2 = 23
LED3 = 12
LED4 = 25

M1 = 8
M2 = 4
M3 = 3
M4 = 1
M5 = 15
M6 = 9
M7 = 10
M8 = 13
GPIO.setup(M1, GPIO.OUT)
GPIO.setup(M2, GPIO.OUT)
GPIO.setup(M3, GPIO.OUT)
GPIO.setup(M4, GPIO.OUT)
GPIO.setup(M5, GPIO.OUT)
GPIO.setup(M6, GPIO.OUT)
GPIO.setup(M7, GPIO.OUT)
GPIO.setup(M8, GPIO.OUT)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)

GPIO.output(LED1, True)
GPIO.output(LED2, True)
GPIO.output(LED3, True)
GPIO.output(LED4, True)

# where all the action happens
try:
    while True:
        # Read x signal from channel 0
        xAV = read_ads7830(0)
        # Read y signal from channel 1
        yAV = read_ads7830(1)

        # x joystick direction
        if xAV < 25:
            GPIO.output(M1, True)
            GPIO.output(M2, True)
            GPIO.output(M3, True)
            GPIO.output(M4, True)
        elif xAV > 230:
            GPIO.output(M1, False)
            GPIO.output(M2, False)
            GPIO.output(M3, False)
            GPIO.output(M4, False)
        else:
            GPIO.output(M1, False)
            GPIO.output(M2, False)
            GPIO.output(M3, False)
            GPIO.output(M4, False)
            
        # y joystick direction
        if yAV < 25:
            GPIO.output(M5, True)
            GPIO.output(M6, True)
            GPIO.output(M7, False)
            GPIO.output(M8, False)            
        elif yAV > 230:
            GPIO.output(M5, False)
            GPIO.output(M6, False)
            GPIO.output(M7, True)
            GPIO.output(M8, True)
        else:
            GPIO.output(M5, False)
            GPIO.output(M6, False)
            GPIO.output(M7, False)
            GPIO.output(M8, False)
            
        buttonCurrent = GPIO.input(buttonPin)
        if (buttonPrevious==0 and buttonCurrent==1):
            if LEDState==False:
             GPIO.output(LED1, True)
             GPIO.output(LED2, True)
             GPIO.output(LED3, True)
             GPIO.output(LED4, True)
             LEDState=True
            else:
              GPIO.output(LED1, False)
              GPIO.output(LED2, False)
              GPIO.output(LED3, False)
              GPIO.output(LED4, False)
              LEDState=False
        
        buttonPrevious = buttonCurrent
        
        # print out values
        print('X, Y and Button Values: ', xAV, yAV, buttonCurrent)
        sleep(delayTime)
        
except KeyboardInterrupt:
    GPIO.cleanup()