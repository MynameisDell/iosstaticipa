from yd_console import YDConsole
import __main__ as main
import sys
import os.path

class YDErrorHandling:

    @staticmethod
    def exit_on_usage(self):
        YDConsole.single_label_and_value('Exiting', f'Check usage \n\t\t[+] {os.path.basename(main.__file__)} [filepath]')
        sys.exit(1)

    @staticmethod
    def exit_on_usage ( arg1: str ):
        YDConsole.single_label_and_value('Exiting', f'\n\t\t[+] {arg1}')
        sys.exit(1)