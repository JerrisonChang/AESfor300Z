from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import pandas as pd

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data: pd.DataFrame):
        super(TableModel, self).__init__()
        self._data = data

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
        try:
            number = int(value)
            if role == Qt.EditRole and 0 <= number <= 4:
                self._data.iloc[index.row(), index.column()] = value
                self.dataChanged.emit(index, index)
                return True
        except ValueError:
            return False
        
        return False

    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemIsEnabled
        else:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
