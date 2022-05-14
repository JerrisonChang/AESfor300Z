import pandas as pd

from typing import List, Dict, Tuple

import rubric as rb
from helperscripts.readingfiles import read_spreadsheet


PATH_TO_COMMENT_BANK = "./documents/AES comments bank.xlsx"

class PostProcessor():
    def __init__(self, input_file: str):
        self.reviewed_spreadsheet = pd.read_excel(input_file,sheet_name=0,engine='openpyxl',header=0)
        self.reviewed_spreadsheet['comments ID'].fillna('', inplace=True)
        self.rank2score: Dict[str, List[int]] = rb.RANK2SCORES
        self.cat2_col_name_maxpoints: Dict[str, Tuple[str,str]] = rb.CAT2COLUMN_NAME_AND_MAXPOINTS
        self.comment_bank = read_spreadsheet(PATH_TO_COMMENT_BANK)
        self.has_comment = True
    
    def generate_two_columns(self):
        final_score = self.reviewed_spreadsheet.apply(self.calculate_final_score, axis=1)
        smart_comment = self.reviewed_spreadsheet.apply(self.write_comment, axis = 1)
        self.reviewed_spreadsheet['final score'] = final_score
        self.reviewed_spreadsheet['smart comment'] = smart_comment
   

    def get_comments(self, comment_IDs: str) -> str:
        """
        This function will take in a list of comment ID's (in string format) along with
        a comment bank (in pandas dataframe) and convert them into text format.
        """
        if comment_IDs == "":
            return ""
        else:
            comment_id_list = comment_IDs.split(',')
            comment_content = [self.comment_bank.loc[int(index_),'content'] for index_ in comment_id_list]

            return '<br/>\n'.join(comment_content)

    def write_comment(self, row: pd.Series) -> str:
        '''
        This function is used within pandas' apply function for each row in a ranked gradebook.
        It will convert the rank into scores and return the string with breakdowns and personalized comments if provided. 
        '''
        SCORE_MAP = self.rank2score
        result = []
        for category, (col_name, max_point) in self.cat2_col_name_maxpoints.items():
            try:
                index = int(row[col_name]-1)
                score = str(SCORE_MAP[max_point][index]) if index >= 0 else "0"
            except:
                score = "0"
            result.append(f"{category}: {score}/{max_point}")

        personalized_comments = "" #self.get_comments(str(row['comments ID']))

        if not pd.isna(row["customized comment"]):
            customized_comment = "<br/>\n".join(str(row["customized comment"]).split("\n")) # if row["customized comment"] != None
            personalized_comments += "<br/>\n"+customized_comment

        return '<br/>\n'.join( result +  [personalized_comments])

    def calculate_final_score(self, row: pd.Series) -> float:
        """
        This function is used within pandas' apply function for a ranked gradebook.
        It will convert the ranks into scores and return the sum of the scores
        """

        SCORE_MAP = self.rank2score
        scores = []
        for col_name, max_point in self.cat2_col_name_maxpoints.values():
            try:
                index = int(row[col_name]-1)
                score = SCORE_MAP[max_point][index] if index >= 0 else 0
            except:
                score = 0

            scores.append(score)
        
        result = sum(scores)
        if result == 20: # all categories are 1 -> did not turn in the assignment
            return 0
        else:
            return result
