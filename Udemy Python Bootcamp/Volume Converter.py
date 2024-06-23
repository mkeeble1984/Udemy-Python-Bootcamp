def volume_converter(fOunce):
    answer = fOunce * 29.57353
    return answer


fOunce = int(input("Please enter the volume in fluid ounces: "))

print(f"This converts to {volume_converter(fOunce)} milliliters.")
