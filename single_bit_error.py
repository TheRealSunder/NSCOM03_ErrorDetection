# SINGLE BIT ERROR
import random

def introduce_single_bit_error(data):
    """Simulates a single-bit error by flipping a random bit in the data."""
    index = random.randint(0, len(data) - 1)  # Randomly choose one bit to flip
    # Flip the chosen bit
    corrupted_data = data[:index] + ('1' if data[index] == '0' else '0') + data[index + 1:]
    return corrupted_data

# Example usage
original_data = "0100010001000111"  # Binary data as a string (16 bits)
print("Original Data:      ", original_data)

# Introduce a single-bit error
single_bit_error_data = introduce_single_bit_error(original_data)
print("Single-bit Error:   ", single_bit_error_data)
