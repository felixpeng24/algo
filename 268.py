"""
Given a 32-bit positive integer N, determine whether it is a power of four in faster than O(log N) time.

"""

#is it a bit manipulation typa deal??
#powers of four: 4 16, 64, 256....
#yea its def bits


def is_power_of_four(N):
    return N > 0 and (N & (N - 1)) == 0 and (N & 0x55555555) != 0






