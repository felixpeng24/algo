"""

This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, 
return 0000 1111 0000 1111 0000 1111 0000 1111.
"""

#pointer at each end, then swap?

def reverse_bits(n):
    binary_str = bin(n)[2:].zfill(32)  # Convert to binary, remove '0b', and pad to 32 bits
    reversed_str = binary_str[::-1]  # Reverse the string
    return int(reversed_str, 2)  # Convert back to integer

# Example usage:
n = int("11110000111100001111000011110000", 2)  # Convert from binary to integer
result = reverse_bits(n)
print(f"Reversed binary: {bin(result)[2:].zfill(32)}")  # Print as 32-bit binary
