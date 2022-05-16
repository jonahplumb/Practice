#! /usr/bin/env python3 

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

num = 1000

five = [i for i in range(num) if(i % 5 ==0)]
three = [i for i in range(num) if(i % 3 ==0)]
fifteen = [i for i in range(num) if(i % 15 ==0)]
print(sum(five + three) -  sum(fifteen))
