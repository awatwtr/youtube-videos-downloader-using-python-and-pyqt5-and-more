import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QRadioButton, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
from pytube import YouTube, Playlist
import os
from PyQt5.QtCore import Qt
from PyQt5 import QtCore



class YouTubeDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()

     # Manage the window   
    def initUI(self):
        self.setWindowTitle('YouTube Video Downloader')
        self.setGeometry(100, 100, 500, 500)
        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False) # block the "Full-Screen" Buttom


        # Manage the logo
        
        logo_label = QLabel(self)
        logo_label.setPixmap(QPixmap('YTlogo.png')) # logo
        logo_label.move(225, 50)
        logo_label.setScaledContents(True)
        logo_label.setAlignment(Qt.AlignCenter)
        logo_label.setFixedSize(100, 100)
        
        # option what user went to downloads?
        self.single_video_rb = QRadioButton('Single Video', self) 
        self.single_video_rb.move(150, 200)
        self.single_video_rb.setChecked(True)
        
        self.playlist_rb = QRadioButton('Playlist', self)
        self.playlist_rb.move(250, 200)
        
        # URL of the youtube videos.
        self.url_le = QLineEdit(self)
        self.url_le.move(100, 250)
        self.url_le.resize(300, 30)
        self.url_le.setPlaceholderText('Enter URL') 
        
        # Download Buttom
        download_btn = QPushButton('Download', self)
        download_btn.move(200, 300)
        download_btn.clicked.connect(self.download)
        
        # path. where user went to located the dowload
    def download(self):
        got_path = QFileDialog.getExistingDirectory(self, 'Select Download Location')
        link_url = self.url_le.text()
        
        # checking user choise
        if self.single_video_rb.isChecked():
            yt = YouTube(link_url)
            yt.streams.get_highest_resolution().download(got_path)
            os.startfile(got_path)
       
        # checking user choise
        if self.playlist_rb.isChecked():
            yt_playlist = Playlist(link_url)
            for video in yt_playlist.videos:
                video.streams.get_highest_resolution().download(got_path)
            os.startfile(got_path)


# to run the tool you need this part 
# without this the tool can't run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YouTubeDownloader()
    ex.show()
    sys.exit(app.exec_())
