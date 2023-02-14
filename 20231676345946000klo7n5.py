import os
import subprocess
from pydub import AudioSegment

# 删除文件名中的空格
for filename in os.listdir():
    if filename.endswith(".mp4"):
        new_filename = filename.replace(" ", "")
        os.rename(filename, new_filename)

# 转换文件为 mp3
for filename in os.listdir():
    if filename.endswith(".mp4"):
        sound = AudioSegment.from_file(filename)
        sound.export(filename[:-3] + "mp3", format="mp3")

# 增加 mp3 文件的末尾 4 秒的空白时长
for filename in os.listdir():
    if filename.endswith(".mp3"):
        sound = AudioSegment.from_file(filename)
        silence = AudioSegment.silent(duration=4000)
        sound = sound + silence
        sound.export(filename, format="mp3")

# 合并所有 mp3 文件
filenames = [filename for filename in os.listdir() if filename.endswith(".mp3")]
sound = AudioSegment.from_file(filenames[0])
for filename in filenames[1:]:
    sound = sound + AudioSegment.from_file(filename)
sound.export("chen.mp3", format="mp3")

# 删除所有过程生成的 mp3 文件，但保留 chen.mp3 文件
for filename in os.listdir():
    if filename.endswith(".mp3") and filename != "chen.mp3":
        os.remove(filename)
