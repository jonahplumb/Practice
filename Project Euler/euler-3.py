#!/usr/bin/env python3

import math

num = 600851475143
i = 2
while i * i < num:
    while num % i == 0:
        num /= i
    i += 1
    
print(int(num))

