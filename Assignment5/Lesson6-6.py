import math

def unit_price(diameter_cm, price_eur):
    radius_m = (diameter_cm / 100) / 2
    area_m2 = math.pi * radius_m ** 2
    return price_eur / area_m2


print("Enter details for Pizza 1:")
diameter1 = float(input("Diameter (cm): "))
price1 = float(input("Price (€): "))

print("\nEnter details for Pizza 2:")
diameter2 = float(input("Diameter (cm): "))
price2 = float(input("Price (€): "))


unit1 = unit_price(diameter1, price1)
unit2 = unit_price(diameter2, price2)

# Display results
print(f"\nPizza 1 unit price: €{unit1:.2f} per m²")
print(f"Pizza 2 unit price: €{unit2:.2f} per m²")

# Compare and decide
if unit1 < unit2:
    print("Pizza 1 offers better value for money.")
elif unit2 < unit1:
    print("Pizza 2 offers better value for money.")
else:
    print("Both pizzas offer the same value for money.")