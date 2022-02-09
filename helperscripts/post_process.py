import pandas as pd

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
        
        self.rank2score = {
            "20pts": [5, 11, 17 ,20],
            "15pts": [3, 8, 13 ,15],
            "10pts": [2, 5, 9, 10]
        } if rank2score == None else rank2score

    def process_to_csv(self, output_file_path:str):
        final_score = self.main_gradebook.apply(self.calculate_final_score, axis=1)
        smart_comment = self.main_gradebook.apply(self.write_comment, axis = 1)
        self.main_gradebook['final score'] = final_score
        self.main_gradebook['smart comment'] = smart_comment

        self.main_gradebook.to_csv(output_file_path, index=False)

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

    def write_comment(self, row) -> str:
        '''
        This function is used within pandas' apply function for each row in a ranked gradebook.
        It will convert the rank into scores and return the string with breakdowns and personalized comments if provided. 
        '''
        content = "content: " + str(self.rank2score["20pts"][int(row['content_prediction']-1)]) + "/20pts;"
        research = "research: " + str(self.rank2score["20pts"][int(row['research_prediction']-1)]) + "/20pts;"
        organization = "organization: " + str(self.rank2score["15pts"][int(row['organization_prediction']-1)]) + "/15pts;"
        communication = "communication: " + str(self.rank2score["15pts"][int(row['communication_prediction']-1)]) + "/15pts;"
        efforts = "efforts: " + str(self.rank2score["10pts"][int(row['efforts_prediction']-1)]) + "/10pts;"
        try:
            bibliography = "bibliography: "+ str(self.rank2score["10pts"][int(row['bibliography']-1)]) + "/10pts;"
        except:
            bibliography = "bibliography: 0/10pts;"
        quality_of_writing = "quality of writing: "+ str(self.rank2score["10pts"][int(row['quality of writing_prediction']-1)]) + "/10pts;"

        # if self.has_comment:
        personalized_comments = "" #self.get_comments(str(row['comments ID']))

        if not pd.isna(row["customized comment"]):
            customized_comment = "<br/>\n".join(str(row["customized comment"]).split("\n")) # if row["customized comment"] != None
            personalized_comments += "<br/>\n"+customized_comment

        return '<br/>\n'.join([content,research,organization,communication,efforts, bibliography, quality_of_writing, personalized_comments])
        # return '<br/>\n'.join([content,research,organization,communication,efforts, bibliography, quality_of_writing])

    def calculate_final_score(self, row) -> float:
        """
        This function is used within pandas' apply function for a ranked gradebook.
        It will convert the ranks into scores and return the sum of the scores
        """
        try:
            content = self.rank2score["20pts"][int(row['content_prediction'])-1]
            research = self.rank2score["20pts"][int(row['research_prediction'])-1]
            organization = self.rank2score["15pts"][int(row['organization_prediction'])-1]
            communication = self.rank2score["15pts"][int(row['communication_prediction'])-1]
            efforts = self.rank2score["10pts"][int(row['efforts_prediction'])-1]
            try:
                bibliography = self.rank2score["10pts"][int(row['bibliography'])-1]
            except:
                bibliography = 0
            quality_of_writing = self.rank2score["10pts"][int(row['quality of writing_prediction'])-1]

            result = sum([content,research,organization,communication,efforts, bibliography, quality_of_writing])

            if result == 20: # all categories are 1 -> did not turn in the assignment
                return 0
            else:
                return sum([content,research,organization,communication,efforts, bibliography, quality_of_writing])
        except:
            return 0

if __name__ == "__main__":
    settings = {
        'input_file': './hw4_s21_gradebook.xlsx',
        'output_file': './hw4_s21 grades with comments v2.csv'
    }

    processor = PostProcessor(settings['input_file'])
    processor.process_to_csv(settings['output_file'])