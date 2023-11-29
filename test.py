import pandas as pd
import numpy as np
df = pd.read_excel(r'FIRST\Second\Book1.xlsx')
print(np.max(df.loc[:,'Maths']))
