from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import pandas as pd

from typing import List, Set

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


class CommentTable(TableModel):
    boxCheckedSignal = QtCore.pyqtSignal(int, name="boxChecked")
    boxUncheckedSignal = QtCore.pyqtSignal(int, name="boxUnchecked")
    
    def __init__(self, data: pd.DataFrame, checked_set: Set[int] = None):
        super().__init__(data)

        self.checks = {} if checked_set is None else {QtCore.QPersistentModelIndex(self.index(i-1, 0)): 2 for i in checked_set}

    def data(self, index, role = Qt.DisplayRole):
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            return f'{self._data.iloc[row, col]}'
        
        if role == Qt.CheckStateRole and col == 0:
            return self.checkState(QtCore.QPersistentModelIndex(index))
        
        # return None

    def checkState(self, index):
        if index in self.checks:
            return self.checks[index]
        else:
            return Qt.Unchecked

    def setData(self, index, value, role=Qt.EditRole):

        if not index.isValid():
            return False

        if role == Qt.CheckStateRole:
            self.checks[QtCore.QPersistentModelIndex(index)] = value
            # print(f"{index} checked!!! {value}")
            row, col = index.row(), index.column()
            if value == 2: # checked
                self.boxCheckedSignal.emit(row + 1)
                # print(f"checked {row} {col}")
            else: # unchecked
                self.boxUncheckedSignal.emit(row + 1)
                # print(f"unchecked {row} {col}")
                pass
            return True
        return False

    def flags(self, index):
        fl = QtCore.QAbstractTableModel.flags(self, index)
        if index.column() == 0:
            fl |= Qt.ItemIsUserCheckable | Qt.ItemIsSelectable
        return fl
