def calculate_cut_off(maths, physics, chemistry):
    return (maths + ((physics+chemistry) / 2))

def main():
    print("Engineering Cut-off Calculator")
    print("------------------------------")
    try:
        maths = float(input("Enter Maths mark (out of 100): "))
        physics = float(input("Enter Physics mark (out of 100): "))
        chemistry = float(input("Enter Chemistry mark (out of 100): "))

        if 0 <= maths <= 100 and 0 <= physics <= 100 and 0 <= chemistry <= 100:
            cut_off = calculate_cut_off(maths, physics, chemistry)
            print("Your engineering cut-off mark is:", cut_off)
        else:
            print("Marks should be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
