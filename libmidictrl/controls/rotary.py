from .abstract_control import AbstractControl
from ..devices.device_interface import IDevice


class RotaryEncoder(AbstractControl):
    """
    Rotary Encoder Control
    """
    def __init__(self, device: IDevice, index: int, channel: int, id_in: int, id_click : int, id_out: int, id_mode: int,
                 layer=0x00):
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
