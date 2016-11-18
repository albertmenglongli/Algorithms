#Integer Multiplication
**Basically** 

12\*13

= 1\*1\*10^2 + 1\*3\*10^1 + 2\*1\*10^1 + 2\*3

And four parts need to be calculated, which make it T(n) <= 4T(n/2) + cn = O(n^log4) = O(n^2)

**Improved**

12 * 13

= (1 * 10 +2 ) * (1 * 10 + 3)

= 1 * 1 * 10^2 + (1 * 3 + 2 * 1 ) * 10^1 + 2 * 3

= 1 * 1 * 10^2 + ((1 + 2) * (1 + 3) - 1 * 1 - 2 * 3) * 10^1 + 2 * 3

= ~~1\*1~~ * 10^2 + (~~(1+2)\*(1+3)~~ - ~~1\*1~~ - ~~2\*3~~) * 10^1 + ~~2\*3~~

The original problem is divided into three part:1\*1, 2\*3, and (1+2)\*(1+3) three parts, with q = 3

T(n) <= 3T(n/2) + cn

T(n) <=O (n^log3) < O(n^2)
