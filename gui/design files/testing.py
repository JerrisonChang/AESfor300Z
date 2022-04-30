# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui\design files\ui_design.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import sys
import os
# from operator import itemgetter

from PyQt5 import QtCore, QtGui, QtWidgets
from AI_part.generate_training import read_spread_sheet
from TableModel import TableModel
import pandas as pd

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
        self.output__dir = QtWidgets.QLineEdit(self.output_group_box)
        self.output__dir.setInputMask("")
        self.output__dir.setObjectName("output__dir")
        self.horizontalLayout_9.addWidget(self.output__dir)
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
        self.output__file_name = QtWidgets.QLineEdit(self.output_group_box)
        self.output__file_name.setObjectName("output__file_name")
        self.horizontalLayout_8.addWidget(self.output__file_name)
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
        # self.std_name__listView = QtWidgets.QListView(self.Reviewing)
        # self.std_name__listView.setMaximumSize(QtCore.QSize(16777215, 30))
        # self.std_name__listView.setObjectName("std_name__listView")
        # self.verticalLayout_11.addWidget(self.std_name__listView)
        self.std_name__comboBox = QtWidgets.QComboBox(self.Reviewing)
        self.std_name__comboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.std_name__comboBox.setObjectName("std_name__comboBox")
        self.verticalLayout_11.addWidget(self.std_name__comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem1)
        self.current_grade__label = QtWidgets.QLabel(self.Reviewing)
        self.current_grade__label.setObjectName("current_grade__label")
        self.verticalLayout_11.addWidget(self.current_grade__label)
        self.grade_table = QtWidgets.QTableView()
        # self.grade_table = QtWidgets.QTableWidget(self.Reviewing)
        # self.grade_table.setMinimumSize(QtCore.QSize(0, 180))
        # self.grade_table.setMaximumSize(QtCore.QSize(16777215, 200))
        # self.grade_table.setAutoFillBackground(False)
        # self.grade_table.setObjectName("grade_table")
        # self.grade_table.setColumnCount(2)
        # self.grade_table.setRowCount(6)
        # item = QtWidgets.QTableWidgetItem()
        # self.grade_table.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.grade_table.setVerticalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.grade_table.setVerticalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.grade_table.setVerticalHeaderItem(3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.grade_table.setVerticalHeaderItem(4, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.grade_table.setVerticalHeaderItem(5, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.grade_table.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.grade_table.setHorizontalHeaderItem(1, item)
        # self.grade_table.horizontalHeader().setVisible(False)
        # self.grade_table.horizontalHeader().setCascadingSectionResizes(False)
        # self.grade_table.horizontalHeader().setDefaultSectionSize(120)
        # self.grade_table.horizontalHeader().setMinimumSectionSize(50)
        # self.grade_table.horizontalHeader().setStretchLastSection(True)
        # self.grade_table.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_11.addWidget(self.grade_table)
        self.horizontalLayout_11.addLayout(self.verticalLayout_11)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.additional_info__label = QtWidgets.QLabel(self.Reviewing)
        self.additional_info__label.setMinimumSize(QtCore.QSize(250, 0))
        self.additional_info__label.setObjectName("additional_info__label")
        self.verticalLayout_4.addWidget(self.additional_info__label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
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

        self.review__next_std_btn.clicked.connect(lambda: self.load_data(pd.DataFrame([[1,None],[2, None]], columns=["machine", "human"], index=["a", "b"]), './testing2.csv'))
        self.review__save_btn.clicked.connect(lambda: self.currentModel.save())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tab2_setup()

    def tab2_setup(self):
        browse_file_option = {
            "default_path": "./gradebook/final",
            "title": "Select Predicted spread sheet",
            "file_format": "Spread sheets (*.csv *.xlsx)",
            "action": self.load_predicted
        }
        self.select_predicted__browse_btn.clicked.connect(lambda: self.browse_file(self.select_predicted__line, browse_file_option))

    def load_data(self, data: pd.DataFrame, path:str):
        self.currentModel = TableModel(data, path)
        self.grade_table.setModel(self.currentModel)

    def browse_file(self, target_line: QtWidgets.QLineEdit, options: dict):
        TITLE = options.get("title", "Open file")
        DEFAULT_PATH = options.get("default_path", "./")
        FILE_FORMAT = options.get("file_format", None)
        fname = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, TITLE, DEFAULT_PATH, FILE_FORMAT)
        target_line.setText(fname[0])

        if "action" in options:
            options.get("action")()

    def load_predicted(self):
        fileName = self.select_predicted__line.text()
        self.tab2__master_df = read_spread_sheet(fileName)

        self.get_student_name()
        # dlg = QtWidgets.QMessageBox()
        # dlg.setWindowTitle("success!")
        # dlg.setText("complete loading predicted spreadsheet")
        # button = dlg.exec()

        # if button == QtWidgets.QMessageBox.Ok:
        #     print("OK!!")

    def get_student_name(self):
        def df_get_student_name(row: pd.Series):
            display = f"{row.get('First Name')} {row.get('Last Name')} ({row.get('Username')})"
            value = row.get('Username')
            return (display, value)
        
        assert isinstance(self.tab2__master_df, pd.DataFrame)

        student_names = self.tab2__master_df.apply( df_get_student_name, axis=1).to_list()
        std_dict = {key: val for key, val in student_names}
        self.std_name__comboBox.clear()
        self.std_name__comboBox.addItems(std_dict.keys())

        pass


    def read_spread_sheet(path: str) -> pd.DataFrame:
        _, extension = os.path.splitext(path)
        
        if extension == '.csv':
            return pd.read_csv(path, encoding='utf-8')
        elif extension == '.xlsx':
            return pd.read_excel(path, engine="openpyxl")
        else:
            raise ExtensionError(f"Unsupported extension type; expected: .csv or .xlsx, got {extension}")


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
        self.output__dir.setText(_translate("MainWindow", "hw1_sp22_predict_template.csv"))
        self.output__label.setText(_translate("MainWindow", "directory:"))
        self.output__browse_btn.setText(_translate("MainWindow", "Browse"))
        self.output__proceed_btn.setText(_translate("MainWindow", "Proceed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.preProcessing), _translate("MainWindow", "Preprocessing"))
        self.load_predited__group_box.setTitle(_translate("MainWindow", "Load prediction templates"))
        self.select_predicted__browse_btn.setText(_translate("MainWindow", "Browse"))
        self.std_name__label.setText(_translate("MainWindow", "Student:"))
        self.current_grade__label.setText(_translate("MainWindow", "Current grades:"))
        # item = self.grade_table.verticalHeaderItem(0)
        # item.setText(_translate("MainWindow", "research"))
        # item = self.grade_table.verticalHeaderItem(1)
        # item.setText(_translate("MainWindow", "communication"))
        # item = self.grade_table.verticalHeaderItem(2)
        # item.setText(_translate("MainWindow", "organization"))
        # item = self.grade_table.verticalHeaderItem(3)
        # item.setText(_translate("MainWindow", "efforts"))
        # item = self.grade_table.verticalHeaderItem(4)
        # item.setText(_translate("MainWindow", "quality of writing"))
        # item = self.grade_table.verticalHeaderItem(5)
        # item.setText(_translate("MainWindow", "bibliography"))
        # item = self.grade_table.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "machine predicted"))
        # item = self.grade_table.horizontalHeaderItem(1)
        # item.setText(_translate("MainWindow", "human correction"))
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

    path = './gui/test.csv'
    df = pd.read_csv(path, index_col=0)

    df2 = pd.DataFrame([[1,None],[2, None]], columns=["machine", "human"], index=["a", "b"])

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.load_data(df, path)
    MainWindow.show()
    sys.exit(app.exec())
