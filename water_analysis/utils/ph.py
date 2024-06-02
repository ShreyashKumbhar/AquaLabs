def get_ph(ph):
    ph = float(input("Enter the pH of your water"))
    return ph

def main():
    ph_value = get_ph()
    print(ph_value)

if __name__ == "__main__":
    main()