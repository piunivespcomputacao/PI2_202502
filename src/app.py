import pandas as pd
import numpy as np


data = pd.read_csv("data.csv", sep = ",")
# Specify the columns you want to keep in a list
selected_columns = ['id','rpm','motor_power','outlet_pressure_bar','air_flow','noise_db','outlet_temp','gaccx','gaccy','gaccz','haccx','haccy','haccz','exvalve','acmotor'] # Replace with your desired columns
data = data[selected_columns]

#print(f"min: {np.min(data):.2f}")
#print(f"max: {np.max(data):.2f}")
#print(f"média: {np.mean(data):.2f}")
#print(f"mediana: {np.median(data):.2f}")
#print(f"mediana 30%: {np.median(data)*0.83:.2f}")
#print(f"mediana 70%: {np.median(data)*1.16:.2f}")
print(data.to_string())


