import RPi.GPIO as GPIO
import time

TEAPOT_PIN 17
BREW_TIME 120


class BrewPot(object):

    def __init__(self, teapot_pin, brew_time)
        self._teapot_pin_ = teapot_pin
        self._brew_time_ = brew_time
        _configure_gpio_(pin)

    def brew(self):
        """
        Turns on the coffee maker/teapot for _brew_time_ seconds.
        """
        _switch_teapot_(self._teapot_pin_, True)
        time.sleep(self._brew_time_)
        _switch_teapot_(self._teapot_pin_, False)

    def _configure_gpio_(self, pin):
        GPIO.setup(pin, GPIO.OUT)

    def _switch_teapot_(self, pin, on):
        GPIO.output(pin, on)

    def __del__(self):
        switch_teapot(False)
        

@app.task
def brew():
    pot = BrewPot(TEAPOT_PIN, BREW_TIME)
    pot.brew()


if __name__ == "__main__":
    brew()
