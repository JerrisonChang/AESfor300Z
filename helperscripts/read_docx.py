
import glob

import os

import docx
import PyPDF2
import re

class DocxReader():
    def __init__(self, path_to_essay_folder:str):
        self.essay_folder = path_to_essay_folder

    def get_netID_to_structured_content(self) -> dict:
        result = {}
        for i in self.get_dox_assignment_list():
            netID = self.get_netID_from_file_path(i)
            structured_essay = self.read_docx_and_structure(i)

            result[netID] = structured_essay

        return result

    def get_netID_from_file_path(self, file_path:str) -> str:
        netID_pattern = r'\w{2}\d{6}'
        match_result = re.search(netID_pattern, file_path)
        if match_result == None:
            result = ''
        else:
            result = match_result.group()    
        return result
    
    def read_docx_and_structure(self, file_path: str) -> tuple:
        """
        This method will disect an essay as 'title page', 'body', and 'bibliography' and return them
        """
        head, ext = os.path.splitext(file_path)
        assert ext == '.docx'

        document = docx.Document(file_path)
        paragraphs = [p.text.strip() for p in document.paragraphs if p.text.strip() != '']
        
        content_start_index: int
        reference_start_index: int

        found_content_start = False
        found_reference_start = False
        if len(paragraphs) == 0:
            return ('','','')

        for i, paragraph in enumerate(paragraphs):
            word_count = len(paragraph.split(' '))
            
            if (not found_content_start):
                if word_count >= 45 or paragraph.lower() in ['abstract']: 
                    found_content_start = True
                    content_start_index = i
            elif not found_reference_start:
                if word_count<=3:
                    # if (not found_reference_start) and paragraph.lower() in ['bibliography', 'references', 'reference','sources']:
                    is_page_number = re.match(r'.*\d\s?$', paragraph) != None # page number e.g. "page 1" or "Bobby 1"
                    is_other_title = paragraph.lower() in ['introduction', 'conclusion', 'abstract']
                    if is_page_number or is_other_title:
                        continue
                
                    found_reference_start = True
                    reference_start_index = i

        if found_content_start:
            title = '\n'.join(paragraphs[:content_start_index])
            
            if found_reference_start:
                body = '\n'.join(paragraphs[content_start_index: reference_start_index])
                references = '\n'.join(paragraphs[reference_start_index:])
            else:
                body = '\n'.join(paragraphs[content_start_index:])
                references = ''
        else:
            title = ''
            body = '\n'.join(paragraphs)
            references = ''
            
        return (title, body, references)

    def get_dox_assignment_list(self) -> list:
        result = glob.glob(f"{self.essay_folder}/*.docx")
        result = list(filter(lambda x: '~$' not in x,result))
        return result


def get_netID2content(path: str) -> dict:
    result = {}
    for i in get_docx_assignment_list(path):
        net_ID, content = get_id_and_content(i)
        result[net_ID] = content
    
    return result

def get_netID2structuredContent(path: str) -> dict:
    result = {}
    for i in get_docx_assignment_list(path):
        netID = get_netID(i)
        structured_essay = read_docx_and_structure(i)

        result[netID] = structured_essay

    return result

def get_docx_assignment_list(path:str) -> list:
    result = glob.glob(f"{path}/*.docx")
    result = list(filter(lambda x: '~$' not in x,result))
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

def read_docx_and_structure(file_path: str) -> tuple:
    """
    This method will disect an essay as 'title page', 'body', and 'bibliography' and return them
    """
    head, ext = os.path.splitext(file_path)
    assert ext == '.docx'

    document = docx.Document(file_path)
    paragraphs = [p.text.strip() for p in document.paragraphs if p.text.strip() != '']
    
    content_start_index: int
    reference_start_index: int

    found_content_start = False
    found_reference_start = False
    if len(paragraphs) == 0:
        return ('','','')

    for i, paragraph in enumerate(paragraphs):
        word_count = len(paragraph.split(' '))
        
        if (not found_content_start):
            if word_count >= 45 or paragraph.lower() in ['abstract']: 
                found_content_start = True
                content_start_index = i
        elif not found_reference_start:
            if word_count<=3:
                # if (not found_reference_start) and paragraph.lower() in ['bibliography', 'references', 'reference','sources']:
                is_page_number = re.match(r'.*\d\s?$', paragraph) != None # page number e.g. "page 1" or "Bobby 1"
                is_other_title = paragraph.lower() in ['introduction', 'conclusion', 'abstract']
                if is_page_number or is_other_title:
                    continue
            
                found_reference_start = True
                reference_start_index = i

    if found_content_start:
        title = '\n'.join(paragraphs[:content_start_index])
        
        if found_reference_start:
            body = '\n'.join(paragraphs[content_start_index: reference_start_index])
            references = '\n'.join(paragraphs[reference_start_index:])
        else:
            body = '\n'.join(paragraphs[content_start_index:])
            references = ''
    else:
        title = ''
        body = '\n'.join(paragraphs)
        references = ''
        
    return (title, body, references)

def print_docx_content(file_path: str) -> str:
    head, ext = os.path.splitext(file_path)
    assert ext == '.docx'
    assert os.path.isfile(file_path)

    document = docx.Document(file_path)
    for paragraph in document.paragraphs:
        text = paragraph.text.strip()
        if text == '': continue
        print(len(text.split(' ')) ,f"--{text}--")

    print('print ended', len(document.paragraphs))
        
### This route is too much work(need to learn to navigate in xml trees), pending for now
# def read_docx_as_xml(file_path: str):
#     head, ext = os.path.splitext(file_path)
#     assert ext == '.docx'

#     document = zipfile.ZipFile(file_path)
#     original_xml = xml.dom.minidom.parseString(document.read('word/document.xml')).toprettyxml(indent='    ')
#     print(original_xml)

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

def test_zipFile_approach():
    file_path = 'testing.docx'
    file_path_2 = 'essays/hw2_fa20/Assignment 2. Privacy_as465988_attempt_2020-10-05-19-56-31_Privacy.docx'
    
    print_docx_content(file_path_2)
    # read_docx_as_xml(file_path_2)
    # for x, y in zip(['title','body','references'],read_docx_and_structure(file_path_2)):
    #     print(x)
    #     print(y)
    # print_docx_content(file_path)


if __name__=="__main__":
    DIR = 'ICSI-300Z_Assignment1_Normative_Ethics'
    test_pdf = 'Assignment 1. Normative Ethics_ec529919_attempt_2020-09-15-06-45-50_EvonChoong_300Z_Assignment1.pdf'
    test_zipFile_approach()
    # first_file_path = get_docx_assignment_list(DIR)[0]
    # content = read_docx_content(first_file_path)
    # print(f'\n{get_netID(first_file_path)}')
    # print(len(''.join(content)))
    # read_pdf_content(f"{DIR}/{test_pdf}")
    # print(read_docx_content('./testing.docx').encode('unicode_escape'))
