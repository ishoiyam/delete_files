import os
import fnmatch

for path, dirs, files in os.walk("."):
    for f in fnmatch.filter(files, "*.vtt"):
        fullname = os.path.abspath(os.path.join(path, f))
        os.remove(fullname)

    for f in fnmatch.filter(files, "*.srt"):
        fullname2 = os.path.abspath(os.path.join(path, f))
        os.remove(fullname2)

        
