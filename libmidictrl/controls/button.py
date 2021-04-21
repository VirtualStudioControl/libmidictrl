from .abstract_control import AbstractControl
from ..devices.device_interface import *


class Button(AbstractControl):
    """
    Simple Button Control
    """

    def __init__(self, device: IDevice, index: int, channel: int, id_in: int, id_out: int, layer: int = 0):
        """
        Constructor

        :param device: Device this control is on
        :param index: Index of the control on the device
        :param channel: MIDI Channel of this control
        :param id_in: MIDI Device Index of this Controls events
        :param id_out: MIDI Device Index of this Controls control commands
        :param layer: Layer on the device this control is on
        """
        super().__init__(device, index, channel, id_in, id_out, layer)

        self.pressed = False
        self.toggleMode = False
