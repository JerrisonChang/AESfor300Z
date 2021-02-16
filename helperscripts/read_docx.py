
import os
import glob
import docx
import PyPDF2
import re

def get_netID2content(path: str) -> dict:
    result = {}
    for i in get_docx_assignment_list(path):
        net_ID, content = get_id_and_content(i)
        result[net_ID] = content
    
    return result

def get_docx_assignment_list(path:str) -> list:
    result = glob.glob(f"{path}/*.docx")

    return result

def get_pdf_assignment_list(path:str) -> list:
    result = glob.glob(f"{path}/*.pdf")

    return result

def get_id_and_content(file_path) -> list:
    net_ID = get_netID(file_path)
    content = read_docx_content(file_path)

    return [net_ID, content]

def read_docx_content(file_path: str) -> str:
    head, ext = os.path.splitext(file_path)
    assert ext == '.docx'

    document = docx.Document(file_path)
    content_list = [p.text for p in document.paragraphs if p.text != '']
    content = ' '.join(content_list)
    return content

def read_pdf_content(file_path: str) -> str:
    head, ext = os.path.splitext(file_path)
    assert ext == '.pdf'

    pdfObject = open(file_path, 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfObject)
    print(pdfReader.getPage(0).extractText())


def get_netID(file_path: str) -> str:
    netID_pattern = r'\w{2}\d{6}'
    match_result = re.search(netID_pattern, file_path)
    if match_result == None:
        result = ''
    else:
        result = match_result.group()    
    return result


if __name__=="__main__":
    DIR = 'ICSI-300Z_Assignment1_Normative_Ethics'
    test_pdf = 'Assignment 1. Normative Ethics_ec529919_attempt_2020-09-15-06-45-50_EvonChoong_300Z_Assignment1.pdf'
    # first_file_path = get_docx_assignment_list(DIR)[0]
    # content = read_docx_content(first_file_path)
    # print(f'\n{get_netID(first_file_path)}')
    # print(len(''.join(content)))
    read_pdf_content(f"{DIR}/{test_pdf}")