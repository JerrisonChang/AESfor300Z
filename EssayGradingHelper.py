# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.12
#

import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.TableModel import TableModel
import pandas as pd

from gui.comment_part import CommentWidget
from models.preprocessor import PreProcessor
from models.postprocessor import PostProcessor
from helperscripts.readingfiles import read_spreadsheet
from gui.quickutil import show_message

from typing import Set


HUMAN_COLUMNS = ['content', 'research', 'organization', 'communication', 'efforts', 'quality of writing', 'bibliography']
COLUMNS = ['content_prediction', 'research_prediction', 'organization_prediction', 'communication_prediction', 'efforts_prediction', 'quality of writing_prediction', 'bibliography']
COMMENT_ID_SEP = ", "
class ExtensionError(Exception):
    pass

class Tabs():
    pass

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 800)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setKerning(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName("tabWidget")
        self.preProcessing = QtWidgets.QWidget()
        self.preProcessing.setObjectName("preProcessing")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.preProcessing)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_group_box = QtWidgets.QGroupBox(self.preProcessing)
        self.input_group_box.setObjectName("input_group_box")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.input_group_box)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.select_roster__label = QtWidgets.QLabel(self.input_group_box)
        self.select_roster__label.setObjectName("select_roster__label")
        self.verticalLayout_6.addWidget(self.select_roster__label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.select_roster__line = QtWidgets.QLineEdit(self.input_group_box)
        self.select_roster__line.setObjectName("select_roster__line")
        self.horizontalLayout_5.addWidget(self.select_roster__line)
        self.select_roster__browse_btn = QtWidgets.QPushButton(self.input_group_box)
        self.select_roster__browse_btn.setObjectName("select_roster__browse_btn")
        self.horizontalLayout_5.addWidget(self.select_roster__browse_btn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.select_dir__label = QtWidgets.QLabel(self.input_group_box)
        self.select_dir__label.setObjectName("select_dir__label")
        self.verticalLayout_6.addWidget(self.select_dir__label)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.select_dir__line = QtWidgets.QLineEdit(self.input_group_box)
        self.select_dir__line.setObjectName("select_dir__line")
        self.horizontalLayout_6.addWidget(self.select_dir__line)
        self.select_dir__browse_btn = QtWidgets.QPushButton(self.input_group_box)
        self.select_dir__browse_btn.setObjectName("select_dir__browse_btn")
        self.horizontalLayout_6.addWidget(self.select_dir__browse_btn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addWidget(self.input_group_box)
        self.output_group_box = QtWidgets.QGroupBox(self.preProcessing)
        self.output_group_box.setObjectName("output_group_box")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.output_group_box)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label = QtWidgets.QLabel(self.output_group_box)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        self.output__file_name_line = QtWidgets.QLineEdit(self.output_group_box)
        self.output__file_name_line.setInputMask("")
        self.output__file_name_line.setObjectName("output__dir")
        self.horizontalLayout_9.addWidget(self.output__file_name_line)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.output__label = QtWidgets.QLabel(self.output_group_box)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setKerning(True)
        self.output__label.setFont(font)
        self.output__label.setObjectName("output__label")
        self.horizontalLayout_8.addWidget(self.output__label)
        self.output__dir_line = QtWidgets.QLineEdit(self.output_group_box)
        self.output__dir_line.setObjectName("output__file_name")
        self.horizontalLayout_8.addWidget(self.output__dir_line)
        self.output__browse_btn = QtWidgets.QPushButton(self.output_group_box)
        self.output__browse_btn.setObjectName("output__browse_btn")
        self.horizontalLayout_8.addWidget(self.output__browse_btn)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10.addLayout(self.verticalLayout_10)
        self.output__proceed_btn = QtWidgets.QPushButton(self.output_group_box)
        self.output__proceed_btn.setMinimumSize(QtCore.QSize(130, 50))
        self.output__proceed_btn.setAutoDefault(False)
        self.output__proceed_btn.setDefault(False)
        self.output__proceed_btn.setFlat(False)
        self.output__proceed_btn.setObjectName("output__proceed_btn")
        self.horizontalLayout_10.addWidget(self.output__proceed_btn)
        self.verticalLayout.addWidget(self.output_group_box)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.tabWidget.addTab(self.preProcessing, "")
        self.Reviewing = QtWidgets.QWidget()
        self.Reviewing.setObjectName("Reviewing")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.Reviewing)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.load_predited__group_box = QtWidgets.QGroupBox(self.Reviewing)
        self.load_predited__group_box.setObjectName("load_predited__group_box")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.load_predited__group_box)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.select_predicted__line = QtWidgets.QLineEdit(self.load_predited__group_box)
        self.select_predicted__line.setObjectName("select_predicted__line")
        self.horizontalLayout_2.addWidget(self.select_predicted__line)
        self.select_predicted__browse_btn = QtWidgets.QPushButton(self.load_predited__group_box)
        self.select_predicted__browse_btn.setObjectName("select_predicted__browse_btn")
        self.horizontalLayout_2.addWidget(self.select_predicted__browse_btn)
        self.verticalLayout_13.addWidget(self.load_predited__group_box)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.std_name__label = QtWidgets.QLabel(self.Reviewing)
        self.std_name__label.setObjectName("std_name__label")
        self.verticalLayout_11.addWidget(self.std_name__label)
        self.std_name__comboBox = QtWidgets.QComboBox(self.Reviewing)
        self.std_name__comboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.std_name__comboBox.setObjectName("std_name__comboBox")
        self.verticalLayout_11.addWidget(self.std_name__comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem1)
        # self.commentWidget_customed = CommentWidgetWindow()
        self.commentWidget = CommentWidget(self.Reviewing)
        # self.commentWidget = QtWidgets.QWidget()
        # self.commentWidget_customed.setupUi(self.commentWidget)
        self.verticalLayout_11.addWidget(self.commentWidget)
        self.current_grade__label = QtWidgets.QLabel(self.Reviewing)
        self.current_grade__label.setObjectName("current_grade__label")
        # self.verticalLayout_11.addWidget(self.current_grade__label)
        self.grade_table = QtWidgets.QTableView()
        # self.verticalLayout_11.addWidget(self.grade_table)
        self.horizontalLayout_11.addLayout(self.verticalLayout_11)
        self.horizontalLayout_11.setStretch(0, 2)
        self.horizontalLayout_11.setStretch(1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.additional_info__label = QtWidgets.QLabel(self.Reviewing)
        self.additional_info__label.setMinimumSize(QtCore.QSize(300, 0))
        self.additional_info__label.setObjectName("additional_info__label")
        self.verticalLayout_4.addWidget(self.additional_info__label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.verticalLayout_4.addWidget(self.current_grade__label)
        self.verticalLayout_4.addWidget(self.grade_table)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.review__save_btn = QtWidgets.QPushButton(self.Reviewing)
        self.review__save_btn.setObjectName("review__save_btn")
        self.horizontalLayout_3.addWidget(self.review__save_btn)
        self.review__next_std_btn = QtWidgets.QPushButton(self.Reviewing)
        self.review__next_std_btn.setObjectName("review__next_std_btn")
        self.horizontalLayout_3.addWidget(self.review__next_std_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_11.addLayout(self.verticalLayout_4)
        self.verticalLayout_13.addLayout(self.horizontalLayout_11)
        self.tabWidget.addTab(self.Reviewing, "")
        self.PostProcessing = QtWidgets.QWidget()
        self.PostProcessing.setObjectName("PostProcessing")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.PostProcessing)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.select_gradebook__label = QtWidgets.QLabel(self.PostProcessing)
        self.select_gradebook__label.setObjectName("select_gradebook__label")
        self.horizontalLayout_12.addWidget(self.select_gradebook__label)
        self.select_gradebook__line = QtWidgets.QLineEdit(self.PostProcessing)
        self.select_gradebook__line.setMinimumSize(QtCore.QSize(200, 0))
        self.select_gradebook__line.setObjectName("select_gradebook__line")
        self.horizontalLayout_12.addWidget(self.select_gradebook__line)
        self.select_gradebook__browse_btn = QtWidgets.QPushButton(self.PostProcessing)
        self.select_gradebook__browse_btn.setObjectName("select_gradebook__browse_btn")
        self.horizontalLayout_12.addWidget(self.select_gradebook__browse_btn)
        self.verticalLayout_14.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.select_bb_sheet__label = QtWidgets.QLabel(self.PostProcessing)
        self.select_bb_sheet__label.setObjectName("select_bb_sheet__label")
        self.horizontalLayout_13.addWidget(self.select_bb_sheet__label)
        self.select_bb_sheet__line = QtWidgets.QLineEdit(self.PostProcessing)
        self.select_bb_sheet__line.setObjectName("select_bb_sheet__line")
        self.horizontalLayout_13.addWidget(self.select_bb_sheet__line)
        self.select_bb_sheet__browse_btn = QtWidgets.QPushButton(self.PostProcessing)
        self.select_bb_sheet__browse_btn.setObjectName("select_bb_sheet__browse_btn")
        self.horizontalLayout_13.addWidget(self.select_bb_sheet__browse_btn)
        self.verticalLayout_14.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14.addLayout(self.verticalLayout_14)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem3)
        self.finish_btn = QtWidgets.QPushButton(self.PostProcessing)
        self.finish_btn.setMinimumSize(QtCore.QSize(150, 50))
        self.finish_btn.setObjectName("finish_btn")
        self.horizontalLayout_14.addWidget(self.finish_btn)
        self.horizontalLayout_14.setStretch(0, 10)
        self.horizontalLayout_14.setStretch(1, 1)
        self.horizontalLayout_14.setStretch(2, 3)
        self.verticalLayout_15.addLayout(self.horizontalLayout_14)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem4)
        self.tabWidget.addTab(self.PostProcessing, "")
        self.verticalLayout_12.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 991, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tab1_setup()
        self.tab2_setup()
        self.tab3_setup()
    
    def tab1_setup(self):
        OUTPUT_DIR_LINE = self.output__dir_line
        OUTPUT_FILE_NAME = self.output__file_name_line
        def update_outputs():
            if not self.select_roster__line.text(): return

            file_path = self.select_roster__line.text()
            dir_text, file_name = os.path.split(file_path)
            get_output_name(file_name)
            OUTPUT_DIR_LINE.setText(dir_text)

        def get_output_name(file_name:str) -> str:
            fname, _ = os.path.splitext(file_name)
            OUTPUT_FILE_NAME.setText(f"{fname}__prediction_template.csv")

        self.select_roster__browse_btn.clicked.connect(lambda x: self.browse_file( self.select_roster__line, {"title": "Select Roster File", "action": update_outputs}))
        self.select_dir__browse_btn.clicked.connect(lambda x: self.browse_directory( self.select_dir__line, {"title": "Select Directory"}))
        self.output__browse_btn.clicked.connect(lambda x: self.browse_directory( self.output__file_name_line, {"title": "Select Output Directory"}))
        self.output__proceed_btn.clicked.connect(self.create_prediction_template)
        
    
    def tab2_setup(self):
        browse_file_option = {
            "default_path": "./gradebook/final",
            "title": "Select Predicted spread sheet",
            "file_format": "Spread sheets (*.csv *.xlsx)",
            "action": self.load_predicted
        }
        self.select_predicted__browse_btn.clicked.connect(lambda x: self.browse_file(self.select_predicted__line, browse_file_option))
        self.std_name__comboBox.currentIndexChanged.connect(self.change_current_student)
        self.review__next_std_btn.clicked.connect(self.next_student)
        self.review__save_btn.clicked.connect(self.tab2_save)
        # self.commentWidget.checkComment.connect(lambda x: self.update_human_df_comments_id(x))
        self.commentWidget.checkComment.connect(self.update_human_df_comment_ids)
        self.commentWidget.typeComment.connect(self.update_human_df_customized_comments)

    def tab3_setup(self):
        default_path = "./gradebook/"
        self.select_gradebook__browse_btn.clicked.connect(lambda x: self.browse_file(self.select_gradebook__line, {"title": "Select Gradebook file", "default_path": default_path}))
        self.select_bb_sheet__browse_btn.clicked.connect(lambda x: self.browse_file(self.select_bb_sheet__line, {"title": "Select Blackboard worksheet", "default_path": default_path}))
        self.finish_btn.clicked.connect(lambda x: self.finish_button())
    
    def tab2_save(self):
        current_file_path = self.select_predicted__line.text()
        dir_, file_ =  os.path.split(current_file_path)
        file_name, _ = os.path.splitext(file_)
        output_path = f"{file_name}_human_graded.xlsx"
        writer = pd.ExcelWriter(os.path.join(dir_, output_path), engine='xlsxwriter')
        self.tab2__human_df.loc[:, HUMAN_COLUMNS + ["comments ID", "customized comment"]].to_excel(writer, sheet_name='human')
        self.tab2__master_df.loc[:, COLUMNS].to_excel(writer, sheet_name='machine')

        writer.save()
        show_message(2, f"Your human reviewed spreadsheet is saved in: {output_path}")

    def next_student(self):
        index = self.std_name__comboBox.currentIndex()
        self.std_name__comboBox.setCurrentIndex(index + 1)

    def browse_file(self, target_line: QtWidgets.QLineEdit, options: dict):
        TITLE = options.get("title", "Open file")
        DEFAULT_PATH = options.get("default_path", "./")
        FILE_FORMAT = options.get("file_format", None)
        fname = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, TITLE, DEFAULT_PATH, FILE_FORMAT)
        target_line.setText(fname[0])

        if "action" in options:
            options.get("action")()

    def browse_directory(self, target_line: QtWidgets.QLineEdit, options: dict):
        TITLE = options.get("title", "Open Diretory")
        DEFAULT_PATH = options.get("default_path", "/Users/sernd/EASfor300Z/essays/")
        fname = QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, TITLE, DEFAULT_PATH)
        target_line.setText(fname)

    def display_grades(self, netId: str):
        machine = self.tab2__master_df.loc[netId, COLUMNS].rename({a: b for a,b in zip(COLUMNS, HUMAN_COLUMNS)})
        human = self.tab2__human_df.loc[netId, HUMAN_COLUMNS]
        df = pd.DataFrame({'machine': machine, 'human': human}, index= HUMAN_COLUMNS)
        self.current_std_Table = TableModel(df)
        self.current_std_Table.dataChanged.connect(lambda x: self.update_human_df(netId, df['human']))
        self.grade_table.setModel(self.current_std_Table)
        
    def display_comments(self, netId: str):
        pure_text = self.tab2__human_df.loc[netId, "comments ID"]
        id_set = set([int(i) for i in pure_text.split(COMMENT_ID_SEP)]) if len(pure_text) > 0 else None
        customized_comment = self.tab2__human_df.loc[netId, "customized comment"]
        
        self.commentWidget.change_comments(id_set, customized_comment)
        
        
    def update_human_df(self, netId: str, data: pd.Series):
        for i in HUMAN_COLUMNS:
            self.tab2__human_df.loc[netId, i] = data[i]

    def update_human_df_comment_ids(self, comments_ids: Set[int]):
        try: self.tab2__std_dict
        except AttributeError as e:
            print("not finished initialization yet")
            return
        
        current_netId = self.tab2__std_dict.get(self.std_name__comboBox.currentText(), None)
        if not current_netId: return

        self.tab2__human_df.loc[current_netId, "comments ID"] = COMMENT_ID_SEP.join([str(i) for i in comments_ids])

    def update_human_df_customized_comments(self, comments: str):
        current_netId = self.tab2__std_dict.get(self.std_name__comboBox.currentText())
        self.tab2__human_df.loc[current_netId, "customized comment"] = comments

    def load_predicted(self):
        fileName = self.select_predicted__line.text()
        if not fileName: return
        self.tab2__master_df = read_spreadsheet(fileName)
        self.tab2__master_df.set_index("Username", inplace=True)
        self.tab2__human_df = self.tab2__master_df.rename({old: new for old, new in zip(COLUMNS, HUMAN_COLUMNS)}, axis=1)
        self.tab2__human_df["comments ID"] = ""
        self.tab2__human_df["customized comment"] = ""
        self.get_student_name()

    def get_student_name(self):
        def df_get_student_name(row: pd.Series):
            display = f"{row.get('First Name')} {row.get('Last Name')} ({row.name})"
            value = row.name
            return (display, value)
        
        assert isinstance(self.tab2__master_df, pd.DataFrame)

        student_names = self.tab2__master_df.apply( df_get_student_name, axis=1).to_list()
        self.tab2__std_dict = {key: val for key, val in student_names}
        self.std_name__comboBox.clear()
        self.std_name__comboBox.addItems(self.tab2__std_dict.keys())

        pass

    def change_current_student(self, x):
        text = self.std_name__comboBox.currentText()
        index = self.std_name__comboBox.currentIndex()
        netId = self.tab2__std_dict[text]
        
        # update next button
        if index == len(self.tab2__std_dict) - 1:
            self.review__next_std_btn.setEnabled(False)
        else:
            self.review__next_std_btn.setEnabled(True)

        # display table
        self.display_grades(netId)
        self.display_comments(netId)
    
    def create_prediction_template(self):
        path_to_roster = self.select_roster__line.text()
        essay_directory = self.select_dir__line.text()
        output_csv = os.path.join(self.output__dir_line.text(), self.output__file_name_line.text())
        
        if not (path_to_roster and essay_directory and output_csv ):
            show_message(1, "You haven't finished the input.")
            return
        
        roster_df = read_spreadsheet(path_to_roster)
        pre_processor = PreProcessor(roster_df)
        pre_processor.create_prediction_template(essay_directory)
        pre_processor.save_prediction_template(output_csv)
        
        # WIG.create_predict_templates(path_to_roster ,essay_directory , output_csv)

        show_message(2, f"Your prediction template is generated at {output_csv}!!")
        self.tabWidget.setCurrentIndex(1)

    def finish_button(self):
        path_to_reviewed_spread_sheet = self.select_gradebook__line.text()
        path_to_roster_file = self.select_bb_sheet__line.text()
        roster_df = read_spreadsheet(path_to_roster_file)
        post_processor = PostProcessor(path_to_reviewed_spread_sheet)
        
        post_processor.generate_two_columns()
        new_roster_df = post_processor.append_to_roster(roster_df)
        
        try:
            new_roster_df.to_csv(path_to_roster_file, index=False)
            show_message(2, f"Your file has been successfully saved to {path_to_roster_file} and is ready to be uploaded!!")
        except PermissionError as e:
            show_message(1, f"It seems like you have the file open, please close the file and try again.")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Essay Grading Helper"))
        self.input_group_box.setTitle(_translate("MainWindow", "Input"))
        self.select_roster__label.setText(_translate("MainWindow", "Select roster file:"))
        self.select_roster__browse_btn.setText(_translate("MainWindow", "Browse"))
        self.select_dir__label.setText(_translate("MainWindow", "Select essay directory"))
        self.select_dir__browse_btn.setText(_translate("MainWindow", "Browse"))
        self.output_group_box.setTitle(_translate("MainWindow", "Output"))
        self.label.setText(_translate("MainWindow", "file name:"))
        self.output__label.setText(_translate("MainWindow", "directory:"))
        self.output__browse_btn.setText(_translate("MainWindow", "Browse"))
        self.output__proceed_btn.setText(_translate("MainWindow", "Proceed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.preProcessing), _translate("MainWindow", "Preprocessing"))
        self.load_predited__group_box.setTitle(_translate("MainWindow", "Load prediction templates"))
        self.select_predicted__browse_btn.setText(_translate("MainWindow", "Browse"))
        self.std_name__label.setText(_translate("MainWindow", "Student:"))
        self.current_grade__label.setText(_translate("MainWindow", "Current grades:"))
        self.additional_info__label.setText(_translate("MainWindow", "Additional information:"))
        self.review__save_btn.setText(_translate("MainWindow", "Save"))
        self.review__next_std_btn.setText(_translate("MainWindow", "Next Student"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Reviewing), _translate("MainWindow", "Reviewing"))
        self.select_gradebook__label.setText(_translate("MainWindow", "Select the grade book"))
        self.select_gradebook__browse_btn.setText(_translate("MainWindow", "browse"))
        self.select_bb_sheet__label.setText(_translate("MainWindow", "Select the blackboard work sheet"))
        self.select_bb_sheet__browse_btn.setText(_translate("MainWindow", "browse"))
        self.finish_btn.setText(_translate("MainWindow", "Finish"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PostProcessing), _translate("MainWindow", "Post Processing"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show() 
    sys.exit(app.exec())
