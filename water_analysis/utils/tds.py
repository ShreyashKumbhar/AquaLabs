def calculate_tds(weight_dish_filtrate, weight_dish, volume_sample):
    # TDS formula: [(A - B) * 1000] / mL sample
    # A = weight of the evaporating dish + filtrate
    # B = weight of the evaporating dish
    # volume_sample = volume of the sample in mL
    tds = ((weight_dish_filtrate - weight_dish) * 1000) / volume_sample
    return round(tds,2)

def main():
    # Get the input from the user
    weight_dish_filtrate = float(input("Enter the weight of the evaporating dish + filtrate (in grams): "))
    weight_dish = float(input("Enter the weight of the evaporating dish (in grams): "))
    volume_sample = float(input("Enter the volume of the sample (in mL): "))

    # Calculate the TDS
    tds_measurement = calculate_tds(weight_dish_filtrate, weight_dish, volume_sample)

    # Print the TDS value
    print(f"The TDS measurement is: {tds_measurement:.2f} mg/L")

if __name__ == "__main__":
    main()