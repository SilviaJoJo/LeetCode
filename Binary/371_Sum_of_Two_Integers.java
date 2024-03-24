class Solution {
    public int getSum(int a, int b) {
        /** the core idea is to implement bitwise operation 
        * bitwise xor: ^
        * bitwise and: &
        * bitwise shift: << or >> 
        
        * Time: O(1) -- a and b are small numbers
        * Space: O(1) -- no extra data structures 
        * Another solution is also available! */
        while (b != 0) {
            int carryIn = (a & b) << 1;
            a = a ^ b; // store a as the xor result
            b = carryIn; // store b as the carry in
        }
        return a;
    }
}