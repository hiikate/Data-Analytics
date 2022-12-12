import matplotlib.pyplot as plt
import numpy as np

# Set the mean value, standard deviation, sample size, and number of bars
mean = 24
std = 10
sample_size = 750000
num_bars = 100

# Generate the sample data using the specified mean and standard deviation
sample_data = np.random.normal(mean, std, sample_size)

# Plot the histogram using the specified number of bars
plt.hist(sample_data, num_bars)

# Show the plot
plt.show()
