import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def control_chart(file_path, column_name):

    data = pd.read_csv(file_path)

    values = data[column_name]

    mean = np.mean(values)
    std_dev = np.std(values)

    upper_control_limit = mean + 3 * std_dev
    lower_control_limit = mean - 3 * std_dev

    plt.figure(figsize=(10, 6))
    plt.plot(values, marker='o', linestyle='-', color='b', label=column_name)
    plt.axhline(mean, color='green', linestyle='--', label='Mean')
    plt.axhline(upper_control_limit, color='red', linestyle='--', label='Upper Control Limit (UCL)')
    plt.axhline(lower_control_limit, color='red', linestyle='--', label='Lower Control Limit (LCL)')

    plt.title(f'Control Chart for {column_name}')
    plt.xlabel('Sample Number')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)

    plt.show()
    print(f"Mean: {mean:.5f}")
    print(f"Standard Deviation: {std_dev:.5f}")
    print(f"Upper Control Limit (UCL): {upper_control_limit:.5f}")
    print(f"Lower Control Limit (LCL): {lower_control_limit:.5f}")

file_path = 'D:\\Download .Hack\\Poisson Distribution -Dataset.csv'
column_name = 'Accidents - 2017' 

control_chart(file_path, column_name)
