import random

def calculate_parity(data):
    """Calculates even parity bit for data."""
    count_of_ones = data.count('1')
    # Return 1 if count of 1's is odd (to make it even), else 0
    parity_bit = '1' if count_of_ones % 2 != 0 else '0'
    return parity_bit

def add_parity_bit(data):
    """Appends the parity bit to the data."""
    parity_bit = calculate_parity(data)
    return data + parity_bit

def introduce_error(data):
    """Simulates an error by flipping a random bit."""
    index = random.randint(0, len(data) - 1)
    corrupted_data = list(data)
    corrupted_data[index] = '1' if corrupted_data[index] == '0' else '0'
    return ''.join(corrupted_data)

def check_parity(data_with_parity):
    """Checks if data has an error by recalculating the parity."""
    data = data_with_parity[:-1]  # Exclude the parity bit
    received_parity = data_with_parity[-1]
    calculated_parity = calculate_parity(data)
    return received_parity == calculated_parity

# Example usage
original_data = "1101001"  # Example data (7 bits)
print("Original Data:        ", original_data)

# Add parity bit
data_with_parity = add_parity_bit(original_data)
print("Data with Parity Bit: ", data_with_parity)

# Introduce an error
corrupted_data = introduce_error(data_with_parity)
print("Corrupted Data:       ", corrupted_data)

# Check if an error is detected
if check_parity(corrupted_data):
    print("No error detected.")
else:
    print("Error detected!")
