# import sys
# import subprocess
from pytube import YouTube
import ffmpeg
from pytube.exceptions import VideoUnavailable, RegexMatchError


class PytubeDownloader:
    resolutions = {'1': [299, 140],
                   '2': [136, 140],
                   '3': [135, 140],
                   '4': [134, 140],
                   '5': [133, 140],
                   '6': [160, 140]}  # The resolution match by it number and itag for audio and video

    def __init__(self, url, pathvideo='./downloads/video.mp4', pathaudio='./downloads/audio.mp4'):
        try:
            self.video = YouTube(url)
            self.pathvideo = ffmpeg.input(pathvideo)
            self.pathaudio = ffmpeg.input(pathaudio)
        except VideoUnavailable:
            print('This video is unavailable')
            exit()
        except RegexMatchError:
            print('Please enter a valid youtube video URL!')
            exit()

    def Summary(self):
        print('Summary:')
        print(f'Title: {self.video.title}')
        print(f'Duration: {self.video.length / 60:.2f} minutes')
        print(f'Rating: {self.video.rating:.2f}')
        print(f'{self.video.views} views\n')
        print('What resolution you want?')

    def Download(self, command):
        self.video.streams.get_by_itag(self.resolutions[command][0])\
            .download(output_path='./downloads/', filename='video')
        self.video.streams.get_by_itag(self.resolutions[command][1])\
            .download(output_path='./downloads/', filename='audio')

    def FFmpegConcat(self):
        ffmpeg.concat(self.pathvideo, self.pathaudio, v=1, a=1).output(f'./downloads/{self.video.title}.mp4').run()
        # Same FFmpeg process to join video and audio but using subprocess instead of ffmpeg-python
        # subprocess.run(f"""ffmpeg -i self.pathvideo -i self.pathaudio
        #              -c 'copy' './downloads/{self.video.title}.mp4'""")
# ---------------------------------------------------------------------------------------------------------------------


print('Paste the URL of the video:')
# video = YouTube(input())
# for i in video.streams.filter(file_extension='mp4'):
#     print(i)
run = PytubeDownloader(input())
run.Summary()
run.Download(input('1 - 1080p, 2 - 720p, 3 - 480p, 4 - 360, 5 - 240p, 6 - 144p : '))
run.FFmpegConcat()
