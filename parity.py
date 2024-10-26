#PARITY

def add_parity_bit(data, parity_type='even'):
    """Calculates and adds a parity bit to the data for error detection."""
    count_of_ones = data.count('1')
    if parity_type == 'even':
        parity_bit = '1' if count_of_ones % 2 != 0 else '0'
    else:  # Odd parity
        parity_bit = '0' if count_of_ones % 2 != 0 else '1'
    return data + parity_bit

def check_parity(data_with_parity, parity_type='even'):
    """Checks if data with parity bit has an error based on the parity type."""
    data = data_with_parity[:-1]
    received_parity = data_with_parity[-1]
    count_of_ones = data.count('1')
    
    if parity_type == 'even':
        expected_parity = '1' if count_of_ones % 2 != 0 else '0'
    else:  # Odd parity
        expected_parity = '0' if count_of_ones % 2 != 0 else '1'
    
    return received_parity == expected_parity

# Example usage with even parity
original_data = "1011101"
print("Original Data:        ", original_data)

# Add even parity bit
data_with_parity = add_parity_bit(original_data, parity_type='even')
print("Data with Even Parity:", data_with_parity)

# Check for errors
if check_parity(data_with_parity, parity_type='even'):
    print("No error detected with even parity.")
else:
    print("Error detected with even parity.")
    
# Example usage with odd parity
data_with_parity = add_parity_bit(original_data, parity_type='odd')
print("Data with Odd Parity: ", data_with_parity)

# Check for errors
if check_parity(data_with_parity, parity_type='odd'):
    print("No error detected with odd parity")
else:
    print("Error detected with odd parity D:")
