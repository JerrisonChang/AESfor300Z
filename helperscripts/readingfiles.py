import pandas as pd

import os

def read_spreadsheet(input_path: str, fill_na_as= "", *args, **kwarg) -> pd.DataFrame:
    _, ext = os.path.splitext(input_path)

    assert ext in ['.csv', '.xlsx']

    if ext == ".csv":
        df = pd.read_csv(input_path, encoding='utf-8').fillna(fill_na_as)
    else:
        sheet_name = kwarg.get("sheet_name", 0)
        df = pd.read_excel(input_path, sheet_name, engine='openpyxl').fillna(fill_na_as)

    return df
    