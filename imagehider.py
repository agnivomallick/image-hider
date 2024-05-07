from PySide6.QtWidgets import *
from ui_imagehider import Ui_MainWindow
import os
from stegano import lsb, exifHeader
import base64

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

basedir = os.path.dirname(__file__)



try:
    from ctypes import windll
    appid = "mycompany.myproduct.subproduct.version"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)
except ImportError:
    pass


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setFixedSize(727, 475)
        self.icon = QIcon()
        self.icon.addFile(os.path.join(basedir, 'logo.ico'), QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(self.icon)

        self.ui.import_image.clicked.connect(self.get_image)

        self.ui.save_image.clicked.connect(lambda: self.lambda_helper_for_saver())

        self.ui.reveal_secret.clicked.connect(lambda: self.lambda_helper_for_revealer())

    def lambda_helper_for_saver(self):
        """
        Catching the attribute error in the save image lambda function.

        We cannot catch it just in the statement - the error is not caught.
        So we create a function and there do try-except.

        This function is passed to the lambda function.
        """
        try:
            self.get_props(self.currentfile_path, self.ui.secret_text.toPlainText())
        except AttributeError:
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Error")  # setting window icon
            # setting that ! sign icon for message box, not window icon
            msgbox.setWindowIcon(self.icon)
            msgbox.setIcon(QMessageBox.Critical)
            msgbox.setText("File was not opened.")

            execution = msgbox.exec()

    def lambda_helper_for_revealer(self):
        """
        Catching the attribute error in the reveal secret lambda function.

        We cannot catch it just in the statement - the error is not caught.
        So we create a function and there do try-except.

        This function is passed to the lambda function.
        """
        try:
            self.revealSecret(self.currentfile_path)
        except AttributeError:
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Error")  # setting window icon
            # setting that ! sign icon for message box, not window icon
            msgbox.setWindowIcon(self.icon)
            msgbox.setIcon(QMessageBox.Critical)
            msgbox.setText("File was not opened.")

            execution = msgbox.exec()

    def get_image(self):
        path = QFileDialog.getOpenFileName(self, "Open File", os.getcwd(), "Image Files (*.png *.jpeg *.jpg *.tiff)")

        if path[0] == '':
            return

        else:
            self.currentfile_path = path
            self.ui.secret_text.clear()
            self.ui.is_want_enc.setChecked(False)

    def get_props(self, file, secret_text):
        if secret_text != '':
            isEnc = self.ui.is_want_enc.isChecked()

            if isEnc:
                self.steganograph(file, secret_text, True)

            else:
                self.steganograph(file, secret_text, False)

    def steganograph(self, file, secret_text, isEnc):
        _, file_ext = os.path.splitext(file[0])

        if file_ext == '.jpeg' or file_ext == '.tiff':
            save_file_path, _ = QFileDialog.getSaveFileName(self, "Save File", os.getcwd(), "Image Files (*.png *.jpg *.jpeg *.tiff)")
            if save_file_path == '':
                return
            else:
                if isEnc:  # encrypting the text if the checkbox is checked.

                    encoded = secret_text.encode()

                    base64_bytes = base64.b64encode(encoded)
                    encrypted = base64_bytes.decode('ascii')
                    stegano_hider = exifHeader.hide(file[0], save_file_path, secret_message=encrypted)

                else:
                    stegano_hider = exifHeader.hide(file[0], save_file_path, secret_message=secret_text)

                msgbox = QMessageBox()
                msgbox.setWindowTitle("Saved file successfully") # setting window icon
                # setting that ! sign icon for message box, not window icon
                msgbox.setWindowIcon(self.icon)
                msgbox.setIcon(QMessageBox.Information)
                msgbox.setText("The file was saved successfully!")

                execution = msgbox.exec()

        else:
            save_file_path, _ = QFileDialog.getSaveFileName(self, "Save File", os.getcwd(), "Image Files (*.png *.jpg *.jpeg *.tiff)")

            if save_file_path == '':
                return
            else:

                if isEnc:
                    encoded = secret_text.encode()

                    base64_bytes = base64.b64encode(encoded)
                    encrypted = base64_bytes.decode('ascii')

                    stegano_hider = lsb.hide(file[0], encrypted)
                    stegano_hider.save(save_file_path)

                else:
                    stegano_hider = lsb.hide(file[0], secret_text)
                    stegano_hider.save(save_file_path)

                msgbox = QMessageBox()
                msgbox.setWindowTitle("Saved file successfully")# setting window icon
                # setting that ! sign icon for message box, not window icon
                msgbox.setWindowIcon(self.icon)
                msgbox.setIcon(QMessageBox.Information)
                msgbox.setText("The file was saved successfully!")

                execution = msgbox.exec()

    def revealSecret(self, file_name):
        _, file_ext = os.path.splitext(file_name[0])

        if file_ext == ".jpeg" or file_ext == ".tiff":
            try:
                revealed = exifHeader.reveal(file_name[0])

                self.ui.secret_text.clear()
                self.ui.secret_text.setText(str(revealed))

            except IndexError:
                msgbox = QMessageBox()
                msgbox.setWindowTitle("Error")
                msgbox.setWindowIcon(self.icon) # setting window icon
                # setting that ! sign icon for message box, not window icon
                msgbox.setIcon(QMessageBox.Critical)
                msgbox.setText("Nothing to reveal or cannot read message")

                execution = msgbox.exec()
        else:
            try:
                revealed = lsb.reveal(str(file_name[0]))
                self.ui.secret_text.clear()
                self.ui.secret_text.setText(str(revealed))
            except IndexError:
                msgbox = QMessageBox()
                msgbox.setWindowTitle("Error")
                msgbox.setWindowIcon(self.icon)  # setting window icon
                msgbox.setIcon(QMessageBox.Critical) # setting that ! sign icon for message box, not window icon
                msgbox.setText("Nothing to reveal or cannot read message")

                execution = msgbox.exec()




if __name__ == '__main__':
    app = QApplication()
    win = MainWindow()
    win.show()
    app.exec()

