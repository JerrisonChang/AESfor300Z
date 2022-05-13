import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

PDFJS = './gui/viewer.html'
# PDFJS = 'file:///usr/share/pdf.js/web/viewer.html'
PDF = 'essays/hw1_fa20/Assignment 1. Normative Ethics_ec529919_attempt_2020-09-15-06-45-50_EvonChoong_300Z_Assignment1.pdf'

class Window(QtWebEngineWidgets.QWebEngineView):
    def __init__(self):
        super(Window, self).__init__()
        self.load(QtCore.QUrl.fromUserInput(f"{PDFJS}"))
        # self.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (PDFJS, PDF)))

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(600, 50, 800, 600)
    window.show()
    sys.exit(app.exec_())