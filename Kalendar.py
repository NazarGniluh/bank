from PyQt5.QtWidgets import *

def kalen():
    kalendari = QDialog()

    kalendari.setWindowTitle('Календар')

    calendar = QCalendarWidget()
    calendar.setGridVisible(True)

    layout = QVBoxLayout()
    layout.addWidget(calendar)

    kalendari.setLayout(layout)

    kalendari.show()
    kalendari.exec()