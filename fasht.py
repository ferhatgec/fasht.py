# MIT License
#
# Copyright (c) 2021 Ferhat Geçdoğan All Rights Reserved.
# Distributed under the terms of the MIT License.
#
# Fasht[dot]py - Python3 implementation of Fasht (lib)
#
# fas(h)t hash algorithm for non-cryptographic uses.
# designed & implemented for gretea language.
#
# github.com/ferhatgec/fasht.py

rounds = [0x2, 0x5, 0x7d5, 0x7e5]


def h(data: str) -> str:
    ascii_data = [ord(c) for c in data]
    table = []
    result: str = ''

    for __round in rounds:
        for ch in ascii_data:
            table.append((ch << 2) ^ __round)

    for arg in table:
        result += hex(arg >> 2)[-1]

    if len(result) > 32:
        result = result[0:32]
    else:
        h(result)

    return result


def hb(data: str) -> int:
    return int(h(data), 16)
