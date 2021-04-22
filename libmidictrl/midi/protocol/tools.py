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
    """
    Generates a new MIDI Message

    :param status: Status Code
    :param channel: Channel for the message
    :param data1: first data byte
    :param data2: second data byte, or None if the message type has only 2 bytes
    :return: a list containing the message
    """
    message = [generateStatus(status, channel), data1 & 0xff]
    if data2 is not None:
        message.append(data2 & 0xff)
    return message


def noteOff(channel: int, note:int, intensity:int):
    """
    Generates a NOTE OFF Command

    :param channel: Channel of the command
    :param note: MIDI Note code
    :param intensity: Intensity of the note
    :return: the generated message
    """
    return generateMessage(STATUS_NOTE_OFF, channel, note, intensity)


def noteOn(channel: int, note:int, intensity:int):
    """
    Generates a NOTE ON Command

    :param channel: Channel of the command
    :param note: MIDI Note code
    :param intensity: Intensity of the note
    :return: the generated message
    """
    return generateMessage(STATUS_NOTE_ON, channel, note, intensity)


def polyphonicAftertouch(channel: int, note:int, intensity:int):
    """
    Generates a POLYPHONIC AFTERTOUCH Command

    :param channel: Channel of the command
    :param note: MIDI Note code
    :param intensity: Intensity of the note
    :return: the generated message
    """
    return generateMessage(STATUS_POLYPHONIC_AFTERTOUCH, channel, note, intensity)


def controlChange(channel: int, controller:int, state:int):
    """
    Generates a CONTROL CHANGE Command

    :param channel: Channel of the command
    :param controller: Controller to set
    :param state: State to set the controller to
    :return: the generated message
    """
    return generateMessage(STATUS_CONTROL_CHANGE, channel, controller, state)


def programChange(channel: int, instrument: int):
    """
    Generates a PROGRAM CHANGE Command

    :param channel: Channel of the command
    :param instrument: Instrument to play on this channel
    :return: the generated message
    """
    return generateMessage(STATUS_PROGRAM_CHANGE, channel, instrument)


def monophonic(channel: int, intensity: int):
    """
    Generates a MONOPHONIC / CHANNEL AFTERTOUCH Command

    :param channel: Channel of the command
    :param intensity: new Intensity for all currently active notes
    :return: the generated message
    """
    return generateMessage(STATUS_PROGRAM_CHANGE, channel, intensity)


def pitchBending(channel: int, data1:int, data2:int):
    """
    Generates a PITCH BENDING Command

    :param channel: Channel of the command
    :param data1: minor byte
    :param data2: major byte
    :return: the generated message
    """
    return generateMessage(STATUS_CONTROL_CHANGE, channel, data1, data2)
