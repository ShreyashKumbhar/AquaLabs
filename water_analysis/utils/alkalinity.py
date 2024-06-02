import matplotlib.pyplot as plt

# Function to find alkalinity based on P and M endpoints
def calculate_alkalinity(V1, V2):
    # Standard reference table
    P = 100 * V1
    M = 100 * V2
    if V1 == 0:
        HCO3 = M
        alkalinity = HCO3 * (50/81)  # Converting alkalinity in CaCO3 equivalent
        return round(alkalinity, 2), round(HCO3, 2), 0, 0
    if V1 == V2:
        OH = P
        alkalinity = OH * (50/37)
        return round(alkalinity, 2), 0, 0, round(OH, 2)
    if V1 == 0.5 * V2:
        CO3 = 2 * P
        return round(alkalinity, 2), 0, round(CO3, 2), 0
    if V1 > 0.5 * V2:
        OH = 2 * P - M
        CO3 = 2 * (M - P)
        alkalinity = CO3 + (OH * (50/37))
        return round(alkalinity, 2), 0, round(CO3, 2), round(OH, 2)
    if V1 < 0.5 * V2:
        CO3 = 2 * P
        HCO3 = M - 2 * P
        alkalinity = CO3 + (HCO3 * (50/81))
        return round(alkalinity, 2), round(HCO3, 2), round(CO3, 2), 0


def main():
    # Experiment data
    V1 = float(input("Enter the volume of HCl added until phenolphthalein endpoint (in mL): "))
    V2 = float(input("Enter the additional volume of HCl added until methyl orange endpoint (in mL): "))

    # Calculate alkalinity
    alkalinity_value, HCO3, CO3, OH = calculate_alkalinity(V1, V2)

if __name__ == "__main__":
    main()

