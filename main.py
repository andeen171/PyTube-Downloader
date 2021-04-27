from PyQt5 import QtCore, QtGui, QtWidgets
from interface import Ui_MainWindow
from pytube import YouTube
import ffmpeg
from pytube.exceptions import VideoUnavailable, RegexMatchError

resolutions = []
itags = []


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        class status: status = True

        def Link():
            global video
            resolutions.clear()
            itags.clear()
            try:
                print(self.txtURL.toPlainText())
                video = YouTube(str(self.txtURL.toPlainText()))
            except VideoUnavailable:
                print('This video is unavailable')
            except RegexMatchError:
                print('Please enter a valid youtube video URL!')
            else:
                Resolutions()

        def Resolutions():
            global resolutions
            for i in video.streams:
                i = str(i).split()
                resolutions.append(i[3].strip('res="'))
                itags.append(i[1].strip('itag="'))
            for i in resolutions:
                self.cbxResolutions.addItem(i)
            Summary()

        def Summary():
            self.lblName.setText(video.title)
            self.lblViews.setText(f'{self.video.views} views')
            self.lblDuration.setText(f'Duration: {self.video.length / 60:.2f} minutes')

        def Download(command):
            self.video.streams.get_by_itag(self.resolutions[1][0]) \
                .download(output_path='./downloads/', filename='video')
            self.video.streams.get_by_itag(self.resolutions[command][1]) \
                .download(output_path='./downloads/', filename='audio')

        def FFmpegConcat():
            ffmpeg.concat(self.pathvideo, self.pathaudio, v=1, a=1).output(f'./downloads/{self.video.title}.mp4').run()

        self.psbCheck.clicked.connect(lambda: Link())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
