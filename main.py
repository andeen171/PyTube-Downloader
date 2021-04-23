import sys
# import subprocess
from pytube import YouTube
import ffmpeg

print('Paste the URL of the video:')
command = input()
resolutions = {'1': [160, 140],
               '2': [160, 140],
               '3': [160, 140],
               '4': [160, 140],
               '5': [160, 140],
               '6': [160, 140]}

video = YouTube(command)

print('Summary:')
print(f'Title: {video.title}')
print(f'Duration: {video.length / 60:.2f} minutes')
print(f'Rating: {video.rating:.2f}')
print(f'{video.views} views\n')
print('What resolution you want?')
command = input('1 - 1080p, 2 - 720p, 3 - 480p, 4 - 360, 5 - 240p, 6 - 144p : ')
video.streams.get_by_itag(resolutions[command][0]).download(output_path='./downloads/', filename='video')
video.streams.get_by_itag(resolutions[command][1]).download(output_path='./downloads/', filename='audio')

input_video = ffmpeg.input('./downloads/video.mp4')

input_audio = ffmpeg.input('./downloads/audio.mp4')

ffmpeg.concat(input_video, input_audio, v=1, a=1).output(f'./downloads/{video.title}.mp4').run()

# videofile = "./downloads/video.mp4"
# audiofile = "./downloads/audio.mp4"
# outputfile = "./downloads/finished_video.mp4"
# codec = "copy"
# subprocess.run(f"ffmpeg -i {videofile} -i {audiofile} -c {codec} {outputfile}")
