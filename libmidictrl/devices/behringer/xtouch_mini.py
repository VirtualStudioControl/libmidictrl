from virtualstudio.common.logging import logengine
from ..abstract_device import AbstractDevice
from ...controls.button import Button
from ...controls.fader import Fader
from ...controls.rotary import RotaryEncoder

from ...midi.protocol.tools import *

#region Constants
BUTTON_LED_OFF = 0x01
BUTTON_LED_ON = 0x02
BUTTON_LED_BLINK = 0x03

ROTARY_LED_MODE_SINGLE = 0x00
ROTARY_LED_MODE_PAN = 0x01
ROTARY_LED_MODE_FAN = 0x02
ROTARY_LED_MODE_SPREAD = 0x03
ROTARY_LED_MODE_TRIM = 0x04

ROTARY_LED_ALL_OFF = 0x00
ROTARY_LED_00_ON = 0x01
ROTARY_LED_01_ON = 0x02
ROTARY_LED_02_ON = 0x03
ROTARY_LED_03_ON = 0x04
ROTARY_LED_04_ON = 0x05
ROTARY_LED_05_ON = 0x06
ROTARY_LED_06_ON = 0x07
ROTARY_LED_07_ON = 0x08
ROTARY_LED_08_ON = 0x09
ROTARY_LED_09_ON = 0x0A
ROTARY_LED_10_ON = 0x0B
ROTARY_LED_11_ON = 0x0C
ROTARY_LED_12_ON = 0x0D
ROTARY_LED_00_BLINK = 0x0E
ROTARY_LED_01_BLINK = 0x0F
ROTARY_LED_02_BLINK = 0x10
ROTARY_LED_03_BLINK = 0x11
ROTARY_LED_04_BLINK = 0x12
ROTARY_LED_05_BLINK = 0x13
ROTARY_LED_06_BLINK = 0x14
ROTARY_LED_07_BLINK = 0x15
ROTARY_LED_08_BLINK = 0x16
ROTARY_LED_09_BLINK = 0x17
ROTARY_LED_10_BLINK = 0x18
ROTARY_LED_11_BLINK = 0x19
ROTARY_LED_12_BLINK = 0x1A
ROTARY_LED_ALL_ON = 0x1B
ROTARY_LED_ALL_BLINK = 0x1C

LAYER_A = 0x00
LAYER_B = 0x01

OPERATION_MODE_STANDARD = 0x00
OPERATION_MODE_MC = 0x01
#endregion

logger = logengine.getLogger()

class XTouchMini(AbstractDevice):
    """
    Behringer X-Touch Compact
    """
    def __init__(self, device_id, in_port, out_port):
        """
        Constructor

        :param in_port: Index of MIDI In Port
        :param out_port: Index of MIDI Out Port
        """
        super().__init__(device_id, in_port, out_port)

        self.globalChannel = 0x00

        self.__createControls()

    #Overrides IDevice
    def getDeviceName(self):
        """
        :return: the model name of this device
        """
        return "X-Touch Mini"

    #Overrides IDevice
    def getDeviceManufacturer(self):
        """
        :return: the manufacturer name of this device
        """
        return "Behringer"

    def __createControls(self):
        """
        Create controls for this device

        **PRIVAT METHOD. PLEASE DO NOT CALL FROM OUTSIDE OF CONSTRUCTOR FOR THIS DEVICE!**

        :return:
        """
        # Layer A

        controls = 0

        self.faders.append(Fader(self, index=controls, channel=0xa, id_in=9, id_touch=127, id_out=127,
                                 layer=LAYER_A))
        controls += 1

        for i in range(8):
            self.rotarys.append(RotaryEncoder(self, index=controls, channel=0xa, id_in=1 + i, id_click=i,
                                              id_out=9 + i, id_mode=1 + i, layer=LAYER_A))
            controls += 1

        for i in range(16):
                self.buttons.append(Button(self, index=controls, channel=0xa, id_in=8 + i, id_out=i, layer=LAYER_A))
                controls += 1

        # Layer B

        self.faders.append(Fader(self, index=controls, channel=0xa, id_in=10, id_touch=127, id_out=127,
                                 layer=LAYER_B))
        controls += 1

        for i in range(8):
            self.rotarys.append(RotaryEncoder(self, index=controls, channel=0xa, id_in=11 + i, id_click=24+i,
                                              id_out=9 + i, id_mode=1 + i, layer=LAYER_B))
            controls += 1

        for i in range(16):
                self.buttons.append(Button(self, index=controls, channel=0xa, id_in=32 + i, id_out=i, layer=LAYER_B))
                controls += 1


    #region UIControl

    def setOperationMode(self, mode: int):
        """
        Set the operation mode for this device

        :param mode: 0 for Standard MIDI Operation, 1 for MC Control emulation
        :return: None
        """
        msg = controlChange(self.globalChannel, 127, mode)
        self.sendMIDIMessage(msg)

    #Overrides IDevice
    def setLayer(self, layer: int):
        msg = programChange(self.globalChannel, layer)
        self.sendMIDIMessage(msg)

    #endregion

    # region Feedback
    # Overrides IDevice
    def setButtonLEDState(self, control: Button, state):

        msg = noteOn(self.globalChannel, control.idOut, state)
        self.sendMIDIMessage(msg)

    # Overrides IDevice
    def setFaderState(self, control: Fader, value):
        msg = controlChange(control.channel, control.idIn, value)
        self.sendMIDIMessage(msg)

    # Overrides IDevice
    def setRotaryLEDMode(self, control: RotaryEncoder, mode):
        msg = controlChange(self.globalChannel, control.idMode, mode)
        self.sendMIDIMessage(msg)

    # Overrides IDevice
    def setRotaryLEDState(self, control: RotaryEncoder, state):
        msg = controlChange(self.globalChannel, control.idOut, state)
        self.sendMIDIMessage(msg)

    # Overrides IDevice
    def setButtonValue(self, control: Button, value: bool):
        data = 127 if value else 0
        msg = noteOn(control.channel, control.idIn, data)
        self.sendMIDIMessage(msg)

    # Overrides IDevice
    def setFaderValue(self, control: Fader, value: int):
        pass # Not Suppoted by Hardware

    # Overrides IDevice
    def setRotaryValue(self, control: RotaryEncoder, value: int):
        msg = controlChange(control.channel, control.idIn, value)
        self.sendMIDIMessage(msg)

    # endregion