import ctypes
import struct


def key_usage_unpack(data: bytes) -> dict[str, bool]:
    # https://stackoverflow.com/a/11481471/3253026
    class Flags_bits(ctypes.BigEndianStructure):
        _fields_ = [
            ("digital_signature", ctypes.c_uint16, 1),
            ("content_comitment", ctypes.c_uint16, 1),
            ("key_encipherment", ctypes.c_uint16, 1),
            ("data_encipherment", ctypes.c_uint16, 1),
            ("key_agreement", ctypes.c_uint16, 1),
            ("key_cert_sign", ctypes.c_uint16, 1),
            ("crl_sign", ctypes.c_uint16, 1),
            ("decipher_only", ctypes.c_uint16, 1),
            ("encipher_only", ctypes.c_uint16, 1),
            # ("unknown", ctypes.c_uint16, 7),
        ]

    class Flags(ctypes.Union):
        _fields_ = [("b", Flags_bits), ("asword", ctypes.c_uint16)]

    flags = Flags()
    # flags.asword = data[0] * 256 + data[1]
    flags.asword = struct.unpack(">H", data)[0]

    return {
        "digital_signature": flags.b.digital_signature == 1,
        "content_comitment": flags.b.content_comitment == 1,
        "key_encipherment": flags.b.key_encipherment == 1,
        "data_encipherment": flags.b.data_encipherment == 1,
        "key_agreement": flags.b.key_agreement == 1,
        "key_cert_sign": flags.b.key_cert_sign == 1,
        "crl_sign": flags.b.crl_sign == 1,
        "decipher_only": flags.b.decipher_only == 1,
        "encipher_only": flags.b.encipher_only == 1,
    }
