from __future__ import annotations
from dataclasses import dataclass
from typing import List
import re
import os
import pickle

import pandas as pd

from .essaystructured import EssayStructured


@dataclass
class DocumentBin():
    hw_code: str
    semester_code: str
    essays: List[EssayStructured]
    
    def attach_scores(self, scores: pd.DataFrame):
        categories = ['content', 'research', 'communication', 'organization', 'bibliography', 'efforts', 'quality of writing']
        for essay in self.essays:
            grades = {j: scores.loc[essay.student_id, j] for j in categories}
            essay.attach_score(grades)
        

    def to_csv(self, path: str, encoding: str='utf-8'):
        array2d = [i.to_list() for i in self.essays]
        df = pd.DataFrame(array2d, columns=['file_name', 'netID', 'title', 'body', 'reference'])
        df.to_csv(path, encoding=encoding)
    
    def save_to_disk(self, path: str):
        *_, file_name = os.path.split(path)
        has_semester_code = re.search(r'(?:fa|sp|su)\d{2}', file_name)
        has_hw_code = re.search(r"hw\d", file_name)
        if not has_semester_code:
            raise Exception(f"file name does not have semester code ({file_name})")
        if not has_hw_code:
            raise Exception(f"file name does not have hw code ({file_name})")
        
        essays = self.essays
        with open(path, 'wb') as f:
            pickle.dump(essays, f)

    @staticmethod
    def load_from_saved(path: str) -> DocumentBin:
        *_, file_name = os.path.split(path)
        hw_code, semester_code, *_ = file_name.split('_')
        with open(path, 'rb') as f:
            return DocumentBin(semester_code, hw_code, pickle.load(f))