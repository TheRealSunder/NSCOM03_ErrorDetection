
def binary_crc_remainder(dividend: str, divisor: str):
    # Convert binary strings to integers
    dividend = int(dividend, 2)
    divisor = int(divisor, 2)
    
    remainder = dividend
    
    divisor_length = divisor.bit_length()

    # Perform binary long division
    while remainder.bit_length() >= divisor_length:
        # Calculate shift amount to align divisor with the remainder
        shift_amount = remainder.bit_length() - divisor_length
        # Subtract the shifted divisor from the remainder using XOR
        remainder ^= (divisor << shift_amount)

    # Convert the final remainder to binary and return
    remainder_binary = bin(remainder)[2:]
    return remainder_binary.zfill(divisor_length - 1)  # Pad to match the CRC length

divisor = "110101"  
dividend = "1010011010"  


remainder = binary_crc_remainder(dividend, divisor)
print("Remainder:", remainder)
