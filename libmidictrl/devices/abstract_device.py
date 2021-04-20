from typing import List
import rtmidi

from .device_interface import IDevice


class InputEventHandler(object):
    def __init__(self, device: IDevice):
        self.device = device

    def __call__(self, event, data=None):
        message, deltatime = event
        self.device.callEventListeners(message[0], message[1], message, deltatime)


class AbstractDevice(IDevice):
    def __init__(self, in_port, out_port):
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
        self.midiOut = rtmidi.MidiOut()
        self.midiOut.open_port(self.out_port)

        self.midiIn = rtmidi.MidiIn()
        self.midiIn.open_port(self.in_port)

        if self._inputEventHandler is None:
            self._inputEventHandler = InputEventHandler(self)

        self.midiIn.set_callback(self._inputEventHandler)
        self.isOpen = True

    def close(self):
        self.isOpen = False

        self.midiIn.close_port()
        del self.midiIn
        self.midiIn = None

        self.midiOut.close_port()
        del self.midiOut
        self.midiOut = None

    # region Events

    def addEventListener(self, control: int, note : int, callback):
        print("Adding Callback:", (control & 0b01110000) >> 4, note & 0b01111111)
        if not self.events[(control & 0b01110000) >> 4]:
            for i in range(128):
                self.events[(control & 0b01110000) >> 4].append([])


        self.events[(control & 0b01110000) >> 4][note & 0b01111111].append(callback)

    def removeEventListener(self, control: int, note: int, callback):
        if not self.events[(control & 0b01110000) >> 4]:
            return
        self.events[(control & 0b01110000) >> 4][note & 0b01111111].remove(callback)

    def callEventListeners(self, control: int, note: int, message: List[int], deltatime):
        print("Message Recieved:", message, deltatime)
        if not self.events[(control & 0b01110000) >> 4]:
            return

        print("Executing Callbacks:", (self.events[(control & 0b01110000) >> 4][note & 0b01111111]))
        for cb in (self.events[(control & 0b01110000) >> 4][note & 0b01111111]):

            cb(message, deltatime)

    # endregion

    def sendMIDIMessage(self, message):
        print("Sending Message:", message)
        self.midiOut.send_message(message)