#!/usr/bin/env python  

from Crypto.Util.number import inverse
from codecs import decode

n = 1216177716507739302616478655910148392804849

e = 65537

p = 1033247481589406269253

q = 1177043968824330681533

c1 = 257733734393970582988408159581244878149116 # ciphertext line 1
c2 = 843105902970788695411197846605744081831851 # ciphertext line 2

part = (p - 1) * (q -1)

d = inverse(e,part)

m1 = pow(c1,d,n)
m2 = pow(c2,d,n)

print(decode(hex(m1)[2:],'hex'))
print(decode(hex(m2)[2:],'hex'))

