from .abstract_control import AbstractControl
from ..devices.device_interface import *

from ..midi.protocol.constants import *

class Button(AbstractControl):

    def __init__(self, device: IDevice, index: int, channel: int, id_in: int, id_out: int, layer: int = 0):
        super().__init__(device, index, channel, id_in, id_out, layer)

        self.pressed = False
        self.toggleMode = False
        self.toggled = False

        self.device.addEventListener(STATUS_NOTE_OFF, self.idIn, self.toggleCallback)

    def toggleCallback(self, msg, deltatime):
        print("Callback Called:", msg, deltatime)
        if not self.toggled:
            self.toggled = True
            self.device.setButtonLEDState(self, BUTTON_LED_BLINK)
        else:
            self.toggled = False
            self.device.setButtonLEDState(self, BUTTON_LED_OFF)


