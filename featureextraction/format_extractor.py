from docx import Document
from docx.text.paragraph import Paragraph

from collections import Counter
from typing import List, Union
import os

def get_majority_font_name(paragraph: Paragraph):
    """Get the most common font in each paragraph"""
    
    fonts_in_paragraphs = [i.font.name for i in paragraph.runs]
    if len(fonts_in_paragraphs)== 0:
        return paragraph.style.font.name
    
    c = Counter(fonts_in_paragraphs)
    return c.most_common()[0][0]

def get_majority_font_size(paragraph: Paragraph) -> Union[None, str]:
    """Get the most common font size in each paragraph"""
    fonts_in_paragraphs = [i.font.size.pt if i.font.size else 0 for i in paragraph.runs ]
    if len(fonts_in_paragraphs)== 0:
        return None
    
    c = Counter(fonts_in_paragraphs)
    return c.most_common()[0][0]

def get_word_count(paragraph: Paragraph):
    """Get word count for each paragraph"""
    word_count = len(paragraph.text.split(" "))
    return word_count

if __name__ == "__main__": 
    document = Document("./example_docx/test.docx")
    paragraphs = document.paragraphs
    print("LineSpace\tJustification\tIndentation\tFont\tFontSize\tWordCount\tHasTitlePage")

    for i in paragraphs:
        pf = i.paragraph_format
        first_character_is_tab = i.text[0] == '\t' if len(i.text) > 0 else False
        print(f"{pf.line_spacing if pf.line_spacing else 'None': <16}", end="")
        #print(pf.alignment , end="\t\t")
        print(f"{str(pf.alignment) if pf.alignment else 'None': <16}", end="")

        print(f"{pf.first_line_indent.inches if pf.first_line_indent else str(first_character_is_tab): <16}",end="" )

        print(f"{str(get_majority_font_name(i)): <16}",end="")
        print(f"{str(get_majority_font_size(i)): <16}", end="")
        print(f"{str(get_word_count(i)): <16}", end="")   


        # tab at beginning?
        # print(str(pf.tab_stops)) 
        print()