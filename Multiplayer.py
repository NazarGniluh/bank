from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import *

from INterfeic import MusicPlayer


def multi():
    def open_file():
        file_path, _ = QFileDialog.getOpenFileName(multipla, "Виберіть музичний файл", "", "MP3 files (*.mp3)")
        if file_path:
            player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))

            label.setText(f'Вибраний файл: {file_path}')


    def play():
        player.play()

    def pause():
        player.pause()

    def stop():
        player.stop()


    multipla = QDialog()

    multipla.setWindowTitle('Медіаплеєр')
    multipla.setGeometry(100, 100, 300, 200)

    player = QMediaPlayer()

    label = QLabel('Натисніть кнопку "Відкрити", щоб вибрати музичний файл')
    btn_open = QPushButton('ВІДКРИТИ')
    btn_play = QPushButton('ВІДТВОРИТИ')
    btn_pause = QPushButton('ПАУЗА')
    btn_stop = QPushButton('СТОП')
    Volume = QSlider()
    Volume.setMinimum(0)
    Volume.setMaximum(100)

    def change_vol(i):
        player.setVolume(i)

    Volume.valueChanged.connect(change_vol)
    btn_open.clicked.connect(open_file)
    btn_play.clicked.connect(play)
    btn_pause.clicked.connect(pause)
    btn_stop.clicked.connect(stop)



    lfyout1 = QHBoxLayout()

    layout = QVBoxLayout()
    lfyout1.addLayout(layout)
    layout.addWidget(label)
    layout.addWidget(btn_open)
    layout.addWidget(btn_play)
    layout.addWidget(btn_pause)
    layout.addWidget(btn_stop)
    lfyout1.addWidget(Volume)



    def open_music_player():
        multipla.music_player.show()
    multipla.setLayout(lfyout1)
    multipla.exec()


