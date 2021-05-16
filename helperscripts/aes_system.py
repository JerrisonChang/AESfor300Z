from read_docx import DocxReader
from post_process import PostProcessor
import write_into_gradebook as wig

if __name__ == "__main__":
    HOMEWORK_CODE = "hw4_s21_demo"
    data_processing_settings = {
        'path_to_blank_gb': f'./gradebook/{HOMEWORK_CODE}/roster.xlsx',
        'path_to_essays': './essays/hw4_s21',
        'output_csv': f'./gradebook/{HOMEWORK_CODE}/predict_template.csv'
    }

    post_processing_settings = {
        'input_file': f'./gradebook/{HOMEWORK_CODE}/hw4_s21_gradebook_demo.xlsx',
        'output_file': f'./gradebook/{HOMEWORK_CODE}/hw4_s21 grades with comments.csv'
    }

    ## uncomment this line for data preparation process
    # wig.create_predict_templates(**data_processing_settings)
    
    ## uncomment the following two lines for post processing
    processor = PostProcessor(post_processing_settings['input_file'])
    processor.process_to_csv(post_processing_settings['output_file'])
