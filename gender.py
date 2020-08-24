import numpy as np
import pandas as pd

data = pd.read_csv("data/gender_split.csv")
# columns:
# - race_name: race name
# - Nw: number of female finishers
# - Nm: number of male finishers

# rows:
# - (race_name, Nw, Nm)


df = pd.DataFrame(data, columns = ['race_name', 'Nw','Nm']) 
df['Nw/Nm'] = df['Nw']/df['Nm'] # add dataframe column

print("avg(Nw/Nm):", df['Nw/Nm'].mean(axis = 0)) # avg ratio of female finishers to male finishers (over all races, all years)

# ----------------- ideas -----------------
#print("max(Nw/Nm) s.t. N > 20:",  df[df['Nw']+df['Nm']>40]) # list races with >20 overall finishers
#print("Nw > 5:", df[df['Nw']>5]) # list races with >5 women finishers
