import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Sample data
data = np.random.normal(loc=0, scale=1, size=1000)

# Estimate the parameters (mean, std dev)
mu, std = np.mean(data), np.std(data)

# Generate a range of values for the PDF
x = np.linspace(min(data), max(data), 1000)

# Calculate the PDF
pdf = norm.pdf(x, mu, std)

# Plot the histogram of the data and the PDF
plt.hist(data, bins=30, density=True, alpha=0.6, color='b')
plt.plot(x, pdf, 'r', label="PDF")
plt.title('PDF of Sample Data')
plt.legend()
plt.show()
