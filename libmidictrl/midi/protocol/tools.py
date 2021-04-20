from typing import Optional

from .constants import *


def generateStatus(status, channel):
    """
    Generates the status byte for MIDI messages

    :param status: Status Code (first 4 bits), (0x80 - 0xF0)
    :param channel: Channel Code (last 4 bits) (0x00 - 0x0F)
    :return:
    """
    return (status & 0xF0) + (channel & 0x0F)


def generateMessage(status : int, channel : int, data1 : int, data2 : Optional[int] = None):
    message = [generateStatus(status, channel), data1 & 0xff]
    if data2 is not None:
        message.append(data2 & 0xff)
    return message


def noteOff(channel: int, note:int, intensity:int):
    return generateMessage(STATUS_NOTE_OFF, channel, note, intensity)


def noteOn(channel: int, note:int, intensity:int):
    return generateMessage(STATUS_NOTE_ON, channel, note, intensity)


def polyphonicAftertouch(channel: int, note:int, intensity:int):
    return generateMessage(STATUS_POLYPHONIC_AFTERTOUCH, channel, note, intensity)


def controlChange(channel: int, controller:int, state:int):
    return generateMessage(STATUS_CONTROL_CHANGE, channel, controller, state)


def programChange(channel: int, instrument: int):
    return generateMessage(STATUS_PROGRAM_CHANGE, channel, instrument)


def monophonic(channel: int, intensity: int):
    return generateMessage(STATUS_PROGRAM_CHANGE, channel, intensity)


def pitchBending(channel: int, data1:int, data2:int):
    return generateMessage(STATUS_CONTROL_CHANGE, channel, data1, data2)
