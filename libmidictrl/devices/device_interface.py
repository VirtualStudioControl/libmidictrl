
class IDevice:
    """
    Interface declaring methods all devices must implement
    """

    def getDeviceID(self) -> str:
        """
        :return: a identifying String for this device
        """
        return ""

    def getDeviceName(self):
        """
        :return: the model name of this device
        """
        return ""

    def getDeviceManufacturer(self):
        """
        :return: the manufacturer name of this device
        """
        return ""

    def open(self):
        """
        Open the MIDI ports for this Device
        :return:
        """
        pass

    def close(self):
        """
        Close the MIDI ports for this Device
        :return:
        """
        pass

    #region Events
    def addEventListener(self, control: int, note:int, callback):
        """
        Adds a Event Listener for a MIDI Listener

        :param control: Control Byte to listen for
        :param note: MIDI Device Index to listen for
        :param callback: callback function to call
        :return: None
        """
        pass

    def removeEventListener(self, control, note, callback):
        """
        Removes a Event Listener for a MIDI Listener

        :param control: Control Byte to listen for
        :param note: MIDI Device Index to listen for
        :param callback: callback function to remove
        :return: None
        """
        pass

    def callEventListeners(self, control, note, message, deltatime):
        """
        Calls the callbacks for all event listeners which meet the criteria

        :param control: Control Byte to listen for
        :param note: MIDI Device Index to listen for
        :param message: Full message received
        :param deltatime: deltatime received with the event
        :return: None
        """
        pass

    #endregion

    #region Controls

    def getButtons(self) -> list:
        """
        :return: a list of all buttons for this controller
        """
        return []

    def getFaders(self) -> list:
        """
        :return: a list of all faders for this controller
        """
        return []

    def getRotaryEncoders(self) -> list:
        """
        :return: a list of all rotary encoders for this controller
        """
        return []

    #endregion

    #region UIControl

    def setLayer(self, layer: int):
        """
        Sets the active layer of the device
        :param layer: layer index of the layer to set active
        :return: None
        """
        pass

    #endregion

    #region Feedback

    def sendMIDIMessage(self, message):
        """
        Sends the given Message to the device

        :param message: Message to send
        :return: None
        """
        pass

    def setButtonLEDState(self, control, state):
        """
        Set the LED State of the given Button control

        **THIS IS NOT LAYER AWARE. FOR LAYER AWARE SETTING OF LEDS, SEE setButtonValue()**

        :param control: Button Control to set LED of
        :param state: State to set the LED to set
        :return: None
        """
        pass

    def setRotaryLEDMode(self, control, mode):
        """
        Set the LED Ring Mode of the given Rotary Encoder control

        **THIS IS NOT LAYER AWARE. FOR LAYER AWARE SETTING OF LEDS, SEE setButtonValue()**

        :param control: Rotary Encoder Control to set LED of
        :param mode: State to set the LED to set
        :return: None
        """
        pass

    def setRotaryLEDState(self, control, state):
        """
        Set the LED State of the given Rotary Encoder control.

        **THIS IS NOT LAYER AWARE. FOR LAYER AWARE SETTING OF LEDS, SEE setButtonValue()**

        :param control: Rotary Encoder Control to set LED of
        :param state: State to set the LED to set
        :return: None
        """
        pass

    def setFaderState(self, control, value):
        """
        Set the State of the given Fader control.

        **THIS IS NOT LAYER AWARE. FOR LAYER AWARE SETTING OF LEDS, SEE setButtonValue()**

        :param control: Control to set LED of
        :param state: State to set the LED to set
        :return: None
        """
        pass

    def setButtonValue(self, control, value):
        """
        Set the Value for the given Control (Layer Aware)

        :param control: Button to set the Value for
        :param value: Value to set (True or False)
        :return: None
        """
        pass

    def setFaderValue(self, control, value):
        """
        Set the Value for the given Control (Layer Aware)

        :param control: Fader to set the Value for
        :param value: Value to set (0 to 127)
        :return: None
        """
        pass

    def setRotaryValue(self, control, value):
        """
        Set the Value for the given Control (Layer Aware)

        :param control: Rotary Encoder to set the Value for
        :param value: Value to set (0 to 127)
        :return: None
        """
        pass
    #endregion