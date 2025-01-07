# Converter MP3 para WAV
import os
from pydub import AudioSegment
from pydub.utils import which

AudioSegment.converter = which("C:/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe")
AudioSegment.ffprobe = which("C:/ffmpeg-master-latest-win64-gpl/bin/ffprobe.exe")

file_path = "AQM4zszyRP71FexfGWT1u4iuabbbg8RabEsuSM0um6LpxkHFDGw83mCIU0O_2M_J2rRMf_VQSskeQg_0NTV9AJjP.mp3"
if os.path.exists(file_path):
  print("Arquivo encontrado!")
  audio = AudioSegment.from_mp3(file_path)
  audio.export("converted_audio.wav", format="wav")
else:
  print("Arquivo não encontrado!")