# Chinese Remainder Theorem

# Systematic search
# Starting with the congruence with the largest modulus, use that for x ≡ a mod p we can write x = a + k*p for arbitrary integer k.
for k in range(0, 936):
    x = 5 + 17*k
    if x % 5 == 2 and x % 11 == 3:
        print(x % 935)
        break
