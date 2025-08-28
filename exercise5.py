talents=float(input("Enter talents "))
pounds=float(input("Enter pounds "))
lots=float(input("Enter lots "))

Pounds_in_Talents =20
Lots_in_Pounds= 32
Grams_in_Lots = 13.3
Grams_in_Kilogram = 1000

total_lots = ((talents * Pounds_in_Talents * Lots_in_Pounds) +
              (pounds * Lots_in_Pounds) + lots)

Total_Grams = total_lots * Grams_in_Lots

kilograms = float(Total_Grams // 1000)
grams = Total_Grams % 1000


print(f"The weight in modern units is :")
print(f"{kilograms} kilograms and {grams:.2f} grams")
