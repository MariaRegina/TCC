import os
from pydub import AudioSegment


vai = open("C:/Users/Public/BaseTCC/cv-corpus-7.0-2021-07-21/pt/clips/common_voice_pt_19273359.mp3")
#
#
print(vai.name)

print(os.path.getsize('C:/Users/Public/BaseTCC/cv-corpus-7.0-2021-07-21/pt/clips/common_voice_pt_19273359.mp3'))
#

# sound = AudioSegment.from_mp3(vai.name)

# sound = AudioSegment.from_mp3('C:/Users/Public/BaseTCC/cv-corpus-7.0-2021-07-21/pt/clips/common_voice_pt_19273359.mp3')
# sound.export("file.wav", format="wav")
# from pydub import AudioSegment
#
# # str =
# #
# sound = AudioSegment.from_mp3(r'C:/Users/Public/BaseTCC/cv-corpus-7.0-2021-07-21/pt/clips/common_voice_pt_19273359.mp3')
# sound.export("audio.wav", format="wav")

# from audioToCSV import audioToCSV
#
# fazAcontecer = audioToCSV()
#
# fazAcontecer.inicio()