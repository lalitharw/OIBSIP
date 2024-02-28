def calculate_BMI(height: float, weight: float) -> str:
    BMI = weight / (height ** 2)

    # BMI logic to determine category
    if BMI < 18.5:
        result = "Underweight"
    elif BMI >= 18.5 and BMI <= 24.9:
        result = "Healthy"
    elif BMI >= 25 and BMI <= 29.9:
        result = "Overweight"
    elif BMI >= 30 and BMI <= 34.9:
        result = "Obese"
    else:
        result = "Extremely obese"

    return result

try:
    height = float(input("Enter Height (in meters): "))
    weight = float(input("Enter Weight (in kilograms): "))

    print(f"As per your height: {height} and weight: {weight}, you belong to {calculate_BMI(height, weight)} Category")
except ValueError:
    print("Please enter numerical value")
