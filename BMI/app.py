def calcalute_BMI(height:float,weight:float):
        BMI = weight/(height**2)
        result = ""
       #  bmi logic
        if(BMI < 18.5):
              result = "UnderWeight"  
        elif(BMI >= 18.5 and BMI <=24.9):
               result = "healthy"
        elif(BMI >=30 and BMI <= 29.9): 
               result = "overWeight"
        elif(BMI >=30 and BMI <= 34.9): 
               result = "obese"
        else:
               result = "extremely obese"
        
        return result

try:
    height = float(input("Enter Height (in meters): "))
    weight = float(input("Enter Weight (in kilograms): "))

    print(f"As per your height: {height} and weight: {weight}, you belong to {calcalute_BMI(height,weight)} Category")
except ValueError:
       print("Please enter numerical value")
