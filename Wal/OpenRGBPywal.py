#!/usr/bin/env python3

#from openrgb import OpenRGBClient
import sys
import openrgb

cli = openrgb.OpenRGBClient()
color1 = sys.argv[1]
color2 = sys.argv[2]

#while True:
keyboard = cli.get_devices_by_type(openrgb.utils.DeviceType.KEYBOARD)[0]
keyboard.set_color(openrgb.utils.RGBColor.fromHEX(color1))
a = keyboard.leds[0]
w = keyboard.leds[22]
d = keyboard.leds[3]
s = keyboard.leds[18]
a.set_color(openrgb.utils.RGBColor.fromHEX(color2))
w.set_color(openrgb.utils.RGBColor.fromHEX(color2))
d.set_color(openrgb.utils.RGBColor.fromHEX(color2))
s.set_color(openrgb.utils.RGBColor.fromHEX(color2))

