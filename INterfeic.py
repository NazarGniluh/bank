import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Медіяплеєр')
        self.setGeometry(100, 100, 300, 200)

        self.player = QMediaPlayer()

        self.label = QLabel('Натисніть кнопку "Відкрити", щоб вибрати музичний файл', self)
        self.btn_open = QPushButton('ВІДКРИТИ', self)
        self.btn_play = QPushButton('ВІДТВОРИТИ', self)
        self.btn_pause = QPushButton('ПАУЗА', self)
        self.btn_stop = QPushButton('СТОП', self)

        self.btn_open.clicked.connect(self.open_file)
        self.btn_play.clicked.connect(self.play)
        self.btn_pause.clicked.connect(self.pause)
        self.btn_stop.clicked.connect(self.stop)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_open)
        layout.addWidget(self.btn_play)
        layout.addWidget(self.btn_pause)
        layout.addWidget(self.btn_stop)

        self.setLayout(layout)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Виберіть музичний файл", "", "MP3 files (*.mp3)")
        if file_path:
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            self.label.setText(f'Вибраний файл: {file_path}')

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

class Launcher(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('МУЗИЧНИЙ ПРОГРАВАЧ ЛАУНЧЕР')
        self.setGeometry(100, 100, 300, 100)

        self.music_player = MusicPlayer()

        self.btn_open_player = QPushButton('Відкрити музичний програвач', self)
        self.btn_open_player.clicked.connect(self.open_music_player)

        layout = QVBoxLayout()
        layout.addWidget(self.btn_open_player)
        self.setLayout(layout)

    def open_music_player(self):
        self.music_player.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    launcher = Launcher()
    launcher.show()
    sys.exit(app.exec_())