# g^a mod p
# let i be the position of bit from the right(starting from 0)
# let b_i be the bit of the binary representation of a
# then g^a can be expressed as product of g^(b_i * 2^i) from 0 to (num_bit -1)
# when b_i = 0, g^(b_i * 2^i) = g^0 = 1, so it can be ignored
# when b_i = 1, g^(b_i * 2^i) = g^(2^i)
# so, g^a can be expressed as product of g^(2^i) from 0 to (num_bit -1) where i != 0
# let x_i be g^(2^i)
# then, x_i+1 = g^(2^i+1) = g^(2^i * 2) = (x_i)^2
# therefore, to proceed to the next term, we square the prev term
# let y_i be x_i mod p
# Modular Multiplication: (A * B) mod C = (A mod C * B mod C) mod C
# then y_i+1 = x_i+1 mod p = (x_i * x_i) mod p = (x_i mod p)^2 mod p = (y_i)^2 mod p
# then g^a mod p can be written as a sequence by
#   y_0 = x_0 mod p = g^(2^0) mod p = g mod p
#   y_i+1 = (y_i)^2 mod p for i = 0 to (num_bit - 1)


# g = base, a = exponenet, p = modulus, y = y_i from the sequence above
def mod_exp(g, a, p):
    r = 1
    y = g % p
    while a > 0:
        if a & 1 == 1:
            r = (r * y) % p
        y = y**2 % p
        a >>= 1
    return r
    
