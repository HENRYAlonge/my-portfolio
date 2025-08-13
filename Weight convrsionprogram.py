#Weight conversion program
weight = float(input("Enter your weight:"))
unit = input("Enter a unit you'd like to convert to: (kg,lb):")
solution = None
if unit == "kg":
    solution = weight * 2.205
    unit = "lbs."
elif unit == "lb":
    solution = weight / 2.205
    unit = "kgs."


if solution is not None:
   print(f"Your weight is:{round(solution,2)} {unit}")
else:
   print(f"{unit} was not valid")