import pandas as pd

def get_comments(comment_df, comment_IDs: str) -> str:
    """
    This function will take in a list of comment ID's (in string format) along with
    a comment bank (in pandas dataframe) and convert them into text format.
    """
    if comment_IDs == "":
        return ""
    elif ',' not in comment_IDs:
        return comment_df.loc[int(comment_IDs), 'content']
    else:
        comment_id_list = comment_IDs.split(',')
        comment_content = [comment_df.loc[int(index_),'content'] for index_ in comment_id_list]

        return '<br/>\n'.join(comment_content)

def write_comment(row, rank2score: dict, comment_df: 'df'= None, has_personalized_comments:bool = False) -> str:
    '''
    This function is used within pandas' apply function for each row in a ranked gradebook.
    It will convert the rank into scores and return the string with breakdowns and personalized comments if provided. 
    '''

    content = "content: " + str(rank2score["20pts"][int(row['content_prediction']-1)]) + "/20pts;"
    research = "research: " + str(rank2score["20pts"][int(row['research_prediction']-1)]) + "/20pts;"
    organization = "organization: " + str(rank2score["15pts"][int(row['organization_prediction']-1)]) + "/15pts;"
    communication = "communication: " + str(rank2score["15pts"][int(row['communication_prediction']-1)]) + "/15pts;"
    efforts = "efforts: " + str(rank2score["10pts"][int(row['efforts_prediction']-1)]) + "/10pts;"
    try:
        bibliography = "bibliography: "+ str(rank2score["10pts"][int(row['bibliography']-1)]) + "/10pts;"
    except:
        bibliography = "bibliography: 0/10pts;"
    quality_of_writing = "quality of writing: "+ str(rank2score["10pts"][int(row['quality of writing_prediction']-1)]) + "/10pts;"

    if has_personalized_comments:
        personalized_comments = get_comments(comment_df, str(row['comments ID']))

        if not pd.isna(row["customized comment"]):
            customized_comment = "<br/>\n".join(str(row["customized comment"]).split("\n")) # if row["customized comment"] != None
            personalized_comments += "<br/>\n"+customized_comment

    return '<br/>\n'.join([content,research,organization,communication,efforts, bibliography, quality_of_writing, personalized_comments])
    # return '<br/>\n'.join([content,research,organization,communication,efforts, bibliography, quality_of_writing])

def calculate_final_score(row, rank2score: dict) -> float:
    """
    This function is used within pandas' apply function for a ranked gradebook.
    It will convert the ranks into scores and return the sum of the scores
    """
    try:
        content = rank2score["20pts"][int(row['content_prediction'])-1]
        research = rank2score["20pts"][int(row['research_prediction'])-1]
        organization = rank2score["15pts"][int(row['organization_prediction'])-1]
        communication = rank2score["15pts"][int(row['communication_prediction'])-1]
        efforts = rank2score["10pts"][int(row['efforts_prediction'])-1]
        try:
            bibliography = rank2score["10pts"][int(row['bibliography'])-1]
        except:
            bibliography = 0
        quality_of_writing = rank2score["10pts"][int(row['quality of writing_prediction'])-1]

        return sum([content,research,organization,communication,efforts, bibliography, quality_of_writing])
        # return sum([content,research,organization,communication,efforts, quality_of_writing])
    except:
        return 0

if __name__ == "__main__":
    settings = {
        # 'input_file': './gradebook/hw2_s21/predict_template_all_ranks.csv',
        'input_file': './gradebook/hw4_s21/hw4_s21_gradebook.xlsx',
        # 'output_file': './gradebook/hw2_s21/finish postprocessing_v2.csv'
        'output_file': './gradebook/hw4_s21/hw4_s21 grades with comments.csv'
    }

    # df = pd.read_csv(settings['input_file'])
    df = pd.read_excel(settings['input_file'],sheet_name=0,engine='openpyxl')
    df['comments ID'].fillna('',inplace=True)

    comment_df = pd.read_excel(settings['input_file'],sheet_name=1, engine='openpyxl',index_col=0)
    rank2score_v2 = {
        "20pts": [5, 11, 17 ,20],
        "15pts": [3, 8, 13 ,15],
        "10pts": [2, 5, 9, 10]
    }

    final_score = df.apply(lambda row: calculate_final_score(row, rank2score_v2), axis=1)
    smart_comment = df.apply(lambda row: write_comment(row, rank2score_v2, comment_df, True), axis = 1)

    df['final score'] = final_score
    df['smart comment'] = smart_comment

    df.to_csv(settings['output_file'],index=False)