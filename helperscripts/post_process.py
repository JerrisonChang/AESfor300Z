import pandas as pd

settings = {
    # 'input_file': './gradebook/hw2_s21/predict_template_all_ranks.csv',
    'output_file': './gradebook/hw2_s21/finish postprocessing_v2.csv'
}

df = pd.read_csv(settings['input_file'])

# rank2score = {
#     "20pts": [0, 10, 15, 19],
#     "15pts": [0, 7, 12, 14], 
#     "10pts": [0, 4.5, 7, 9.5] 
#     #TODO: set thresholds to upgrade score to perfect score
# }
rank2score_v2 = {
    "20pts": [5, 11, 17 ,20],
    "15pts": [3, 8, 13 ,15],
    "10pts": [2, 5, 9, 10]
}


def write_comment(row, rank2score: dict = rank2score_v2) -> str:
    content = "content: " + str(rank2score["20pts"][int(row['content_prediction']-1)]) + "/20pts;"
    research = "research: " + str(rank2score["20pts"][int(row['research_prediction']-1)]) + "/20pts;"
    organization = "organization: " + str(rank2score["15pts"][int(row['organization_prediction']-1)]) + "/15pts;"
    communication = "communication: " + str(rank2score["15pts"][int(row['communication_prediction']-1)]) + "/15pts;"
    efforts = "efforts: " + str(rank2score["10pts"][int(row['efforts_prediction']-1)]) + "/10pts;"
    # bibliography = "bibliography: "+ str(rank2score["10pts"][int(row['bibliography']-1)]) + "/10pts;"
    quality_of_writing = "quality of writing: "+ str(rank2score["10pts"][int(row['quality of writing_prediction']-1)]) + "/10pts;"

    # return '\n'.join([content,research,organization,communication,efforts, bibliography, quality_of_writing])
    return '\n'.join([content,research,organization,communication,efforts, quality_of_writing])

def calculate_final_score(row, rank2score: dict = rank2score_v2) -> float:
    content = rank2score["20pts"][int(row['content_prediction'])-1]
    research = rank2score["20pts"][int(row['research_prediction'])-1]
    organization = rank2score["15pts"][int(row['organization_prediction'])-1]
    communication = rank2score["15pts"][int(row['communication_prediction'])-1]
    efforts = rank2score["10pts"][int(row['efforts_prediction'])-1]
    # bibliography = rank2score["10pts"][int(row['bibliography'])-1]
    quality_of_writing = rank2score["10pts"][int(row['quality of writing_prediction'])-1]

    # return sum([content,research,organization,communication,efforts, bibliography, quality_of_writing])
    return sum([content,research,organization,communication,efforts, quality_of_writing])

final_score = df.apply(lambda row: calculate_final_score(row, rank2score_v2), axis=1)
smart_comment = df.apply(lambda row: write_comment(row, rank2score_v2), axis = 1)

df['final score'] = final_score
df['smart comment'] = smart_comment

df.to_csv(settings['output_file'])