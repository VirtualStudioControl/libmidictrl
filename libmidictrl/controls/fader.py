from .abstract_control import AbstractControl
from ..devices.device_interface import IDevice


class Fader(AbstractControl):

    def __init__(self, device: IDevice, index: int, channel: int, id_in: int, id_touch: int, id_out: int, layer: int = 0):
        super().__init__(device, index, channel, id_in, id_out, layer)
        self.idTouch = id_touch
