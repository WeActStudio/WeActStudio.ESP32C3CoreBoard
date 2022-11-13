#  - WeAct Studio Official Link
#  - taobao: weactstudio.taobao.com
#  - aliexpress: weactstudio.aliexpress.com
#  - github: github.com/WeActTC
#  - gitee: gitee.com/WeAct-TC
#  - blog: www.weact-tc.cn

import machine
import esp
print('ESP32-C3 Core Board Designed By WeAct Studio')
print('CPU Freq.: ' + str(machine.freq()/1000000) + 'Mhz')
print('Flash Size: ' + str(esp.flash_size()/1024) + 'kB')

from utime import sleep
from machine import Pin, PWM

print('led with smooth duty change Example')

DUTY_MAX = 2**16 - 1

duty_u16 = 0
delta_d = 48

p = PWM(Pin(8), 2000, duty_u16=duty_u16)
print(p)

while True:
    p.duty_u16(duty_u16)

    sleep(1 / 1000)

    duty_u16 += delta_d
    if duty_u16 >= DUTY_MAX:
        duty_u16 = DUTY_MAX
        delta_d = -delta_d
    elif duty_u16 <= 0:
        duty_u16 = 0
        delta_d = -delta_d