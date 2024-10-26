def getChecksum(data):
    checksum = data[-1]
    actual_data = data[:-1]
    return checksum, actual_data

def calculate_checksum(data):
    total_sum = sum(data)
    wrapped_sum = (total_sum & 0b1111) + (total_sum >> 4)
    checksum = ~wrapped_sum & 0b1111
    return checksum

def sender(data):
    checksum = calculate_checksum(data)
    print(f"Sender - Data: {data}, Checksum: {checksum}")
    return data + [checksum]

def receiver(received_data):
    received_checksum, data = getChecksum(received_data)
    total_sum = sum(data) + received_checksum
    wrapped_sum = (total_sum & 0b1111) + (total_sum >> 4)
    verification_result = ~wrapped_sum & 0b1111
    if verification_result == 0:
        print(f"Receiver - Data received correctly: {data}, Checksum: {received_checksum}")
    else:
        print(f"Receiver - Error detected in received data: {data}, Checksum: {received_checksum}")

data_string = "NSCOM3"
data = [ord(char) for char in data_string]
sent_data = sender(data)
receiver(sent_data)
