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

class IDevice:

    #region Events
    def addEventListener(self, control, note, callback):
        pass

    def removeEventListener(self, control, note, callback):
        pass

    def callEventListeners(self, control, note, message, deltatime):
        pass

    #endregion

    #region Controls

    def getButtons(self) -> list:
        return []

    def getFaders(self) -> list:
        return []

    def getRotaryEncoders(self) -> list:
        return []

    #endregion

    #region UIControl

    def setLayer(self, layer : int):
        pass

    #endregion

    #region Feedback

    def sendMIDIMessage(self, message):
        pass

    def setButtonLEDState(self, control, state):
        pass

    def setRotaryLEDMode(self, control, mode):
        pass

    def setRotaryLEDState(self, control, state):
        pass

    def setFaderState(self, control, value):
        pass

    def setButtonValue(self, control, value):
        pass

    def setFaderValue(self, control, value):
        pass

    def setRotaryValue(self, control, value):
        pass
    #endregion