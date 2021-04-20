from ..devices.device_interface import IDevice

class AbstractControl:

    def __init__(self, device: IDevice, index: int, channel: int, id_in: int, id_out: int, layer=0x00):
        super(AbstractControl, self).__init__()
        self.index = index

        self.device: IDevice = device
        self.channel = channel

        self.idIn = id_in
        self.idOut = id_out

        self.layer = layer
