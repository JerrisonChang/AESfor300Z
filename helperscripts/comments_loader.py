import enum
from dataclasses import dataclass

import pandas as pd

# path to the comment bank 
PATH = './documents/AES comments bank.xlsx'

# comment_df = pd.read_excel(PATH, engine='openpyxl', index_col=0)

def load_comment_bank() -> pd.DataFrame:
    return pd.read_excel(PATH, engine='openpyxl', index_col=0)