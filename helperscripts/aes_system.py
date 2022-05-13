from helperscripts.read_docx import DocxReader
import helperscripts.write_into_gradebook as WIG
from helperscripts.post_process import PostProcessor

# class pre_processing(Ui_MainWindow):
#     def proceed_btn():
#         # check if all three boxed are already filled ....
#         WIG.create_predict_templates(path_to_blank_gb= Ui_MainWindow.roster_string, path_to_essays= Ui_MainWindow.essay_dir_string , output_csv= Ui_MainWindow.output_dir)
#         # go to the next tab

if __name__ == "__main__":
    HOMEWORK_CODE = "hw4_sp22"
    data_processing_settings = {
        'path_to_blank_gb': f'./gradebook/{HOMEWORK_CODE}/roster.xlsx',
        # 'path_to_blank_gb': f'./test2.csv',
        'path_to_essays': f'./essays/{HOMEWORK_CODE}',
        'output_csv': f'./gradebook/{HOMEWORK_CODE}/predict_template_hw4.csv'
    }

    post_processing_settings = {
        'input_file': f'./gradebook/{HOMEWORK_CODE}/{HOMEWORK_CODE}_ready_for_post.xlsx',
        'output_file': f'./gradebook/{HOMEWORK_CODE}/{HOMEWORK_CODE} grades with comments.csv'
    }

    # uncomment this line for data preparation process
    #WIG.create_predict_templates(**data_processing_settings)
    
    ## uncomment the following two lines for post processing
    # processor = PostProcessor(post_processing_settings['input_file'])
    # processor.process_to_csv(post_processing_settings['output_file'])
