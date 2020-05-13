# Import pandas as pd
import pandas
import glob

logAngles = pandas.DataFrame(pandas.read_csv('soudLocalizer_dumper/logAngles/data.log', sep=' ', header=None))
logHeadState = pandas.DataFrame(pandas.read_csv('soudlocalizer_dumper/logHeadState/data.log',
                                                sep=' ', header=None, index_col=0))
column_names = ["id", "audio_filename", "azimuth_elevation",
                "joint_0", "joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
result = pandas.DataFrame(columns=column_names)

for file in glob.glob('audioSamples/20200512-202942/*.wav'):
    id_audio = file[29:30]
    audio_timestamp = float(file[31:49])
    indexAngles = abs(logAngles[1] - audio_timestamp).idxmin()
    indexHead = abs(logHeadState[1] - logAngles.at[indexAngles, 1]).idxmin()
    result_aux = pandas.DataFrame([[id_audio, audio_timestamp, str(logAngles.at[indexAngles, 2]) + " " +
                                    str(logAngles.at[indexAngles, 3]) + " " + str(logAngles.at[indexAngles, 4]),
                                    logHeadState.at[indexHead, 2], logHeadState.at[indexHead, 3],
                                    logHeadState.at[indexHead, 4], logHeadState.at[indexHead, 5],
                                    logHeadState.at[indexHead, 6], logHeadState.at[indexHead, 7]]],
                                  columns=column_names)
    result = result.append(result_aux, ignore_index=True)

result.to_csv('result.csv', index=False)
