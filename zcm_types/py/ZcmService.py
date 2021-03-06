"""ZCM type definitions
This file automatically generated by zcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class ZcmService(object):
    __slots__ = ["timestamp", "processing"]

    def __init__(self):
        self.timestamp = 0
        self.processing = 0

    def encode(self):
        buf = BytesIO()
        buf.write(ZcmService._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qi", self.timestamp, self.processing))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != ZcmService._get_packed_fingerprint():
            raise ValueError("Decode error")
        return ZcmService._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = ZcmService()
        self.timestamp, self.processing = struct.unpack(">qi", buf.read(12))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if ZcmService in parents: return 0
        tmphash = (0xab017a94ae37fdad) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + ((tmphash>>63)&0x1)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if ZcmService._packed_fingerprint is None:
            ZcmService._packed_fingerprint = struct.pack(">Q", ZcmService._get_hash_recursive([]))
        return ZcmService._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

