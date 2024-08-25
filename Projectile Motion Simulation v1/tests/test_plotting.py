import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data/times_heights.csv'

df = pd.read_csv(file_path)

plt.plot(df['Time'], df['Height'])
plt.xlabel('Time (seconds)')
plt.ylabel('Height (meters)')
plt.title('Time vs. Height')
plt.grid(True)

output_path = "plots/Time_vs_Height.png"
plt.savefig(output_path)

plt.show()