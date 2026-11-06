import math

# Traditional values that can cause rounding errors
x = 1.23456789012345
y = 1.23456789012345
z = -1.5241578753238836

# Standard math: (x * y) is rounded first, then z is added
standard_result = (x * y) + z

# Fused Multiply-Add: (x * y) + z is computed with a single rounding step at the end
fma_result = math.fma(x, y, z)

print("Standard:", standard_result)
print("FMA:     ", fma_result)
