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

def convert_df_to_category(singled_cat: 'df', max_pts: str) -> 'df':
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
    print(distribution)
    # split each rank in 

if __name__ == "__main__":
    ASSIGNMENT_DIR = 'ICSI-300Z_Assignment1_Normative_Ethics'
    GRADE_BOOK_PATH = '2020_hw_DATA.xlsx'
    EXISTING_GRADE_BOOK_PATH = 'hw1_entire_data_processed.xlsx'

    base_gb_hw1 = pd.read_excel('ICSI-300Z-Fall2020.xlsx', sheet_name=1, engine='openpyxl')
    # print(base_gb_hw1.head)
    append_essay_content_to_gb(base_gb_hw1, 'essays/hw1_fa20')
    writing_gb = single_out_category(base_gb_hw1, 'quality of writing')
    print(convert_df_to_category(writing_gb, '10pts'))
    # abc = get_content_and_column(base_gb_hw1, 'quality of writing', 'essays/hw1_fa20')
    
    # print(abc)
    # write_content_into_gradebook(ASSIGNMENT_DIR, GRADE_BOOK_PATH, 'hw1_entire_data.csv') 
    # split_train_test_on_item('hw1_entire_data_processed.xlsx', 'content_s')
    
    # add_content_into_exisiting_gradebook(EXISTING_GRADE_BOOK_PATH, 'ICSI-300Z_hw1_summer20')

    
