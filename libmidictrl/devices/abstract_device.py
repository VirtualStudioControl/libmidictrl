from typing import List
import rtmidi

from .device_interface import IDevice


class InputEventHandler(object):
    """
    rtmidi Event handler
    """
    def __init__(self, device: IDevice):
        self.device = device

    def __call__(self, event, data=None):
        message, deltatime = event
        self.device.callEventListeners(message[0], message[1], message, deltatime)


class AbstractDevice(IDevice):
    def __init__(self, in_port, out_port):
        """
        Constructor

        :param in_port: Index of MIDI In Port
        :param out_port: Index of MIDI Out Port
        """
        super().__init__()

        self.in_port = in_port
        self.out_port = out_port

        self.buttons = []
        self.faders = []
        self.rotarys = []

        self.events = [[],[],[],[],[],[],[],[]]

        self.midiIn = None
        self.midiOut = None
        self.isOpen = False

        self._inputEventHandler = None

    def open(self):
        """
        Open the MIDI ports for this Device
        :return:
        """
        self.midiOut = rtmidi.MidiOut()
        self.midiOut.open_port(self.out_port)

        self.midiIn = rtmidi.MidiIn()
        self.midiIn.open_port(self.in_port)

        if self._inputEventHandler is None:
            self._inputEventHandler = InputEventHandler(self)

        self.midiIn.set_callback(self._inputEventHandler)
        self.isOpen = True

    def close(self):
        """
        Close the MIDI ports for this Device
        :return:
        """
        self.isOpen = False

        self.midiIn.close_port()
        del self.midiIn
        self.midiIn = None

        self.midiOut.close_port()
        del self.midiOut
        self.midiOut = None

    # region Events

    # Overrides IDevice
    def addEventListener(self, control: int, note : int, callback):
        print("Adding Callback:", (control & 0b01110000) >> 4, note & 0b01111111)
        if not self.events[(control & 0b01110000) >> 4]:
            for i in range(128):
                self.events[(control & 0b01110000) >> 4].append([])


        self.events[(control & 0b01110000) >> 4][note & 0b01111111].append(callback)

    # Overrides IDevice
    def removeEventListener(self, control: int, note: int, callback):
        if not self.events[(control & 0b01110000) >> 4]:
            return
        self.events[(control & 0b01110000) >> 4][note & 0b01111111].remove(callback)

    # Overrides IDevice
    def callEventListeners(self, control: int, note: int, message: List[int], deltatime):
        if not self.events[(control & 0b01110000) >> 4]:
            return

        for cb in (self.events[(control & 0b01110000) >> 4][note & 0b01111111]):
            cb(message, deltatime)

    # endregion

    # Overrides IDevice
    def sendMIDIMessage(self, message):
        self.midiOut.send_message(message)
