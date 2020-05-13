# Import pandas as pd
import pandas
import glob

logAngles = pandas.DataFrame(pandas.read_csv('soudLocalizer_dumper/logAngles/data.log', sep=' ', header=None))
logHeadState = pandas.DataFrame(pandas.read_csv('soudlocalizer_dumper/logHeadState/data.log',
                                                sep=' ', header=None, index_col=0))

for file in glob.glob('audioSamples/20200512-202942/*.wav'):
    id_audio = file[29:30]
    audio_timestamp = float(file[31:49])
    indexAngles = abs(logAngles[1] - audio_timestamp).idxmin()
    indexHead = abs(logHeadState[1] - logAngles.at[indexAngles, 1]).idxmin()

    #result = [id_audio, audio_timestamp, logAngles.loc[indexAngles], logHeadState.loc[indexHead]]

