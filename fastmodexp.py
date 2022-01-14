# g^a mod p
# let i be the position of bit from the right(starting from 0)
# let b_i be the bit of the binary representation of a
# then g^a can be expressed as product of g^(b_i * 2^i); for i: 0 to (num_bit -1)
# There are two different cases of b_i:
#   when b_i = 0, g^(b_i * 2^i) = g^0 = 1, so it can be ignored
#   when b_i = 1, g^(b_i * 2^i) = g^(2^i)
# so, g^a can be expressed as product of g^(2^i) for i: 0 to (num_bit -1) where i != 0

# let x_i be g^(2^i)
# then, x_(i+1) = g^(2^(i+1)) = g^(2^i * 2) = (g^(2^i)) ^ 2 = (x_i)^2
# therefore, to proceed to the next term, we square the prev term
# let y_i be x_i mod p

# Modular Multiplication: (A * B) mod C = (A mod C * B mod C) mod C

# then y_(i+1) = x_(i+1) mod p = (x_i * x_i) mod p = (x_i mod p)^2 mod p = (y_i)^2 mod p (line 15)
# then g^a mod p can be written as a (product of the sequence) mod p:
#   y_0 = x_0 mod p = g^(2^0) mod p = g mod p
#   y_(i+1) = (y_i)^2 mod p for i: 0 to (num_bit-1)


# g = base, a = exponenet, p = modulus, y = y_i from the sequence above
def mod_exp(g, a, p):
    # r is a product of all y values (y_0 ....... y_(numbit-1)
    r = 1
    # y_0 is g mod p (line 19)
    y = g % p
    while a > 0:
        # when the leftmost bit is set to 1 (line 7)
        if a & 1 == 1:
            # product of y_i and y_(i+1)
            # mod p is necessary bcause the product can easily exceed p
            r = (r * y) % p
        # move y_i to y_(i+1) (line 20)
        y = y**2 % p
        # move to the next bit in a
        a >>= 1
    return r
    
