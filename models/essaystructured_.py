from dataclasses import dataclass, field
from typing import List, Dict

from docx.text.paragraph import Paragraph

@dataclass
class EssayStructured:
    # raw_doc: Document
    file_name: str
    student_id: str
    title: List[Paragraph] = field(default_factory=list)
    body: List[Paragraph] = field(default_factory=list)
    reference: List[Paragraph] = field(default_factory=list)
    others: List[Paragraph] = field(default_factory=list)
    scores: Dict[str, int] = field(default_factory=dict)

    def preview(self,):
        """This is for debugging purposes"""
        print(f"\n>>>TITLE")
        for i in self.title:
            print(i.text)

        print(f"\n>>>BODY")
        for i in self.body:
            print(i.text[:80], "...")
        
        print(f"\n>>>REFERENCE")
        for i in self.reference:
            print(i.text)

    def get_title(self): 
        return '\n'.join([i.text.strip() for i in self.title])

    def get_body(self): 
        return '\n'.join([i.text.strip() for i in self.body])
    
    def get_reference(self): 
        return '\n'.join([i.text.strip() for i in self.reference])

    def get_word_count(self):
        return sum([len(i.text.split(" ")) for i in self.body])

    def to_list(self) -> List[str]:
        return [self.file_name, self.student_id, *[self.para_to_text(i) for i in [self.title, self.body, self.reference]]]

    def para_to_text(self, para: List[Paragraph]) -> str:
        return '\n'.join(p.text for p in para)

    def attach_score(self, scores: Dict[str, int]):
        self.scores = scores
