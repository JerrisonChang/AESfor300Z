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
