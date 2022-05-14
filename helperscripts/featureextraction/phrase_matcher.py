class OpinionMatcher:
    """this class is supposed to find if student express their own interest or not."""
    def __init__(self, ):
        self.phrases_to_check = ["In my opnion", "I think", "I believe", "In conclusion"]
    
    def match_against(self, text: str) -> bool:
        for phrase in self.phrases_to_check:
            if phrase in text:
                return True

        return False


class ConceptMatcher:
    pass