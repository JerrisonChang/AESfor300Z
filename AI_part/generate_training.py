import os
from glob import glob
from enum import Enum
from dataclasses import dataclass
from typing import List

import pandas  as pd

@dataclass
class HW:
    code: str
    topic: str

class Catagories(Enum):
    CONTENT = "content"
    RESEARCH = "research"
    ORGANIZATION = "oganization"
    COMMUNICATION = "communication"
    EFFORTS = "efforts"
    QUALITY = "quality of writing"
    BIBLIOGRAPHY = "bibliography"

TOPIC_INDEPENTENT = {
    Catagories.CONTENT: True,
    Catagories.RESEARCH: True,
    Catagories.ORGANIZATION: False,
    Catagories.COMMUNICATION: True,
    Catagories.EFFORTS: False,
    Catagories.BIBLIOGRAPHY: False
}

class ExtensionError(Exception):
    pass

# HIST_SEMESTERS = ['fa20', 'fa21', 'sp22', 'summer21']
FOLDER = os.path.join('./gradebook/final')
HWS = [
    HW('normative_ethics', 'Normative Ethics'),
    HW('privacy', 'Privacy'),
    HW('epfoscl', 'Ethics, privacy, freedom of speech, copyrights, and laws'),
    HW('hacktivism', 'Hacktivism'),
    HW('facial_recognition', "Facial Recognition") # usually extra assignment
]

def read_spread_sheet(path: str) -> pd.DataFrame:
    _, extension = os.path.splitext(path)
    
    if extension == '.csv':
        return pd.read_csv(path, encoding='utf-8')
    elif extension == '.xlsx':
        return pd.read_excel(path, engine="openpyxl")
    else:
        raise ExtensionError(f"Unsupported extension type; expected: .csv or .xlsx, got {extension}")

def get_df(catagory: Catagories, hw_code: str) -> pd.DataFrame:
    if TOPIC_INDEPENTENT[catagory]:
        files = glob(os.path.join(FOLDER, f"{hw_code}_*"))
    else:
        files = glob(FOLDER)

    frames = [read_spread_sheet(i) for i in files]
    result = pd.concat(frames)[[catagory.value, 'title page', 'essay body', 'essay refs', 'word count']]
    
    return result

if __name__=="__main__":
    result = get_df(Catagories.CONTENT, 'normative_ethics')

    print(result[:30])

    