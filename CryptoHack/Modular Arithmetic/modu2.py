# 3^17 mod 17: Applying Fermat's little theorem, a = 3 and p = 17 is prime number, so 3^17 ≡ 3 (mod 17)
# 7^16 mod 17: Applying Fermat's little theorem, a = 7 and p = 17, a is not divisible by p and (a, p) is coprime, so 3^(17-1) = 3^16 ≡ 1 (mod 17)
# do the same with the challenge below

a = 273246787654
b = 65536
print((a**b)%(b+1))