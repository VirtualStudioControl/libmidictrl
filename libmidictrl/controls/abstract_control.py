from ..devices.device_interface import IDevice

class AbstractControl:
    """
    Abstract baseclass for Controls
    """

    def __init__(self, device: IDevice, index: int, channel: int, id_in: int, id_out: int, layer=0x00):
        """
        Constructor

        :param device: Device this control is on
        :param index: Index of the control on the device
        :param channel: MIDI Channel of this control
        :param id_in: MIDI Device Index of this Controls events
        :param id_out: MIDI Device Index of this Controls control commands
        :param layer: Layer on the device this control is on
        """
        super(AbstractControl, self).__init__()
        self.index = index

        self.device: IDevice = device
        self.channel = channel

        self.idIn = id_in
        self.idOut = id_out

        self.layer = layer
