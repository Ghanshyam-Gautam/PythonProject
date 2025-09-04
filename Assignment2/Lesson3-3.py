
gender = input("Choose Gender: male, female ")
value = int(input("Enter hemoglobin value (g/l): "))
if gender == "male":
    if value < 134 :
        print("Hemoglobin level is low")
    elif 134 <= value <= 167 :
        print("Hemoglobin level is normal")
    else:
        print("Hemoglobin level is high")
elif gender == "female":
    if value < 117:
        print("Hemoglobin level is low")
    elif 117<= value <= 155:
        print("Hemoglobin level is normal")
    else:
        print("Hemoglobin level is high")
else:
    print("wrong gender or value")
