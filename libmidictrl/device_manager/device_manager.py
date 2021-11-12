from typing import List, Optional, Dict

import rtmidi


from ..devices.device_interface import IDevice

from ..devices.behringer.xtouch_compact import XTouchCompact
from ..devices.behringer.xtouch_mini import XTouchMini

__DEVICE_LIST: Optional[List[IDevice]] = None

__DEVICE_DICT: Dict[str, type] = {
    "X-TOUCH COMPACT": XTouchCompact,
    "X-TOUCH MINI": XTouchMini

}


def registerDeviceType (midi_port_prefix: str, device: type):
    __DEVICE_DICT[midi_port_prefix] = device


def getDevices() -> List[IDevice]:
    global __DEVICE_LIST
    if __DEVICE_LIST is not None:
        return __DEVICE_LIST

    midiout = rtmidi.MidiOut()
    midiin = rtmidi.MidiIn()

    out_ports = midiout.get_ports()
    in_ports = midiin.get_ports()

    out_port_lut = {}
    for i in range(len(out_ports)):
        out_port_lut[out_ports[i]] = i

    in_port_lut = {}
    for i in range(len(in_ports)):
        in_port_lut[in_ports[i]] = i

    out_sorted = sortDevicesByType(out_ports)
    in_sorted = sortDevicesByType(in_ports)

    __DEVICE_LIST = []

    for k in in_sorted:
        in_sorted[k].sort()
        out_sorted[k].sort()

        devices = min(len(in_sorted[k]), len(out_sorted[k]))

        for i in range(devices):
            __DEVICE_LIST.append(__DEVICE_DICT[k]("{}-{}".format(k, i), in_port_lut[in_sorted[k][i]],
                                                  out_port_lut[out_sorted[k][i]]))

    return __DEVICE_LIST


def sortDevicesByType(ports: List[str]):
    result = {}

    for k in __DEVICE_DICT:
        for p in ports:
            if p.startswith(k):
                if k not in result:
                    result[k] = []
                result[k].append(p)

    return result
