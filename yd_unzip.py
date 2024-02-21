from pathlib import Path
import os.path

class Unzipper:

    def __init__ ( self, path, filename ):
        self.filename = filename
        self.user_entered_path = path

    #    self.cwd_path = self.santized_path

    # @property
    # def santized_path ( self ):
    #     if not self.path:
    #         return (os.getcwd())
    #     else:
    #         return (self.path)

    def UnzipFile ():
        target = TargetIpa()
        # target.path, target.filename = Parameters()
        # full_path = os.path.join(target_to_unzip.santized_path, target_to_unzip.filename)
        # zipped_file = Path(full_path)
        # print("[+] Checking file at path: " + full_path)

        try:
            result = zipped_file.exists()
        except FileNotFoundError:
            print("file not found")
        else:
            print("[+] file exist check: " + str(result))