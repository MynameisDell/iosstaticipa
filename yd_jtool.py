import shutil
from yd_console import YDConsole

class YDjtool:
    filename = 'jtool'

    def __init__(self):
        self.exists()

    def exists ( self ):
        if (shutil.which(self.filename) is not None) == True:
            print("exists")
        else:
            print(f"does not exist / problem finding {self.filename}")