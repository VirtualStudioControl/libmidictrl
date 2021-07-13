from .abstract_control import AbstractControl
from ..devices.device_interface import IDevice

from ..midi.protocol.constants import *


class RotaryEncoder(AbstractControl):
    """
    Rotary Encoder Control
    """
    def __init__(self, device: IDevice, index: int, channel: int, id_in: int, id_click : int, id_out: int, id_mode: int,
                 layer=0x00,
                 status_byte_down: int = STATUS_NOTE_ON,
                 status_byte_up: int = STATUS_NOTE_OFF,
                 status_byte_value_change: int = STATUS_CONTROL_CHANGE):
        """
        Constructor

        :param device: Device this control is on
        :param index: Index of the control on the device
        :param channel: MIDI Channel of this control
        :param id_in: MIDI Device Index of this Controls events
        :param id_click: MIDI Device Index of this Controls click events
        :param id_out: MIDI Device Index of this Controls LED control commands
        :param id_mode: MIDI Device Index of this Controls LED ring mode commands
        :param layer: Layer on the device this control is on
        """
        super().__init__(device, index, channel, id_in, id_out, layer)
        self.idClick = id_click
        self.idMode = id_mode

        self.status_down = status_byte_down
        self.status_up = status_byte_up
        self.status_value_changed = status_byte_value_change
