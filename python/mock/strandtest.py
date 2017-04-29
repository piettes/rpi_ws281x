# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

# LED strip configuration:
LED_COUNT = 30  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5  # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 30  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)



class Strandtest(object):
    """"""
    def main(self, theClass):
        """Main"""
        strip = theClass.Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        # Intialize the library (must be called once before other functions).
        strip.begin()

        print ('Press Ctrl-C to quit.')
        while True:
            # Color wipe animations.
            self.colorWipe(strip, theClass.Color(255, 0, 0))  # Red wipe
            self.colorWipe(strip, theClass.Color(0, 255, 0))  # Blue wipe
            self.colorWipe(strip, theClass.Color(0, 0, 255))  # Green wipe

    # Define functions which animate LEDs in various ways.
    def colorWipe(self, strip, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
