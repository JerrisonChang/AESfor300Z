from PyQt5.QtWidgets import QMessageBox


def show_message(type: int, message: str):
    """
    type: 1= error, 2=success
    """
    msg = QMessageBox()
    if type == 1:
        msg.setWindowTitle("Something went wrong")
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
    else:
        msg.setWindowTitle("Success!")
        msg.setText(message)

    msg.exec_()
