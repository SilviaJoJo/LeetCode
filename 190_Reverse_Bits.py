class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        1. initialize a vairable: 32-bit 0, called ans
        2. execute the following loop for 32 times:
            3. left shift ans for 1 bit
            4. if the last bit of n is 1, change the last bit of ans to 1
            5. else, do nothing
            6. right shift n for one bit

        Time: O(1)
        Space: O(1)
        '''
        ans = 0
        for _ in range(32):
            # this is the shorthand for ans = ans << 1
            # don't forget to assign the value after shifting!
            ans <<= 1
            # n & 1 (which is 000...1) checks the last bit
            if (n & 1):
                ans += 1
            n >>= 1
        return ans