

RANK2SCORES = {
    "20pts": [5, 11, 17 ,20],
    "15pts": [3, 8, 13 ,15],
    "10pts": [2, 5, 9, 10]
}

CAT2COLUMN_NAME_AND_MAXPOINTS = {
    "content": ("content_prediction", "20pts"),
    "research": ("research_prediction", "20pts"),
    "organization": ("organization_prediction", "15pts"),
    "communication": ("communication_prediction", "15pts"),
    "efforts": ("efforts_prediction", "10pts"),
    "bibliography": ("bibliography", "10pts"), # bibliography doesn't have prediction yet
    "quality of writing": ("quality of writing_prediction", "10pts")
}