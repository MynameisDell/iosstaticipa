
class YDVersion:

    major = 0
    minor = 0
    patch = 1

    @staticmethod
    def string():
        return f'Version \t{YDVersion.major}-{YDVersion.minor}-{YDVersion.patch}'