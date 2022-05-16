import pandas as pd

from .docxreader import DocxReader

from typing import Dict, Tuple

class PreProcessor():
    def __init__(self, roster: pd.DataFrame):
        self.roster = roster
        self.features = [
            ['title page', ''], #title, default value
            ['essay body', ''], 
            ['essay refs', '']
        ]
        self.default_essay = [default_value for _, default_value in self.features]

    def append_structured_essay_content_to_gradebook(self, essay_directory: str) -> pd.DataFrame:
        df = self.roster.copy()
        reader = DocxReader(essay_directory)
        netID2structured_essay = reader.get_netID_to_structured_content()
        
        for i, (feature_title, _) in enumerate(self.features):
            df[feature_title] = df.apply(self.append_feature_to_cell, args=(netID2structured_essay, i), axis=1 )
        
        df['bibliography'] = ""
        df['word count'] = df.apply(self.get_word_count, axis=1)

        return df

    def create_prediction_template(self, essay_directory: str) -> None:
        self.prediction_template = self.roster.loc[:, "Last Name": "Username"].copy()
        self.prediction_template = self.append_structured_essay_content_to_gradebook(essay_directory)
        self.prediction_template["comments ID"] = ""
        self.prediction_template["customized comment"] = ""
        
    def save_prediction_template(self, output_path: str) -> None:
        assert not self.prediction_template is None
        
        self.prediction_template.to_csv(output_path, index=False)

    def get_word_count(self, row: pd.Series) -> int:
        words = row['essay body'].split(' ')
        if len(words) > 1:
            return len(words)
        else:
            return 0

    def append_feature_to_cell(self, row: pd.Series, essay_dict: Dict[str, Tuple], index: int):
        userId = row['Username']
        
        return essay_dict.get(userId, self.default_essay)[index]