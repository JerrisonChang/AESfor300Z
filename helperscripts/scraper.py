'''
This script is supposed to take in an essay folder and output a csv with username, hw_id, and extracted feature
'''

import pandas as pd

import glob
import re
from typing import List, Dict

from helperscripts.read_docx import DocxReader, EssayStructured

def get_netID(file_path:str) -> str:
    netID_pattern = r'\w{2}\d{6}'
    match_result = re.search(netID_pattern, file_path)
    
    netID = "" if match_result == None else match_result.group()
    return netID

def get_docx_list(essay_folder_path: str) -> List[str]:
    result = glob.glob(f"{essay_folder_path}/*.docx")
    result = list(filter(lambda x: '~$' not in x,result))
    return result


def get_ID2EssayStructured(essay_folder: str) -> Dict[str, EssayStructured]:
    docxReader = DocxReader(essay_folder)
    file_list = get_docx_list(essay_folder)
    result = {get_netID(i): docxReader.parse_document_into_sections(docxReader.read_document(i)) for i in file_list}

    return result

def get_df(id2EssayStructured: Dict[str, EssayStructured]) -> pd.DataFrame:
    nested_list = [[key, essay.get_title(), essay.get_body(), essay.get_reference(), essay.get_word_count()] for key, essay in id2EssayStructured.items()]
    df = pd.DataFrame(nested_list, columns=["Username", "Title", "Body", "Reference", "Word Count"])

    return df
    
    