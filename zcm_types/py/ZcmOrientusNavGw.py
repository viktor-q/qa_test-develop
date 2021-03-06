"""ZCM type definitions
This file automatically generated by zcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

from ZcmOrientusVelocity import ZcmOrientusVelocity

from ZcmOrientusAccuracy import ZcmOrientusAccuracy

from ZcmOrientusFilterStatus import ZcmOrientusFilterStatus

from ZcmOrientusOrientation import ZcmOrientusOrientation

from ZcmOrientusSystemStatus import ZcmOrientusSystemStatus

from ZcmService import ZcmService

class ZcmOrientusNavGw(object):
    __slots__ = ["service", "orientusSystemStatus", "orientusFilterStatus", "orientusAccuracy", "orientusOrientation", "orientusVelocity"]

    def __init__(self):
        self.service = ZcmService()
        self.orientusSystemStatus = ZcmOrientusSystemStatus()
        self.orientusFilterStatus = ZcmOrientusFilterStatus()
        self.orientusAccuracy = ZcmOrientusAccuracy()
        self.orientusOrientation = ZcmOrientusOrientation()
        self.orientusVelocity = ZcmOrientusVelocity()

    def encode(self):
        buf = BytesIO()
        buf.write(ZcmOrientusNavGw._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        assert self.service._get_packed_fingerprint() == ZcmService._get_packed_fingerprint()
        self.service._encode_one(buf)
        assert self.orientusSystemStatus._get_packed_fingerprint() == ZcmOrientusSystemStatus._get_packed_fingerprint()
        self.orientusSystemStatus._encode_one(buf)
        assert self.orientusFilterStatus._get_packed_fingerprint() == ZcmOrientusFilterStatus._get_packed_fingerprint()
        self.orientusFilterStatus._encode_one(buf)
        assert self.orientusAccuracy._get_packed_fingerprint() == ZcmOrientusAccuracy._get_packed_fingerprint()
        self.orientusAccuracy._encode_one(buf)
        assert self.orientusOrientation._get_packed_fingerprint() == ZcmOrientusOrientation._get_packed_fingerprint()
        self.orientusOrientation._encode_one(buf)
        assert self.orientusVelocity._get_packed_fingerprint() == ZcmOrientusVelocity._get_packed_fingerprint()
        self.orientusVelocity._encode_one(buf)

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != ZcmOrientusNavGw._get_packed_fingerprint():
            raise ValueError("Decode error")
        return ZcmOrientusNavGw._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = ZcmOrientusNavGw()
        self.service = ZcmService._decode_one(buf)
        self.orientusSystemStatus = ZcmOrientusSystemStatus._decode_one(buf)
        self.orientusFilterStatus = ZcmOrientusFilterStatus._decode_one(buf)
        self.orientusAccuracy = ZcmOrientusAccuracy._decode_one(buf)
        self.orientusOrientation = ZcmOrientusOrientation._decode_one(buf)
        self.orientusVelocity = ZcmOrientusVelocity._decode_one(buf)
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if ZcmOrientusNavGw in parents: return 0
        newparents = parents + [ZcmOrientusNavGw]
        tmphash = (0xf26aad789c692d6c+ ZcmService._get_hash_recursive(newparents)+ ZcmOrientusSystemStatus._get_hash_recursive(newparents)+ ZcmOrientusFilterStatus._get_hash_recursive(newparents)+ ZcmOrientusAccuracy._get_hash_recursive(newparents)+ ZcmOrientusOrientation._get_hash_recursive(newparents)+ ZcmOrientusVelocity._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + ((tmphash>>63)&0x1)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if ZcmOrientusNavGw._packed_fingerprint is None:
            ZcmOrientusNavGw._packed_fingerprint = struct.pack(">Q", ZcmOrientusNavGw._get_hash_recursive([]))
        return ZcmOrientusNavGw._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

