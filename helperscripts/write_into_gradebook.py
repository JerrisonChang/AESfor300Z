import pandas as pd
import read_docx 
import collections
import json

def write_content_into_gradebook(directory, gradebook_path, output_name):
    netID2content = read_docx.get_netID2content(directory)
    grade_book_df = pd.read_excel(gradebook_path, 1, engine='openpyxl')
    grade_book_df['original content'] = grade_book_df.apply(lambda row: netID2content.get(row['Username'], ''), axis = 1)
    grade_book_df.to_csv(output_name)

def append_essay_content_to_gb(base_gradebook: 'df', hw_dir) -> 'df':
    netID2content = read_docx.get_netID2content(hw_dir)
    base_gradebook['essay content'] = base_gradebook.apply(lambda row: netID2content.get(row['Username'], ''), axis=1)

    return base_gradebook

def single_out_category(base_gradebook: 'df', category: str) -> 'df':
    assert category in base_gradebook.columns
    export_gb = base_gradebook.filter(items = ['Username', category, 'essay content'])
    return export_gb

def convert_pts_to_rank(singled_cat: 'df', max_pts: str) -> 'df':
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

def split_train_test(single_cat: 'df', ratio= 0.8) -> tuple:
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

        train.append(train_data)
        test.append(test_data_of_rank)

    concat_train = pd.concat(train).sort_index()
    concat_test = pd.concat(test).sort_index()

    return (concat_train, concat_test)
    


def add_content_into_exisiting_gradebook(exisiting_gradebook_path, new_content_directory: str):
    grade_book_df = pd.read_excel(exisiting_gradebook_path, engine='openpyxl')
    
    new_content_col = grade_book_df['original content']
    new_essays = read_docx.get_netID2content('ICSI-300Z_hw1_summer20')
    for netId, content in new_essays.items():
        pass

def split_train_test_on_item(data_path:str , column_name: str):
    # get number of each rank
    df = pd.read_excel(data_path, engine='openpyxl')
    
    rank_column = df[column_name]
    distribution = collections.Counter(rank_column)
    # split each rank in 

def split_data_into_categories(dataFrame: 'df', hw_num: str):
    essay_dir = f"essays/{hw_num}_fa20"
    dataframe_with_essay = append_essay_content_to_gb(dataFrame, essay_dir)

    categories = [
        ## category, worths points , folder for the outputfile
        # ('content', '20pts', './classifiers/content_{hw_num}'),
        ('research', '20pts', './classifiers/research'),
        ('organization', '15pts', './classifiers/organization'),
        # ('communication', '15pts', './classifiers/communication_{hw_num}'),
        ('effort', '10pts', './classifiers/effort'),
        ('bibliography', '10pts', './classifiers/bibliography'),
        ('quality of writing', '10pts', './classifiers/quality_of_writing')
    ]

    for category, pts, output_dir in categories:
        temp_df = single_out_category(dataframe_with_essay, category)
        temp_rank_df = convert_pts_to_rank(temp_df, pts)
        train_test_data = split_train_test(temp_rank_df)
        output_names = ['train', 'test']

        for data, name in zip(train_test_data, output_names):
            data.to_csv(f"{output_dir}/{hw_num}_{name}.csv")

if __name__ == "__main__":
    # GRADE_BOOK_PATH = '2020_hw_DATA.xlsx'
    # EXISTING_GRADE_BOOK_PATH = 'hw1_entire_data_processed.xlsx'

    base_gb_hw1 = pd.read_excel('ICSI-300Z-Fall2020.xlsx', sheet_name=2, engine='openpyxl')

    

   
