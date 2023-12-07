from machine import Pin, ADC
from machine import Pin, PWM
import random 
import utime

xAxis = ADC(Pin(28))
yAxis = ADC(Pin(27))
button = Pin(16,Pin.IN, Pin.PULL_UP)


while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    xStatus = "middle"
    yStatus = "middle"
    buttonStatus = "not pressed"
    if xValue <= 600:
        xStatus = "GAUCHE"
    elif xValue >= 60000:
        xStatus = "DROITE"
    if yValue <= 600:
        yStatus = "AVANCE"
    elif yValue >= 60000:
        yStatus = "RECULE"
    if buttonValue == 0:
        buttonStatus = "pressed"
    print("X: " + xStatus + ", Y: " + yStatus + " -- button " + buttonStatus)