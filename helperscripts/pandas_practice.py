import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([[1,2,3],[2,3,4],[3,4,5]]), columns=['id', 'a', 'other'])
print(df)

df_id = df.set_index('id')

df_id.to_excel('./practice.xlsx')
