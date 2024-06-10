# Define the function to convert depth in cm to NTU
def depth_to_ntu(depth_cm):
    # Given equation: Depth in cm = 244.13 * (Turbidity in NTU)^-0.662
    # Rearrange the equation to solve for NTU:
    # NTU = (244.13 / Depth in cm)^(1 / 0.662)
    ntu = (244.13 / depth_cm) ** (1 / 0.662)
    return ntu

def main():
    # Getting the depth reading from the user
    depth_cm = float(input("Enter the depth reading in centimeters: "))

    # Converting the depth reading to NTU
    ntu_measurement = round(depth_to_ntu(depth_cm))

    # Printing the NTU measurement
    print(f"The NTU measurement is: {ntu_measurement:.2f} NTU")

if __name__ == "__main__":
    main()