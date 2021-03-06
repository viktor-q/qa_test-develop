"""ZCM type definitions
This file automatically generated by zcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class ZcmOrientusVelocity(object):
    __slots__ = ["angularVelocity_X", "angularVelocity_Y", "angularVelocity_Z", "acceleration_X", "acceleration_Y", "acceleration_Z", "angularAcceleration_X", "angularAcceleration_Y", "angularAcceleration_Z"]

    def __init__(self):
        self.angularVelocity_X = 0.0
        self.angularVelocity_Y = 0.0
        self.angularVelocity_Z = 0.0
        self.acceleration_X = 0.0
        self.acceleration_Y = 0.0
        self.acceleration_Z = 0.0
        self.angularAcceleration_X = 0.0
        self.angularAcceleration_Y = 0.0
        self.angularAcceleration_Z = 0.0

    def encode(self):
        buf = BytesIO()
        buf.write(ZcmOrientusVelocity._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">fffffffff", self.angularVelocity_X, self.angularVelocity_Y, self.angularVelocity_Z, self.acceleration_X, self.acceleration_Y, self.acceleration_Z, self.angularAcceleration_X, self.angularAcceleration_Y, self.angularAcceleration_Z))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != ZcmOrientusVelocity._get_packed_fingerprint():
            raise ValueError("Decode error")
        return ZcmOrientusVelocity._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = ZcmOrientusVelocity()
        self.angularVelocity_X, self.angularVelocity_Y, self.angularVelocity_Z, self.acceleration_X, self.acceleration_Y, self.acceleration_Z, self.angularAcceleration_X, self.angularAcceleration_Y, self.angularAcceleration_Z = struct.unpack(">fffffffff", buf.read(36))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if ZcmOrientusVelocity in parents: return 0
        tmphash = (0x7b90382042d22ff2) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + ((tmphash>>63)&0x1)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if ZcmOrientusVelocity._packed_fingerprint is None:
            ZcmOrientusVelocity._packed_fingerprint = struct.pack(">Q", ZcmOrientusVelocity._get_hash_recursive([]))
        return ZcmOrientusVelocity._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

