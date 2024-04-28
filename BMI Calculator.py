weight_in_kg = float(input("Enter your weight in kilograms: "))
height_in_m = float(input("Enter your height in meters: "))

bmi = weight_in_kg / (height_in_m ** 2)

bmi_categories = {
    "Underweight": (0, 18.5),
    "Normal": (18.5, 25),
    "Overweight": (25, 30),
    "Obese": (30, float("inf"))
}

for category, (lower_bound, upper_bound) in bmi_categories.items():
    if lower_bound <= bmi < upper_bound:
        bmi_category = category
        break
else:
    bmi_category = "Invalid BMI"

print(f"Your BMI is: {bmi:.2f}")
print(f"Your BMI category is: {bmi_category}")