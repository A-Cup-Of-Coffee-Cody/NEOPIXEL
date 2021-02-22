'''
Codes for Neopixel
Library needed: rspi_ws281x (sudo pip3 install rpi_ws281x / sudo pip install rpi_ws281x
LED_PIN (Ensure SPI is enabled for all GPIO under RaspPi settings)

Author: Cody Tan
'''

from rpi_ws281x import *

# LED strip configuration:
LED_COUNT      = 1      # Number of LED pixels.
#LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,LED_DMA,LED_INVERT,LED_BRIGHTNESS,LED_CHANNEL)
strip.begin()

for x in range(0,LED_COUNT):
    strip.setPixelColor(x,Color(255,0,0)) #R,G,B

strip.show()