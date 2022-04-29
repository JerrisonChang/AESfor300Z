## AI part

The script in this part is responsible for creating prediction model from an already labeld data (this is usually the graded assignments from the past)

`generate_training.py` is responsible for taking out relevant data and concatenate them into a giant spread sheet with labeled data.

To run this script, you will need a folder with the past data in a folder (in our case, we put it in `./gradebook/final/`) and currently we support `.csv` format and `.xlsx` format. Also, make sure in the spreadsheet you have all grading categories in your columns: `content`, `research`, `oganization`,  `communication`, `efforts`, `quality of writing`, and `bibliography`, the column indeces for essays are: `title page`, `essay body`, `essay refs`, and `word count`