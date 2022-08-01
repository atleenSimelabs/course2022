#exponential calculator

base=input("Base: ")
expo=input("Expo: ")
def exponent_calc(base, expo):
    if expo == 0:
        return 1
    else:
        return int(base)**int(expo)
        # return pow(base, expo)

# print(exponent_calc(5, 3))
print(exponent_calc(base=base, expo=expo))

