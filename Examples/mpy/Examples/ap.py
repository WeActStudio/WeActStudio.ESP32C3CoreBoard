#  - WeAct Studio Official Link
#  - taobao: weactstudio.taobao.com
#  - aliexpress: weactstudio.aliexpress.com
#  - github: github.com/WeActTC
#  - gitee: gitee.com/WeAct-TC
#  - blog: www.weact-tc.cn

from utime import sleep
sleep(0.5)
print('No IDE connect,start app now.')

import machine
import esp

print('ESP32-C3 Core Board Designed By WeAct Studio')
print('CPU Freq.: ' + str(machine.freq()/1000000) + 'Mhz')
print('Flash Size: ' + str(esp.flash_size()/1024) + 'kB')

import network
from machine import Pin
from utime import sleep

print('AP Example')

ap = network.WLAN(network.AP_IF) # create access-point interface
ap.config(essid='WeAct Studio') # set the SSID of the access point
ap.config(max_clients=1) # set how many clients can connect to the network
ap.active(True)         # activate the interface

print('LED GPIO8 Blink')

led = Pin(8, Pin.OUT)
key = Pin(9, Pin.IN)

led_tick = 0
while True:
    sleep(0.2)
    
    led_tick += 1
    if led_tick == 4:
        led_tick = 0
        if led.value() == 1:
            led.value(0)
        else:
            led.value(1)
        
    if key.value() == 0:
        print('key 9 pressed')