# Import pandas as pd
import pandas
import glob

logAngles = pandas.DataFrame(pandas.read_csv('soudLocalizer_dumper/logAngles/data.log'))
print(logAngles)

for file in glob.glob('audioSamples/20200512-202942/*.wav'):
    print(file)
    id_audio = file[29:30]
    audio_filenames = file[31:49]
    print(id_audio)
    print(audio_filenames)









