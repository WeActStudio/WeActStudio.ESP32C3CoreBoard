* [中文版本](./README-zh.md)
# WeActStudio.ESP32C3CoreBoard
![display](Images/1.png)
ESP32-C3FH4
> 160Mhz Max,400KB RAM,384KB ROM,4MB FLASH

Espressif Official Website www.espressif.com.cn

|Dir Name|Explain|
| :--:|:--:|
|Doc|DataSheet/ReferenceManual|
|Hardware|Hardware Development Kit|
|Examples|Software Examples|
|Tools|Tools|

## How to download the program
Method
1. Decompress `esptool-v4.2.1-win64_WeActStudio.zip` in the `Tools` directory
2. Run `WeAct Studio UART Download Tool.bat`
3. Press and hold the BOOT button and connect the computer with a USB cable. Release the BOOT button
4. Drag in the program to be burned, enter the burning address and serial port number, click Enter to start burning

## ESP-IDF Use precautions
1. When the program is continuously reset, it can be downloaded normally only after entering the burning mode
2. Software engineering needs to set UART printing to `USB Serial/Debug`
3. TBD

```
/*---------------------------------------
- WeAct Studio Official Link
- taobao: weactstudio.taobao.com
- aliexpress: weactstudio.aliexpress.com
- github: github.com/WeActTC
- gitee: gitee.com/WeAct-TC
- blog: www.weact-tc.cn
---------------------------------------*/
```