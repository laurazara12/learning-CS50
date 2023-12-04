def calculate_energy(mass_kg):
    speed_of_light = 300000000  # meters per second
    energy_joules = mass_kg * speed_of_light ** 2
    return energy_joules

def main():
    mass_input = input("Enter mass in kilograms: ")
    mass = int(mass_input)
    energy = calculate_energy(mass)
    print(f"The equivalent energy is: {energy} Joules")

if __name__ == "__main__":
    main()
