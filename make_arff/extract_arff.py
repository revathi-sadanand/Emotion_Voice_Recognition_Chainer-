import os
import glob
import ntpath

# for f in glob.glob('/home/julie/Downloads/opensmile-2.3.0/AudioData/JK/*.wav'):
#
#     cmd='SMILExtract -C /home/julie/Downloads/opensmile-2.3.0/config/IS13_ComParE.conf -I /home/julie/Downloads/opensmile-2.3.0/AudioData/JK/*.wav -O JK.arff -instname JK  -classlabel {anger,fear,disgust,neutral,sadness,happiness,surprise}'
#     print (f)
#     os.system(cmd)


# filepath= '/home/julie/Downloads/opensmile-2.3.0/AudioData/DC/n19.wav'
#
# commandLine= 'SMILExtract -C /home/julie/Downloads/opensmile-2.3.0/config/IS13_ComParE.conf -I %s -O sal.arff -instname a01  -classlabel disgust' % filepath
# os.system(commandLine)


# fileList = os.listdir('/home/julie/Downloads/opensmile-2.3.0/AudioData/*/')

fileList = glob.glob('/home/julie/Downloads/opensmile-2.3.0/AudioData/*/*.wav')
classlable = ''

for file in fileList:
    fileName = ntpath.basename(file)
    fileNameWithoutExtension = os.path.splitext(fileName)[0]
    if fileName.startswith("a"):
        classlable = 'anger'
    elif fileName.startswith('h'):
        classlable = 'happiness'
    elif fileName.startswith('d'):
        classlable = 'disgust'
    elif fileName.startswith('sa'):
        classlable = 'sadness'
    elif fileName.startswith('su'):
        classlable = 'surprise'
    elif fileName.startswith('n'):
        classlable = 'neutral'
    else:
        classlable = 'fear'

    commandLine = 'SMILExtract -C /home/julie/Downloads/opensmile-2.3.0/config/IS13_ComParE.conf -I %s -O english.arff -instname %s  -classlabel %s' % (
        file, fileNameWithoutExtension, classlable)
    os.system(commandLine)
