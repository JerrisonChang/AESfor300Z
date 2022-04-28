import os
from enum import Enum
from dataclasses import dataclass
# from typing import List

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


HIST_SEMESTERS = ['fa20', 'fa21', 'sp22', 'summer21']
FOLDER = os.path.join('./gradebook/final')
HWS = [
    HW('normative_ethics', 'Normative Ethics'),
    HW('privacy', 'Privacy'),
    HW('epfoscl', 'Ethics, privacy, freedom of speech, copyrights, and laws'),
    HW('hacktivism', 'Hacktivism'),
    HW('facial_recognition', "Facial Recognition")
]

def get_df(catagory: Catagories, hw_code: str) -> pd.DataFrame:
    if TOPIC_INDEPENTENT[catagory]:
        print("just this")
        file_names = [f"{hw_code}_{i}" for i in HIST_SEMESTERS] # file names starting with ...
        df = pd.DataFrame()
    else:
        print("grab all")


if __name__=="__main__":
    get_df(Catagories.RESEARCH, 'normative_ethics')
    