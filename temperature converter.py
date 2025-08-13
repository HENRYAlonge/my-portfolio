conversion = input("Enter what temperature scale you'd like to convert to (c,C or f,F): ")
temperature = float(input("Enter the temperature: "))

# Check if the temperature is within range first
if not (-100 <= temperature <= 100):
    print("Invalid temperature")
else:
    if conversion == "c" or conversion == "C":
        result = (temperature - 32) * 5 / 9
        print(f"{temperature}°F is {result:.2f}°C")

    elif conversion == "f" or conversion == "F":
        result = (9 / 5 * temperature) + 32
        print(f"{temperature}°C is {result:.2f}°F")

    else:
        print("Invalid conversion scale. Use 'c','C' or 'f','F'.")
