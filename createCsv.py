# Import pandas as pd
import pandas
import glob

logAngles = pandas.DataFrame(pandas.read_csv('soudLocalizer_dumper/logAngles/data.log', sep=' ', header=None))
logHeadState = pandas.DataFrame(pandas.read_csv('soudlocalizer_dumper/logHeadState/data.log', sep=' ', header=None))

for file in glob.glob('audioSamples/20200512-202942/*.wav'):
    id_audio = file[29:30]
    audio_filenames = file[31:49]









