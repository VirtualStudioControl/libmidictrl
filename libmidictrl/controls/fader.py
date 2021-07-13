from .abstract_control import AbstractControl
from ..devices.device_interface import IDevice

from ..midi.protocol.constants import *


class Fader(AbstractControl):
    """
    Fader Control
    """
    def __init__(self, device: IDevice, index: int, channel: int, id_in: int, id_touch: int, id_out: int, layer: int = 0,
                 status_byte_touch_begin: int = STATUS_CONTROL_CHANGE,
                 status_byte_touch_end: int = STATUS_CONTROL_CHANGE,
                 status_byte_value_change: int = STATUS_CONTROL_CHANGE):
        """
        Constructor

        :param device: Device this control is on
        :param index: Index of the control on the device
        :param channel: MIDI Channel of this control
        :param id_in: MIDI Device Index of this Controls value change events
        :param id_touch: MIDI Device Index of this Controls touch events
        :param id_out: MIDI Device Index of this Controls control commands
        :param layer: Layer on the device this control is on
        """
        super().__init__(device, index, channel, id_in, id_out, layer)
        self.idTouch = id_touch

        self.status_touch_begin = status_byte_touch_begin
        self.status_touch_end = status_byte_touch_end
        self.status_value_changed = status_byte_value_change