def two_dimensional_parity(binary_data):
    row_parity = [str(binary.count('1') % 2) for binary in binary_data]
    

    col_parity = ''.join([str(sum(int(row[i]) for row in binary_data) % 2) for i in range(len(binary_data[0]))])

    return row_parity, col_parity


binary_data = [
    "1100111",
    "1011101",
    "0111001",  
    "0101001"
]

row_parity, col_parity = two_dimensional_parity(binary_data)


for binary, parity in zip(binary_data, row_parity):
    print(f"{binary} | Parity: {parity}")

print(f"Column Parity: {''.join(col_parity)}")  

# Output for parity
print("\nParity Check")
for binary, parity in zip(binary_data, row_parity):
    print(f"{binary} with parity bit: {parity}")
print(f"Column Parity: {''.join(col_parity)}\n") 
