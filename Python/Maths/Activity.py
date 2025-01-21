import pandas as pd
from scipy.stats import poisson

file_path = 'D:\\Download .Hack\\Poisson Distribution -Dataset.csv'  
data = pd.read_csv(file_path)

st=input("Enter the State name : ") 

state_data = data[data['State/UT']== st].iloc[0] 

mean_fatal_accidents = (state_data['Accidents - 2016'] + state_data['Accidents - 2017']) / 2

print("=== Poisson Distribution Calculator ===\n")
print(f"State:{st}\n")
print(f"Average Number of Fatal Accidents (λ) for 2016 and 2017: {mean_fatal_accidents:.2f}\n")

k_values = [
    int(mean_fatal_accidents),                
    int(mean_fatal_accidents) - 1,            
    int(mean_fatal_accidents) + 1,            
    int(mean_fatal_accidents // 2),           
    int(mean_fatal_accidents * 2)             
]
k_values = [k for k in k_values if k >= 0]

print("=== Probability Results (Poisson Distribution) ===\n")
for k in k_values:
    prob = poisson.pmf(k, mean_fatal_accidents)
    print(f"P(X = {k}) = {prob:.6f} or {prob*100:.4f}%")

cumulative_prob = poisson.cdf(int(mean_fatal_accidents), mean_fatal_accidents)

print(f"\nCumulative Probability P(X ≤ {int(mean_fatal_accidents)}) = {cumulative_prob:.6f} or {cumulative_prob*100:.4f}%")
