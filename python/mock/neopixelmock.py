
def Color(red, green, blue, white=0):
    """Convert the provided red, green, blue color to a 24-bit color value.
    Each color component should be a value 0-255 where 0 is the lowest intensity
    and 255 is the highest intensity.
    """
    return (white << 24) | (red << 16) | (green << 8) | blue


class _LED_Data(object):
    """Wrapper class which makes a SWIG LED color data array look and feel like
    a Python list of integers.
    """

    def __init__(self, channel, size):
        self.size = size
        self.channel = channel

    def __getitem__(self, pos):
        """Return the 24-bit RGB color value at the provided position or slice
        of positions.
        """

    def __setitem__(self, pos, value):
        """Set the 24-bit RGB color value at the provided position or slice of
        positions.
        """

class Adafruit_NeoPixel(object):
    def __init__(self, num, pin, freq_hz=800000, dma=5, invert=False,
                 brightness=255, channel=0, strip_type=1):
        """Class to represent a NeoPixel/WS281x LED display.  Num should be the
        number of pixels in the display, and pin should be the GPIO pin connected
        to the display signal line (must be a PWM pin like 18!).  Optional
        parameters are freq, the frequency of the display signal in hertz (default
        800khz), dma, the DMA channel to use (default 5), invert, a boolean
        specifying if the signal line should be inverted (default False), and
        channel, the PWM channel to use (defaults to 0).
        """
        self.num = num

    def __del__(self):
        # Required because Python will complain about memory leaks
        # However there's no guarantee that "ws" will even be set
        # when the __del__ method for this class is reached.
        """"""

    def _cleanup(self):
        # Clean up memory used by the library when not needed anymore.
        """"""

    def begin(self):
        """Initialize library, must be called once before other functions are
        called.
        """

    def show(self):
        """Update the display with the data from the LED buffer."""

    def setPixelColor(self, n, color):
        """Set LED at position n to the provided 24-bit color value (in RGB order).
        """

    def setPixelColorRGB(self, n, red, green, blue, white=0):
        """Set LED at position n to the provided red, green, and blue color.
        Each color component should be a value from 0 to 255 (where 0 is the
        lowest intensity and 255 is the highest intensity).
        """

    def setBrightness(self, brightness):
        """Scale each LED in the buffer by the provided brightness.  A brightness
        of 0 is the darkest and 255 is the brightest.
        """

    def getPixels(self):
        """Return an object which allows access to the LED display data as if 
        it were a sequence of 24-bit RGB values.
        """

    def numPixels(self):
        """Return the number of pixels in the display."""
        return self.num

    def getPixelColor(self, n):
        """Get the 24-bit RGB color value for the LED at position n."""
