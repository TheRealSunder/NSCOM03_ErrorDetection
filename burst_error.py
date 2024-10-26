# BURST ERROR
import random

def introduce_burst_error(data, burst_length):
    """Simulates a burst error by flipping a sequence of bits in the data."""
    start = random.randint(0, len(data) - burst_length)  # Start point for burst error
    corrupted_data = list(data)
    # Flip a sequence of bits of specified length
    for i in range(start, start + burst_length):
        corrupted_data[i] = '1' if corrupted_data[i] == '0' else '0'
    return ''.join(corrupted_data)

# Example usage
original_data = "0100010001000111"  # Binary data as a string (16 bits)
print("Original Data:      ", original_data)

# Introduce a burst error of length 8
burst_error_data = introduce_burst_error(original_data, burst_length=8)
print("Burst Error (8 bits):", burst_error_data)
