import time
import os

class file_handler:
    def __init__(self):
        pass

    def write(self, fname, lines):
        """
        write the given input to the given file
        """
        fname = fname + '-' + time.strftime("%Y%m%d")

        if os.path.exists(fname):
            os.remove(fname)
        with open(fname, 'a') as f:
            for d in lines:
                f.write(d+'\n')

    def writeArray(self, fname, lines_array):
        """
        write the given input to the given file
        """
        fname = fname + '-' + time.strftime("%Y%m%d")
        if os.path.exists(fname):
            os.remove(fname)
        with open(fname, 'a') as f:
            for d in lines_array:
                #d = "\t".join(d)
                d = "\t".join('{message: <40}'.format(message=item) for item in d)
                f.write(d+'\n')

    def lookup_file(self, fname):
        """
        check whether the given file exists
        """
        timestr = time.strftime("%Y%m%d")
        fname = './' + fname + '-' + timestr
        if os.path.isfile(fname):
            return True
        else:
            return False

    def read(self, fname):
        """
        read all lines from the given file
        """
        timestr = time.strftime("%Y%m%d")
        fname = './' + fname + '-' + timestr
        if os.path.isfile(fname):
            with open(fname) as f:
                # https://stackoverflow.com/questions/12330522/reading-a-file-without-newlines
                return f.read().splitlines()
        else:
            return None