# AI part

The script in this part is responsible for creating prediction model from an already labeled data (this is usually the graded assignments from the past)

## Labeled data and file name format
- Folder Location<br/>
To run this script, you will need a folder with the past data in a folder (in our case, we put it in `./gradebook/final/`). Because the data contains sensitive information, we do not include them in this repository but will have a general description about how to properly store your files.

- File Names<br/>
In order for the script to function properly, you will need to name your file in the following format: `<homework_code>_<semester> your own annotation`, this can be either `.csv` file or `.xlsx` file. <br/>
Because homework number could change in the future, we specify use the topic of the homework as identifier for them. Currently we have the following unique assignments:
```Python
@dataclass
class HW:
    code: str
    topic: str

HWS = [
    HW('normative_ethics', 'Normative Ethics'),
    HW('privacy', 'Privacy'),
    HW('epfoscl', 'Ethics, privacy, freedom of speech, copyrights, and laws'),
    HW('hacktivism', 'Hacktivism'),
    HW('facial_recognition', "Facial Recognition") # usually extra assignment
]
```

- File Content<br/>
Make sure in the spreadsheet you have all grading categories in your columns: `content`, `research`, `oganization`,  `communication`, `efforts`, `quality of writing`, and `bibliography`, the column indeces for essays are: `title page`, `essay body`, `essay refs`, and `word count`

## `generate_training.py` 
This script is responsible for taking out relevant data and concatenate them into a giant spread sheet with labeled data for representation learning and machine learning. If your data folder is different from the default, remember to change the `FOLDER` variable.
