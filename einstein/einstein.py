#ask for mass
def main():
    mass = int(input("m (kg): "))
    mass_to_energy(mass)

#convert mass to energy
def mass_to_energy(mass):
    energy = mass * 300000000 ** 2
    print(f"E (J): {energy}")

main()