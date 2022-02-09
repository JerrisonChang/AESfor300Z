from helperscripts.read_docx import DocxReader
from helperscripts.post_process import PostProcessor
import helperscripts.write_into_gradebook as WIG

if __name__ == "__main__":
    HOMEWORK_CODE = "hw1_fa21"
    data_processing_settings = {
        'path_to_blank_gb': f'./gradebook/{HOMEWORK_CODE}/roster.xlsx',
        'path_to_essays': f'./essays/{HOMEWORK_CODE}',
        'output_csv': f'./gradebook/{HOMEWORK_CODE}/predict_template_1122_3.csv'
    }

    post_processing_settings = {
        'input_file': f'./gradebook/{HOMEWORK_CODE}/{HOMEWORK_CODE}_gradebook_2.xlsx',
        'output_file': f'./gradebook/{HOMEWORK_CODE}/{HOMEWORK_CODE} grades with comments.csv'
    }

    # uncomment this line for data preparation process
    WIG.create_predict_templates(**data_processing_settings)
    
    ## uncomment the following two lines for post processing
    # processor = PostProcessor(post_processing_settings['input_file'])
    # processor.process_to_csv(post_processing_settings['output_file'])
