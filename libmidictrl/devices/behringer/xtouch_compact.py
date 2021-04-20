from ..abstract_device import AbstractDevice
from ...controls.button import Button
from ...controls.fader import Fader
from ...controls.rotary import RotaryEncoder

from ...midi.protocol.tools import *

LAYER_A = 0x00
LAYER_B = 0x01

OPERATION_MODE_STANDARD = 0x00
OPERATION_MODE_MC = 0x01

class XTouchCompact(AbstractDevice):

    def __init__(self, in_port, out_port):
        super().__init__(in_port, out_port)

        self.globalChannel = 0x01

        self.createControls()

    def createControls(self):

        widgetIndex = 0

        # Layer A
        for i in range(24):
            self.buttons.append(Button(self, index=widgetIndex, channel=0x00, id_in=16 + i, id_out=i, layer=LAYER_A))
            widgetIndex += 1

        for i in range(8):
            self.buttons.append(Button(self, index=widgetIndex, channel=0x00, id_in=40 + i, id_out=24 + i, layer=LAYER_A))
            widgetIndex += 1

        self.buttons.append(Button(self, index=widgetIndex, channel=0x00, id_in=48, id_out=32, layer=LAYER_A))
        widgetIndex += 1

        for i in range(6):
            self.buttons.append(Button(self, index=widgetIndex, channel=0x00, id_in=49 + i, id_out=33 +i, layer=LAYER_A))
            widgetIndex += 1

        for i in range(9):
            self.faders.append(Fader(self, index=widgetIndex, channel=0x00, id_in=1 + i, id_touch=101 + i, id_out=1 +i,
                                     layer=LAYER_A))
            widgetIndex += 1

        for i in range(16):
            self.rotarys.append(RotaryEncoder(self, index=widgetIndex, channel=0x00, id_in=10 + i, id_click=i,
                                              id_out=26 + i, id_mode=10 + i, layer=LAYER_A))
            widgetIndex += 1

        # Layer B

        for i in range(24):
            self.buttons.append(Button(self, index=widgetIndex, channel=0x00, id_in=71 + i, id_out=i, layer=LAYER_B))
            widgetIndex += 1

        for i in range(8):
            self.buttons.append(Button(self, index=widgetIndex, channel=0x00, id_in=95 + i, id_out=24 + i, layer=LAYER_B))
            widgetIndex += 1

        self.buttons.append(Button(self, index=widgetIndex, channel=0x00, id_in=103, id_out=32, layer=LAYER_B))
        widgetIndex += 1

        for i in range(6):
            self.buttons.append(Button(self, index=widgetIndex, channel=0x00, id_in=104 + i, id_out=33 +i, layer=LAYER_B))
            widgetIndex += 1

        for i in range(9):
            self.faders.append(Fader(self, index=widgetIndex, channel=0x00, id_in=28 + i, id_touch=111 + i, id_out=1 +i, layer=LAYER_B))
            widgetIndex += 1

        for i in range(16):
            self.rotarys.append(RotaryEncoder(self, index=widgetIndex, channel=0x00, id_in=37 + i, id_click=55 + i,
                                              id_out=26 + i, id_mode=10 + i, layer=LAYER_B))
            widgetIndex += 1

    #region UIControl

    def setOperationMode (self, mode: int):
        msg = controlChange(self.globalChannel, 127, mode)
        self.sendMIDIMessage(msg)

    def setLayer(self, layer : int):
        msg = programChange(self.globalChannel, layer)
        self.sendMIDIMessage(msg)

    #endregion

    # region Feedback

    def setButtonLEDState(self, control: Button, state):
        msg = noteOn(self.globalChannel, control.idOut, state)
        self.sendMIDIMessage(msg)

    def setFaderState(self, control: Fader, value):
        msg = controlChange(control.channel, control.idIn, value)
        self.sendMIDIMessage(msg)

    def setRotaryLEDMode(self, control: RotaryEncoder, mode):
        msg = controlChange(self.globalChannel, control.idMode, mode)
        self.sendMIDIMessage(msg)

    def setRotaryLEDState(self, control: RotaryEncoder, state):
        msg = controlChange(self.globalChannel, control.idOut, state)
        self.sendMIDIMessage(msg)

    def setButtonValue(self, control: Button, value: bool):
        data = 127 if value else 0
        msg = noteOn(control.channel, control.idIn, data)
        self.sendMIDIMessage(msg)

    def setFaderValue(self, control: Fader, value: int):
        msg = controlChange(control.channel, control.idIn, value)
        self.sendMIDIMessage(msg)

    def setRotaryValue(self, control: RotaryEncoder, value: int):
        msg = controlChange(control.channel, control.idIn, value)
        self.sendMIDIMessage(msg)

    # endregion