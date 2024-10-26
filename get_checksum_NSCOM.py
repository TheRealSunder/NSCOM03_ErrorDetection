def getChecksum(data):
    # Separate data and checksum
    checksum = data[-1]  # Last element is the checksum
    actual_data = data[:-1]  # All elements except the last are data
    return checksum, actual_data

def calculate_checksum(data):
    # Calculate the sum of data elements
    total_sum = sum(data)
    
    # Wrap the sum to fit within 4 bits
    wrapped_sum = (total_sum & 0b1111) + (total_sum >> 4)
    
    # Calculate checksum as the 1's complement of the wrapped sum
    checksum = ~wrapped_sum & 0b1111
    return checksum

def sender(data):
    # Calculate checksum
    checksum = calculate_checksum(data)
    print(f"Sender - Data: {data}, Checksum: {checksum}")
    
    # Send data with checksum
    return data + [checksum]

def receiver(received_data):
    # Get checksum and actual data using the new getChecksum function
    received_checksum, data = getChecksum(received_data)
    
    # Calculate the sum including the received checksum
    total_sum = sum(data) + received_checksum
    
    # Wrap the sum to fit within 4 bits
    wrapped_sum = (total_sum & 0b1111) + (total_sum >> 4)
    
    # Verify by taking 1's complement of the wrapped sum
    verification_result = ~wrapped_sum & 0b1111
    
    if verification_result == 0:
        print(f"Receiver - Data received correctly: {data}, Checksum: {received_checksum}")
    else:
        print(f"Receiver - Error detected in received data: {data}, Checksum: {received_checksum}")

# Convert "NSCOM3" to ASCII values
data_string = "NSCOM3"
data = [ord(char) for char in data_string]  # Get ASCII values

# Sender sends the data with checksum
sent_data = sender(data)

# Receiver receives the data and verifies it
receiver(sent_data)
