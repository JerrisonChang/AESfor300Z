# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\design files\comment.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from functools import partial
from tabnanny import check
from xml.etree.ElementTree import Comment
from PyQt5 import QtCore, QtGui, QtWidgets
from helperscripts.comments_loader import load_comment_bank
from TableModel import CommentTable
from enum import Enum


class Catagories(Enum):
    CONTENT = "content"
    RESEARCH = "research"
    ORGANIZATION = "oganization"
    COMMUNICATION = "communication"
    EFFORTS = "efforts"
    QUALITY = "quality of writing"
    BIBLIOGRAPHY = "bibliography"

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1018, 613)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableView__comments = QtWidgets.QTableView(Form)
        self.tableView__comments.setObjectName("tableView__comments")
        self.horizontalLayout_2.addWidget(self.tableView__comments)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label__filter = QtWidgets.QLabel(Form)
        self.label__filter.setMinimumSize(QtCore.QSize(120, 0))
        self.label__filter.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label__filter.setObjectName("label__filter")
        self.verticalLayout_2.addWidget(self.label__filter)
        self.radio__show_all = QtWidgets.QRadioButton(Form)
        self.radio__show_all.setChecked(True)
        self.radio__show_all.setObjectName("radio__show_all")
        self.verticalLayout_2.addWidget(self.radio__show_all)
        self.radio__content = QtWidgets.QRadioButton(Form)
        self.radio__content.setObjectName("radio__content")
        self.verticalLayout_2.addWidget(self.radio__content)
        self.radio__research = QtWidgets.QRadioButton(Form)
        self.radio__research.setObjectName("radio__research")
        self.verticalLayout_2.addWidget(self.radio__research)
        self.radio__organization = QtWidgets.QRadioButton(Form)
        self.radio__organization.setObjectName("radio__organization")
        self.verticalLayout_2.addWidget(self.radio__organization)
        self.radio__communication = QtWidgets.QRadioButton(Form)
        self.radio__communication.setObjectName("radio__communication")
        self.verticalLayout_2.addWidget(self.radio__communication)
        self.radio__quality = QtWidgets.QRadioButton(Form)
        self.radio__quality.setObjectName("radio__quality")
        self.verticalLayout_2.addWidget(self.radio__quality)
        self.radio__efforts = QtWidgets.QRadioButton(Form)
        self.radio__efforts.setObjectName("radio__efforts")
        self.verticalLayout_2.addWidget(self.radio__efforts)
        self.radio__bibliography = QtWidgets.QRadioButton(Form)
        self.radio__bibliography.setObjectName("radio__bibliography")
        self.verticalLayout_2.addWidget(self.radio__bibliography)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.setStretch(3, 2)
        self.verticalLayout_2.setStretch(4, 2)
        self.verticalLayout_2.setStretch(5, 2)
        self.verticalLayout_2.setStretch(6, 2)
        self.verticalLayout_2.setStretch(7, 2)
        self.verticalLayout_2.setStretch(8, 2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label__cust_comments = QtWidgets.QLabel(Form)
        self.label__cust_comments.setObjectName("label__cust_comments")
        self.verticalLayout.addWidget(self.label__cust_comments)
        self.plainTextEdit__cust_comments = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit__cust_comments.setMaximumSize(QtCore.QSize(16777215, 100))
        self.plainTextEdit__cust_comments.setObjectName("plainTextEdit__cust_comments")
        self.verticalLayout.addWidget(self.plainTextEdit__cust_comments)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.setupFunctions()
    
    def setupFunctions(self):
        self.currentStudentCommentDf = load_comment_bank().fillna("")
        self.proxy_model = QtCore.QSortFilterProxyModel()
        self.proxy_model.setFilterKeyColumn(1)
        self.proxy_model.setSourceModel(CommentTable(self.currentStudentCommentDf))
        self.tableView__comments.setModel(self.proxy_model)
        self.tableView__comments.setColumnWidth(0, 400)
        self.tableView__comments.resizeRowsToContents()
        filtered_btns = [
            self.radio__show_all,
            self.radio__content,
            self.radio__research,
            self.radio__communication,
            self.radio__organization,
            self.radio__efforts,
            self.radio__quality, 
            self.radio__bibliography
        ]
        columns = [None, 'content', 'research', 'communication', 'organization', 'effort', 'quality of writing', 'bibliography']
        for i, name in zip(filtered_btns, columns):
            slot = partial(self.enable_disable_mod, *(i, name))
            i.toggled.connect(slot)

        # self.tableView__comments.resizeColumnsToContents()
    def enable_disable_mod(self, checkbox: QtWidgets.QRadioButton, name: str):
        # checks = self.tableView__comments.model().get_check_state()
        
        if checkbox.isChecked():
            if not name is None:
                self.proxy_model.setFilterFixedString(name)
                print(f"{name} is checked")
            else:
                self.proxy_model.setFilterFixedString("")

            self.tableView__comments.resizeRowsToContents()
                


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label__filter.setText(_translate("Form", "Filter Comments:"))
        self.radio__show_all.setText(_translate("Form", "Show All"))
        self.radio__content.setText(_translate("Form", "Content"))
        self.radio__research.setText(_translate("Form", "Research"))
        self.radio__organization.setText(_translate("Form", "Organization"))
        self.radio__communication.setText(_translate("Form", "Communication"))
        self.radio__quality.setText(_translate("Form", "Quality of Writing"))
        self.radio__efforts.setText(_translate("Form", "Efforts"))
        self.radio__bibliography.setText(_translate("Form", "Bibliography"))
        self.label__cust_comments.setText(_translate("Form", "Customized Comments:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
