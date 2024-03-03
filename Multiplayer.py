from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import *

from INterfeic import MusicPlayer


def multi():
    multipla = QDialog()

    multipla.setWindowTitle('Мультиплеєр')
    multipla.setGeometry(100, 100, 300, 200)

    multipla.player = QMediaPlayer()

    multipla.label = QLabel('Натисніть кнопку "Відкрити", щоб вибрати музичний файл', multipla)
    multipla.btn_open = QPushButton('ВІДКРИТИ', multipla)
    multipla.btn_play = QPushButton('ВІДТВОРИТИ', multipla)
    multipla.btn_pause = QPushButton('ПАУЗА', multipla)
    multipla.btn_stop = QPushButton('СТОП', multipla)



    multipla.btn_open.clicked.connect(multipla.open_file)
    multipla.btn_play.clicked.connect(multipla.play)
    multipla.btn_pause.clicked.connect(multipla.pause)
    multipla.btn_stop.clicked.connect(multipla.stop)

    def open_file():
        file_path, _ = QFileDialog.getOpenFileName(multipla, "Виберіть музичний файл", "", "MP3 files (*.mp3)")
        if file_path:
            multipla.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            multipla.label.setText(f'Вибраний файл: {file_path}')

    def play():
        multipla.player.play()

    def pause():
        multipla.player.pause()

    def stop():
        multipla.player.stop()


    layout = QVBoxLayout()
    layout.addWidget(multipla.label)
    layout.addWidget(multipla.btn_open)
    layout.addWidget(multipla.btn_play)
    layout.addWidget(multipla.btn_pause)
    layout.addWidget(multipla.btn_stop)

    def init_ui():
        multipla.setWindowTitle('МУЗИЧНИЙ ПРОГРАВАЧ ЛАУНЧЕР')
        multipla.setGeometry(100, 100, 300, 100)

        multipla.music_player = MusicPlayer()

        multipla.btn_open_player = QPushButton('Відкрити музичний програвач', multipla)
        multipla.btn_open_player.clicked.connect(multipla.open_music_player)

        layout = QVBoxLayout()
        layout.addWidget(multipla.btn_open_player)
        multipla.setLayout(layout)

    def open_music_player():
        multipla.music_player.show()
    multipla.setLayout(layout)


