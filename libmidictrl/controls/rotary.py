from .abstract_control import AbstractControl
from ..devices.device_interface import IDevice

class RotaryEncoder(AbstractControl):

    def __init__(self, device: IDevice, index: int, channel: int, id_in: int, id_click : int, id_out: int, id_mode: int, layer=0x00):
        super().__init__(device, index, channel, id_in, id_out, layer)
        self.idClick = id_click
        self.idMode = id_mode
