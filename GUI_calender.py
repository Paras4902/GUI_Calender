from PySide2.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.calendar = QCalendarWidget()
        self.setWindowTitle("Pyside2 Calendar")
        self.setGeometry(300, 200, 500, 400)
        self.create_calender()
        self.show()

    def create_calender(self):
        vbox = QVBoxLayout()
        self.calendar.setGridVisible(True)

        vbox.addWidget(self.calendar)
        self.setLayout(vbox)


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    window = Window()
    myapp.exec_()
    sys.exit()
