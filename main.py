import os 
os.system('python setup.py')

import vidfile,videoprocess

vid = vidfile.select_file()
videoprocess.vidprocess(vid)







