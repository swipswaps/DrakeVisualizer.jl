"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import drakevis.lcmt_viewer_link_data

class lcmt_viewer_load_robot(object):
    __slots__ = ["num_links", "link"]

    def __init__(self):
        self.num_links = 0
        self.link = []

    def encode(self):
        buf = BytesIO()
        buf.write(lcmt_viewer_load_robot._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">i", self.num_links))
        for i0 in range(self.num_links):
            assert self.link[i0]._get_packed_fingerprint() == drakevis.lcmt_viewer_link_data._get_packed_fingerprint()
            self.link[i0]._encode_one(buf)

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != lcmt_viewer_load_robot._get_packed_fingerprint():
            raise ValueError("Decode error")
        return lcmt_viewer_load_robot._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = lcmt_viewer_load_robot()
        self.num_links = struct.unpack(">i", buf.read(4))[0]
        self.link = []
        for i0 in range(self.num_links):
            self.link.append(drakevis.lcmt_viewer_link_data._decode_one(buf))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if lcmt_viewer_load_robot in parents: return 0
        newparents = parents + [lcmt_viewer_load_robot]
        tmphash = (0x739e6927d8bcec39+ drakevis.lcmt_viewer_link_data._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if lcmt_viewer_load_robot._packed_fingerprint is None:
            lcmt_viewer_load_robot._packed_fingerprint = struct.pack(">Q", lcmt_viewer_load_robot._get_hash_recursive([]))
        return lcmt_viewer_load_robot._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
