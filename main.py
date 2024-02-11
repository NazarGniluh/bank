
import sys
from PyQt5.QtWidgets import (
QApplication, QWidget, QVBoxLayout, QCalendarWidget)

class CalendarApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Календар')
        self.setGeometry(100, 200, 300, 300)

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)

        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calendar_app = CalendarApp()
    calendar_app.show()
    sys.exit(app.exec_())





