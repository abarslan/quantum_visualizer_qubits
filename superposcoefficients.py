import numpy as np
import matplotlib.pyplot as plt

def generate_normalized_coefficients():
    # Generate random complex coefficients, 1j * np.random.rand() generates a 
    # random complex number where the real part is zero and the imaginary part 
    # is a random number between 0 and 1 example 0.3j.
    coefficients = [np.random.rand() + 1j * np.random.rand() for _ in range(16)]

    # Normalize the coefficients, calculate the normalization factor as the 
    # square root of the sum of the squares of the absolute values of the coefficients
    # (a*a)+(b*b)+(g*g)+(d*d)=1=coeffs
    # norm_factor = sqrt(coeffs)
    norm_factor = np.sqrt(sum(np.abs(coeff)**2 for coeff in coefficients))
    coefficients = [coeff / norm_factor for coeff in coefficients]

    return coefficients

# Generate a random quantum state
results = generate_normalized_coefficients()

# Define the mapping between qubit states and binary numbers
binary_mapping = {
    '|0000⟩': '0000',
    '|0001⟩': '0001',
    '|0010⟩': '0010',
    '|0011⟩': '0011',
    '|0100⟩': '0100',
    '|0101⟩': '0101',
    '|0110⟩': '0110',
    '|0111⟩': '0111',
    '|1000⟩': '1000',
    '|1001⟩': '1001',
    '|1010⟩': '1010',
    '|1011⟩': '1011',
    '|1100⟩': '1100',
    '|1101⟩': '1101',
    '|1110⟩': '1110',
    '|1111⟩': '1111'
}

# Make a list of binarymapping as states for choosing the random state basen on distributions
states = list(binary_mapping.keys())
state = np.random.choice(states, p=np.abs(results)**2)

# Access the binary representation based on the chosen state
probability = np.abs(results[states.index(state)])**2
binary_representation = binary_mapping[state]
print("4 binary bit:", binary_representation)
print("Probability:", probability)

# Plot the probability distribution
probabilities = np.abs(results)**2

plt.bar(states, probabilities)
plt.xlabel('Qubit States')
plt.ylabel('Probability')
plt.title('Probability Distribution of Qubit States')
plt.xticks(rotation=90)
plt.show()
