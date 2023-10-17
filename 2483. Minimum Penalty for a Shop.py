"""You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

if the ith character is 'Y', it means that customers come at the ith hour
whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.

 

Example 1:

Input: customers = "YYNY"
Output: 2
Explanation: 
- Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.
Example 2:

Input: customers = "NNNNN"
Output: 0
Explanation: It is best to close the shop at the 0th hour as no customers arrive."""


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix_N = [0] * (n+1)
        postfix_Y = [0] * (n+1)

        # counting N values for prefix
        for i in range(1, n+1):
            prefix_N[i] = prefix_N[i-1]
            if customers[i-1] == 'N':
                prefix_N[i] += 1

        # counting Y values for postfix
        for i in range(n-1, -1, -1):
            postfix_Y[i] = postfix_Y[i+1]
            if customers[i] == 'Y':
                postfix_Y[i] += 1

        min_penality, idx = float('inf'), 0
        for i in range(n+1):
            score = prefix_N[i] + postfix_Y[i]
            if score < min_penality:
                min_penality = score
                idx = i
        return idx
