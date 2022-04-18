from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import pandas as pd

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data: pd.DataFrame, file_path: str):
        super(TableModel, self).__init__()
        self._data = data
        self._file_path = file_path

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return str(self._data.iloc[index.row(), index.column()])

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            
            if orientation == Qt.Vertical:
                return str(self._data.index[section])

    def setData(self, index, value, role):
        if role == Qt.EditRole and value:
            self._data.iloc[index.row(), index.column()] = value
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def save(self):
        self._data.to_csv(self._file_path, encoding='utf-8')