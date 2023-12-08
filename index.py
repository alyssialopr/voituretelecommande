from machine import Pin, PWM
import time

# Set up la MANETTE
from machine import Pin, ADC
from machine import Pin, PWM
import random 
import utime

xAxis = ADC(Pin(28))
yAxis = ADC(Pin(27))
button = Pin(16,Pin.IN, Pin.PULL_UP)

#Set up les moteurs

#moteur 1
motor1_pin1 = Pin(7, Pin.OUT)
motor1_pin2 = Pin(8, Pin.OUT)
#EN_A = Pin(8, Pin.OUT)

#moteur 2
motor2_pin1 = Pin(4, Pin.OUT)
motor2_pin2 = Pin(3, Pin.OUT)
EN_B = Pin(2, Pin.OUT)


EN_B.high()

def MDAr():
    motor1_pin1.low()
    motor1_pin2.high()

def MDA():
    motor1_pin1.high()
    motor1_pin2.low()

def MGA():
    motor2_pin1.low()
    motor2_pin2.high()

def MGAr():
    motor2_pin1.high()
    motor2_pin2.low()
    
def Stop():
    motor1_pin1.low()
    motor1_pin2.low()
    motor2_pin1.low()
    motor2_pin2.low()
Stop()



def avancer():
    MDA()
    MGA()

def reculer():
    MDAr()
    MGAr()

def droite():
    MGA()
    MDAr()

def gauche():
    MDA()
    MGAr()

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    buttonStatus = "not pressed"
    
    if buttonValue == 0:
        buttonStatus = "pressed"
        
    if xValue <= 600:
        xStatus = "left"
        gauche()
        print('gauche')
        #time.sleep(0.2)
        
    elif xValue >= 60000:
        xStatus = "right"
        droite()
        print('droite')
        #time.sleep(0.2)
        
    elif yValue <= 600:
        yStatus = "up"
        avancer()
        print('avancer')
        #time.sleep(0.2)
        
    elif yValue >= 60000:
        yStatus = "down"
        reculer()
        print('recule')
        #time.sleep(0.2)
    else:
        print("stop")
        Stop()
    print(xValue)
    print(yValue)
    time.sleep(1)
    
        

    
    
    
    
    #if xValue <= 600:
        #xStatus = "GAUCHE"
    #elif xValue >= 60000:
        #xStatus = "DROITE"
    #if yValue <= 600:
        #yStatus = avancer()
    #elif yValue >= 60000:
        #yStatus = "RECULE"
        
        
        


    #if yValue <= 600:
       # print("a")
        #avancer()
   # time.sleep(0.1)
   # if yValue <= 60000:
    #    print("b")
      #  gauche()
       #reculer()
   # time.sleep(0.1)
    
    
#     FAIRE AVANCER LA VOITURE AVEC LA MANETTE

#avancer
#if yValue <= 600:
 #   avancer()
    
#if yValue >= 60000:
   # reculer()

    

