import pandas as pd
import read_docx
import collections

def write_content_into_gradebook(directory, gradebook_path, output_name):
    netID2content = read_docx.get_netID2content(directory)
    grade_book_df = pd.read_excel(gradebook_path, 1, engine='openpyxl')
    grade_book_df['original content'] = grade_book_df.apply(lambda row: netID2content.get(row['Username'], ''), axis = 1)
    grade_book_df.to_csv(output_name)

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

    # write_content_into_gradebook(ASSIGNMENT_DIR, GRADE_BOOK_PATH, 'hw1_entire_data.csv') 
    # split_train_test_on_item('hw1_entire_data_processed.xlsx', 'content_s')
    
    add_content_into_exisiting_gradebook(EXISTING_GRADE_BOOK_PATH, 'ICSI-300Z_hw1_summer20')

    

    
