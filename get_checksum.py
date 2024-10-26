def calculate_checksum(data):
    total = sum(data)
    while total > 15:
        total = (total & 0xF) + (total >> 4)
    checksum = ~total & 0xF
    return checksum

def sender(data):
    sender_checksum = calculate_checksum(data)
    sent_data = data + [sender_checksum]
    print(f"Sender Checksum: {sender_checksum}")
    print(f"Data sent: {sent_data}")
    return sent_data

def receiver(sent_data):
    receiver_checksum = calculate_checksum(sent_data)
    print(f"Receiver Checksum: {receiver_checksum}")
    if receiver_checksum == 0:
        print("Data received successfully with no errors.")
    else:
        print("Error detected in received data.")

data = [7, 11, 12, 0, 6]
sent_data = sender(data)
receiver(sent_data)
