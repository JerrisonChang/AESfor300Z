import pandas as pd
import os
# from helperscripts
from helperscripts.read_docx import DocxReader
import json
###
# This 
#
###
def write_content_into_gradebook(directory, gradebook_path, output_name):
    netID2content = DocxReader.get_netID2content(directory)
    grade_book_df = pd.read_excel(gradebook_path, 1, engine='openpyxl')
    grade_book_df['original content'] = grade_book_df.apply(lambda row: netID2content.get(row['Username'], ''), axis = 1)
    grade_book_df.to_csv(output_name)

def append_essay_content_to_gb(base_gradebook: pd.DataFrame, hw_dir) -> pd.DataFrame:
    netID2content = DocxReader.get_netID2content(hw_dir)
    base_gradebook['essay content'] = base_gradebook.apply(lambda row: netID2content.get(row['Username'], ''), axis=1)

    return base_gradebook

def append_structured_essay_content_to_gb(base_gradebook: pd.DataFrame, hw_dir) -> pd.DataFrame:
    reader = DocxReader(hw_dir)
    netID2structured_essay = reader.get_netID_to_structured_content()
    empty_essay = ('','','', 0, 0, 0 ,0)
    
    #features = ['title page', 'essay body', 'essay refs', 'line space', 'justification', 'indentation', 'font portion']
    features = ['title page', 'essay body', 'essay refs']
    for i, feature in enumerate(features):
        base_gradebook[feature] = base_gradebook.apply(lambda row: netID2structured_essay.get(row['Username'], empty_essay)[i], axis=1 )
    # base_gradebook['title page'] = base_gradebook.apply(lambda row: netID2structured_essay.get(row['Username'],empty_essay)[0], axis=1)
    # base_gradebook['essay body'] = base_gradebook.apply(lambda row: netID2structured_essay.get(row['Username'],empty_essay)[1], axis=1)
    # base_gradebook['essay refs'] = base_gradebook.apply(lambda row: netID2structured_essay.get(row['Username'],empty_essay)[2], axis=1)
    # base_gradebook['line space'] = base_gradebook.apply(lambda row: netID2structured_essay.get(row['Username'],empty_essay)[3], axis=1)
    # base_gradebook['justification'] = base_gradebook.apply(lambda row: netID2structured_essay.get(row['Username'],empty_essay)[4], axis=1)
    # base_gradebook['indentation'] = base_gradebook.apply(lambda row: netID2structured_essay.get(row['Username'],empty_essay)[5], axis=1)
    # base_gradebook['font portion'] = base_gradebook.apply(lambda row: netID2structured_essay.get(row['Username'],empty_essay)[6], axis=1)
    base_gradebook['word count'] = base_gradebook.apply(lambda row: len(row['essay body'].split(' ')) if len(row['essay body'].split(' '))>1 else 0, axis=1)
    base_gradebook['bibliography'] = base_gradebook.apply(lambda row: "", axis=1)

    return base_gradebook

def single_out_category(base_gradebook: pd.DataFrame, category: str) -> pd.DataFrame:
    assert category in base_gradebook.columns
    export_gb = base_gradebook.filter(items = ['Username', category, 'essay content', 'title page', 'essay body', 'essay refs'])
    return export_gb

def convert_pts_to_rank(singled_cat: pd.DataFrame, max_pts: str) -> pd.DataFrame:
    def determin_rank(scheme, point: float):
        for i, x in enumerate(scheme):
            min_, max_ = x
            if point <= max_:
                return i + 1

    with open('helperscripts/rubrics.json','r') as f:
        rubric: dict = json.load(f)
    
    assert max_pts in rubric
    scheme = rubric[max_pts]

    singled_cat.iloc[:,1] = singled_cat.iloc[:,1].apply(lambda value: determin_rank(scheme, value))
    return singled_cat

def split_train_test(single_cat: pd.DataFrame, ratio= 0.8) -> tuple:
    assert ratio < 1
    # filter out row where essays are empty but get high scores (pdfs)
    # filtered_df = single_cat.iloc[:,1].where(lambda x: x != 1) & single_cat.iloc[:,2] == ""
    # print(filtered_df)
    masks = [single_cat.iloc[:,1] == i for i in [1,2,3,4]]
 
    train = []
    test = []
    for mask in masks:
        test_data_of_rank = single_cat[mask]
        train_data = test_data_of_rank.sample(frac= ratio)
        test_data_of_rank = test_data_of_rank.drop(train_data.index)
        
        train.append(train_data)
        test.append(test_data_of_rank)

    concat_train = pd.concat(train).sort_index()
    mask = ~((concat_train.iloc[:,1] != 1) & (concat_train['essay body']== '')) # in case it is a pdf file
    concat_train = concat_train[mask]
    concat_test = pd.concat(test).sort_index()

    return (concat_train, concat_test)
    
def split_data_by_categories(dataFrame: pd.DataFrame, hw_num: str, semester_code: str):
    """
    This function will be called for creating training gradebook for each categories and put them in corresponding folders.
    """
    essay_dir = f"essays/{hw_num}_{semester_code}"
    # dataframe_with_essay = append_essay_content_to_gb(dataFrame, essay_dir)
    dataframe_with_structured_essay = append_structured_essay_content_to_gb(dataFrame, essay_dir)

    categories = [
        ## category, worths points , folder for the outputfile
        ('content', '20pts', f'./classifiers/content_{hw_num}'),
        ('research', '20pts', './classifiers/research'),
        ('organization', '15pts', './classifiers/organization'),
        ('communication', '15pts', f'./classifiers/communication_{hw_num}'),
        ('efforts', '10pts', './classifiers/effort'),
        ('bibliography', '10pts', './classifiers/bibliography'),
        ('quality of writing', '10pts', './classifiers/quality_of_writing')
    ]

    for category, pts, output_dir in categories:
        temp_df = single_out_category(dataframe_with_structured_essay, category)
        temp_rank_df = convert_pts_to_rank(temp_df, pts)
        train_test_data = split_train_test(temp_rank_df)
        output_names = ['train', 'test']

        for data, name in zip(train_test_data, output_names):
            if not os.path.isdir(output_dir):
                os.makedirs(output_dir)

            data.to_csv(f"{output_dir}/{hw_num}_{name}_structured.csv")

def create_predict_templates(path_to_blank_gb: str, path_to_essays: str, output_csv:str, input_format: str = "xlsx"):
    if input_format == "xlsx":
        df = pd.read_excel(path_to_blank_gb, sheet_name=0, engine='openpyxl').fillna(0)
    elif input_format == "csv":
        df = pd.read_csv(path_to_blank_gb).fillna(0)
    else:
        raise Exception("Type not supported")
    
    base_gb = df.loc[:, "Last Name": "Username"].copy()
    base_gb = append_structured_essay_content_to_gb(base_gb, path_to_essays)
    base_gb["comments ID"] = ""
    base_gb["customized comment"] = ""
    base_gb.to_csv(output_csv)

def create_train_csv(hw_code: str, semester_code: str):
    base_gb = pd.read_excel('ICSI-300Z-Fall2020.xlsx', sheet_name=4, engine='openpyxl').fillna(0)
    split_data_by_categories(base_gb, hw_code, semester_code)

if __name__ == "__main__":
    settings = {
        'path_to_blank_gb': './roster.xlsx',
        'path_to_essays': './essays/hw2_sp22',
        'output_csv': './gradebook/hw2_sp22/predict_template.csv'
    }
    # create_train_csv('hw4', 'fa20')
    
    create_predict_templates(**settings) 
    
    # base_gb_hw1 = pd.read_excel('ICSI-300Z-Fall2020.xlsx', sheet_name=1, engine='openpyxl').fillna(0)
    # base_gb_hw1 = pd.read_excel('hw1_s21.xlsx', sheet_name=0, engine='openpyxl').fillna(0)
    
    # base_gb_hw2 = pd.read_excel('ICSI-300Z-Fall2020.xlsx', sheet_name=2, engine= 'openpyxl').fillna(0)
    # base_gb_hw3 = pd.read_excel('ICSI-300Z-Fall2020.xlsx', sheet_name=3, engine= 'openpyxl').fillna(0)
    # split_data_by_categories(base_gb_hw1, 'hw1')
    
    
    # split_data_by_categories(base_gb_hw2, 'hw2')
    # split_data_by_categories(base_gb_hw3, 'hw3')