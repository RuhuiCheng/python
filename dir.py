import os

ls = os.listdir('/home/crh/free-space')
print(len(ls))

bl = os.path.exists('/home/crh/free-space/demo.txt')
print(bl)

filepath, tmpfilename = os.path.split(wav_file)
