"""ZCM type definitions
This file automatically generated by zcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class ZcmOrientusSystemStatus(object):
    __slots__ = ["systemFailure", "accelerometerSensorFailure", "gyroscopeSensorFailure", "magnetometerSensorFailure", "accelerometerOverRange", "gyroscopeOverRange", "magnetometerOverRange", "minimumTemperatureAlarm", "maximumTemperatureAlarm", "lowVoltageAlarm", "highVoltageAlarm", "dataOutputOverflowAlarm"]

    def __init__(self):
        self.systemFailure = False
        self.accelerometerSensorFailure = False
        self.gyroscopeSensorFailure = False
        self.magnetometerSensorFailure = False
        self.accelerometerOverRange = False
        self.gyroscopeOverRange = False
        self.magnetometerOverRange = False
        self.minimumTemperatureAlarm = False
        self.maximumTemperatureAlarm = False
        self.lowVoltageAlarm = False
        self.highVoltageAlarm = False
        self.dataOutputOverflowAlarm = False

    def encode(self):
        buf = BytesIO()
        buf.write(ZcmOrientusSystemStatus._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">bbbbbbbbbbbb", self.systemFailure, self.accelerometerSensorFailure, self.gyroscopeSensorFailure, self.magnetometerSensorFailure, self.accelerometerOverRange, self.gyroscopeOverRange, self.magnetometerOverRange, self.minimumTemperatureAlarm, self.maximumTemperatureAlarm, self.lowVoltageAlarm, self.highVoltageAlarm, self.dataOutputOverflowAlarm))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != ZcmOrientusSystemStatus._get_packed_fingerprint():
            raise ValueError("Decode error")
        return ZcmOrientusSystemStatus._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = ZcmOrientusSystemStatus()
        self.systemFailure = bool(struct.unpack('b', buf.read(1))[0])
        self.accelerometerSensorFailure = bool(struct.unpack('b', buf.read(1))[0])
        self.gyroscopeSensorFailure = bool(struct.unpack('b', buf.read(1))[0])
        self.magnetometerSensorFailure = bool(struct.unpack('b', buf.read(1))[0])
        self.accelerometerOverRange = bool(struct.unpack('b', buf.read(1))[0])
        self.gyroscopeOverRange = bool(struct.unpack('b', buf.read(1))[0])
        self.magnetometerOverRange = bool(struct.unpack('b', buf.read(1))[0])
        self.minimumTemperatureAlarm = bool(struct.unpack('b', buf.read(1))[0])
        self.maximumTemperatureAlarm = bool(struct.unpack('b', buf.read(1))[0])
        self.lowVoltageAlarm = bool(struct.unpack('b', buf.read(1))[0])
        self.highVoltageAlarm = bool(struct.unpack('b', buf.read(1))[0])
        self.dataOutputOverflowAlarm = bool(struct.unpack('b', buf.read(1))[0])
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if ZcmOrientusSystemStatus in parents: return 0
        tmphash = (0xaa4d6bf9888ccf56) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + ((tmphash>>63)&0x1)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if ZcmOrientusSystemStatus._packed_fingerprint is None:
            ZcmOrientusSystemStatus._packed_fingerprint = struct.pack(">Q", ZcmOrientusSystemStatus._get_hash_recursive([]))
        return ZcmOrientusSystemStatus._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

