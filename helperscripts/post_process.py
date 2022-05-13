from re import M
import pandas as pd
import os
from typing import List, Dict, Tuple

class PostProcessor():
    def __init__(self, input_file, rank2score: dict = None):
        self.main_gradebook = pd.read_excel(input_file,sheet_name=0,engine='openpyxl',header=0)
        self.main_gradebook['comments ID'].fillna('',inplace=True)
        # print(self.main_gradebook[:3])

        try:
            self.comment_bank: pd.DataFrame = pd.read_excel(input_file,sheet_name=1, engine='openpyxl',index_col=0)
            self.has_comment: bool = True
        except:
            self.comment_bank: pd.DataFrame = pd.DataFrame()
            self.has_comment: bool = False
            print(f"No second sheets!")
        
        self.rank2score: Dict[str, List[int]] = {
            "20pts": [5, 11, 17 ,20],
            "15pts": [3, 8, 13 ,15],
            "10pts": [2, 5, 9, 10]
        } if rank2score == None else rank2score

        self.cat2_col_name_maxpoints: Dict[str, Tuple[str,str]] = {
            "content": ("content_prediction", "20pts"),
            "research": ("research_prediction", "20pts"),
            "organization": ("organization_prediction", "15pts"),
            "communication": ("communication_prediction", "15pts"),
            "efforts": ("efforts_prediction", "10pts"),
            "bibliography": ("bibliography", "10pts"), # bibliography doesn't have prediction yet
            "quality of writing": ("quality of writing_prediction", "10pts")
        }

    def generate_two_columns(self):
        final_score = self.main_gradebook.apply(self.calculate_final_score, axis=1)
        smart_comment = self.main_gradebook.apply(self.write_comment, axis = 1)
        self.main_gradebook['final score'] = final_score
        self.main_gradebook['smart comment'] = smart_comment
        # df = pd.read_csv('uploadfile.csv')
        # print(self.main_gradebook['final score'])

        

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

# if __name__ == "__main__":
#     settings = {
#         'input_file': './hw1_sp22.xlsx',
#         'output_file': './hw1_sp22 grades with comments v2.csv'
#     }
    # processor = PostProcessor(settings['input_file'])
    # processor.process_to_csv(settings['output_file'])
    # df = pd.read_excel('./gradebook/hw1_sp22/hw1_sp22_gradebook_1.xlsx',sheet_name=1,engine='openpyxl',header=0)
    # print(df)
    # path = './gradebook/hw1_sp22/hw1_sp22_gradebook_1.xlsx
    # print(os.path.isfile(path))
