#!/usr/bin/python3
""" UTF-8 Validation """

def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    byte_count = 0

    bit_mask_1 = 1 << 7
    bit_mask_2 = 1 << 6

    for byte in data:

        current_bit_mask = 1 << 7

        if byte_count == 0:

            while current_bit_mask & byte:
                byte_count += 1
                current_bit_mask = current_bit_mask >> 1

            if byte_count == 0:
                continue

            if byte_count == 1 or byte_count > 4:
                return False

        else:
            if not (byte & bit_mask_1 and not (byte & bit_mask_2)):
                return False

        byte_count -= 1

    if byte_count == 0:
        return True

    return False
