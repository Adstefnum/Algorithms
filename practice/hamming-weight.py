def hammingWeight(self, x: int) -> int:
        x -= (x >> 1) & 0x5555555555555555
        x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
        x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
        return ((x * 0x0101010101010101) & 0xffffffffffffffff ) >> 56
