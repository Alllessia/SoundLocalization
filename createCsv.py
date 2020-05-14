if __name__ == '__main__':
    import pandas
    import glob

    logAngles = pandas.DataFrame(pandas.read_csv('soudLocalizer_dumper/logAngles/data.log', sep=' ', header=None))
    logHeadState = pandas.DataFrame(pandas.read_csv('soudlocalizer_dumper/logHeadState/data.log',
                                                    sep=' ', header=None, index_col=0))
    column_names = ["audio_filename", "azimuth", "elevation",
                    "joint_0", "joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    result = pandas.DataFrame(columns=column_names)

    for file in glob.glob('audioSamples/20200512-202942/*.wav'):
        path = file.split("\\")
        id_audio = path[1].split(".")
        id_audio = id_audio[0] + "." + id_audio[1]
        audio_name = file.split("_")
        audio_name = audio_name[1].split(".")
        audio_timestamp = float(audio_name[0] + "." + audio_name[1])
        indexAngles = abs(logAngles[1] - audio_timestamp).idxmin()
        indexHead = abs(logHeadState[1] - logAngles.at[indexAngles, 1]).idxmin()
        result_aux = pandas.DataFrame([[id_audio, logAngles.at[indexAngles, 2], logAngles.at[indexAngles, 3],
                                        logHeadState.at[indexHead, 2], logHeadState.at[indexHead, 3],
                                        logHeadState.at[indexHead, 4], logHeadState.at[indexHead, 5],
                                        logHeadState.at[indexHead, 6], logHeadState.at[indexHead, 7]]],
                                      columns=column_names)
        result = result.append(result_aux, ignore_index=True)

    result.to_csv('result.csv', index=False)
