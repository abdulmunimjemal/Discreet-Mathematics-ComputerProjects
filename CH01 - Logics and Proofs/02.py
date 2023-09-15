"""
Given two bit strings of length n, find the bitwise AND,
bitwise OR, and bitwise XOR of these strings.
"""

def bitwise(bit_string1: str, bit_string2: str) -> str:
    if len(bit_string1) != len(bit_string2):
        print("The bit length should be equal")
        return None

    n = len(bit_string1)
    
    # intial results
    bitwise_and = ""
    bitwise_or = ""
    bitwise_xor = ""
    
    # perform bitwise operations
    for i in range(n):
        bit1 = int(bit_string1[i])
        bit2 = int(bit_string2[i])
        
        bitwise_and += str(bit1 & bit2)
        bitwise_or += str(bit1 | bit2)
        bitwise_xor += str(bit1 ^ bit2)
    
    return bitwise_and, bitwise_or, bitwise_xor