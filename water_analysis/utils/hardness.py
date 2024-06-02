# Function to calculate the molarity of EDTA
def calculate_edta_molarity(znso4_volume, znso4_concentration, edta_volume):
    moles_znso4 = znso4_volume * znso4_concentration
    molarity_edta = moles_znso4 / edta_volume
    return round(molarity_edta,2)

# Function to calculate the hardness of water
def calculate_hardness(edta_molarity, edta_volume_B):
    Hardness = (1000 * edta_molarity * edta_volume_B * 100) / 10
    return round(Hardness,2)

# Main function
def main():
    # Constants
    znso4_concentration = 0.01  # Molarity of ZnSO4 solution in mol/L

    # Experiment data
    znso4_volume = float(input("Enter the volume of ZnSO4 solution used (in mL): "))
    edta_volume = float(input("Enter the burette reading of EDTA solution used (in mL): "))

    # Calculate the molarity of EDTA
    edta_molarity = calculate_edta_molarity(znso4_volume / 1000, znso4_concentration, edta_volume / 1000)
    print("Molarity of EDTA:", edta_molarity, "mol/L")

    edta_volume_B = float(input("Enter the volume of EDTA used to titrate water sample: "))
    # Calculate the hardness of water
    water_hardness = calculate_hardness(edta_molarity, edta_volume_B)
    print("Hardness of water:", water_hardness, "mg/L")

if __name__ == "__main__":
    main()
