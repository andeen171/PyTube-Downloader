import sys
import subprocess
from pytube import YouTube
import ffmpeg

print(sys.path)
print('Paste the URL of the video:')
command = input()
resolutions = ['1080p', '720p', '480p', '360p', '240p', '144p']

video = YouTube(command)
print('Summary:')
print(f'Title: {video.title}')
print(f'Duration: {video.length / 60:.2f} minutes')
print(f'Rating: {video.rating:.2f}')
print(f'# of views: {video.views}')
print('')
print('What resolution you want?')
print('1 - 1080p, 2 - 720p, 3 - 480p, 4 - 360, 5 - 240p, 6 - 144p')
command = int(input())
for i in video.streams.filter(file_extension="mp4", res=resolutions[command - 1]):
    print(i)

command = int(input('What version of the video?(only input the itag!)'))
video.streams.get_by_itag(command).download(output_path='./downloads/', filename='video')

for i in video.streams.filter(file_extension="mp4", type='audio'):
    print(i)

command = int(input('What version of the audio in the video?(only input the itag!)'))
video.streams.get_by_itag(command).download(output_path='./downloads/', filename='audio')

input_video = ffmpeg.input('./downloads/video.mp4')

input_audio = ffmpeg.input('./downloads/audio.mp4')

ffmpeg.concat(input_video, input_audio, v=1, a=1).output(f'./downloads/{video.title}.mp4').run()

# videofile = "./downloads/video.mp4"
# audiofile = "./downloads/audio.mp4"
# outputfile = "./downloads/finished_video.mp4"
# codec = "copy"
# subprocess.run(f"ffmpeg -i {videofile} -i {audiofile} -c {codec} {outputfile}")
