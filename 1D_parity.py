def one_dimensional_parity(binary_data):
    total_ones = sum(binary.count('1') for binary in binary_data)
    parity_bit = str(total_ones % 2)
    return parity_bit

binary_data = [
    "1100111",
    "1011101",
    "1111001",  
    "0101001"
]

parity_bit = one_dimensional_parity(binary_data)

for binary in binary_data:
    print(f"{binary}")

print(f"Overall Parity Bit: {parity_bit}")

print("\n--- PARITY CHECK ---")
print(f"Data: {''.join(binary_data)} with parity bit: {parity_bit}\n")
