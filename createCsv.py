if __name__ == '__main__':
    import pandas
    import glob

    ID_AUDIO = AUDIO_NAME = AUDIO_TIMESTAMP = ""
    INDEX_ANGLE = INDEX_HEAD = 0

    logAngles = pandas.DataFrame(pandas.read_csv('soudLocalizer_dumper/logAngles/data.log', sep=' ', header=None))
    logHeadState = pandas.DataFrame(pandas.read_csv('soudlocalizer_dumper/logHeadState/data.log',
                                                    sep=' ', header=None, index_col=0))
    column_names = ["audio_filename", "azimuth", "elevation",
                    "joint_0", "joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    result = pandas.DataFrame(columns=column_names)

    for file in glob.glob('audioSamples/20200512-202942/*.wav'):
        ID_AUDIO = (file.split("\\"))[1].split(".")
        ID_AUDIO = ID_AUDIO[0] + "." + ID_AUDIO[1]
        AUDIO_NAME = (ID_AUDIO.split("_"))[1].split(".")
        AUDIO_TIMESTAMP = float(AUDIO_NAME[0] + "." + AUDIO_NAME[1])
        INDEX_ANGLE = abs(logAngles[1] - AUDIO_TIMESTAMP).idxmin()
        INDEX_HEAD = abs(logHeadState[1] - logAngles.at[INDEX_ANGLE, 1]).idxmin()
        result_aux = pandas.DataFrame([[ID_AUDIO, logAngles.at[INDEX_ANGLE, 2], logAngles.at[INDEX_ANGLE, 3],
                                        logHeadState.at[INDEX_HEAD, 2], logHeadState.at[INDEX_HEAD, 3],
                                        logHeadState.at[INDEX_HEAD, 4], logHeadState.at[INDEX_HEAD, 5],
                                        logHeadState.at[INDEX_HEAD, 6], logHeadState.at[INDEX_HEAD, 7]]],
                                      columns=column_names)
        result = result.append(result_aux, ignore_index=True)

    result.to_csv('result.csv', index=False)
