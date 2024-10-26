def binary_crc_remainder(dividend: str, divisor: str) -> str:
    dividend = int(dividend, 2)
    divisor = int(divisor, 2)

    remainder = dividend << (divisor.bit_length() - 1)

    while remainder.bit_length() >= divisor.bit_length():
        shift_amount = remainder.bit_length() - divisor.bit_length()
        remainder ^= (divisor << shift_amount)

    remainder_binary = bin(remainder)[2:]
    return remainder_binary.zfill(divisor.bit_length() - 1)

divisor = "100110000010001110110110111"
dividend = "1010011010"

remainder = binary_crc_remainder(dividend, divisor)
print("CRC-32 Remainder:", remainder)