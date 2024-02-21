class YDConsole:

    @staticmethod
    def single_value ( arg1: str):
        print('[+]' + str(arg1))

    @staticmethod
    def single_value_subheading ( arg1: str):
        print('\t' + str(arg1))

    @staticmethod
    def single_label_and_value (arg0: str, arg1: str):
        print('\t' + arg0 + ': ' + arg1)

    @staticmethod
    def banner(arg1: str):
        print('\n[-]' + ('*' * 10) + ' ' + arg1 + ' ' + ('*' * 10) + '[-]')

    @staticmethod
    def single_list(arg1: list):
        print(arg1)
        for i in arg1:
            print('[+]' + i)