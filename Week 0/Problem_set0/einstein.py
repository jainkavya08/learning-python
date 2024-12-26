# Define the speed of light (in meters per second) squared
c = int(300000000 * 300000000)

# Prompt the user to input the mass (m) in kilograms
m = int(input("m :"))

# Calculate energy (E) using Einstein's equation E = mc^2
E = int(m * c)

# Print the calculated energy
print(f"E : {E}")
