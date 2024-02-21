#!/usr/bin/env python

from yd_console import YDConsole
from yd_radare2 import CheckBinary
from yd_file_ext_search import YDFileExtensionSearch, YDDepth
from yd_start_helper import YDStartUpParameters
from yd_version import YDVersion
from yd_jtool import YDjtool

if __name__ == '__main__':
    YDConsole.banner('script started')
    YDConsole.single_value_subheading(YDVersion.string())
    b = YDStartUpParameters()
    YDConsole.single_value_subheading('Script executing ' + b.main_file)
    YDConsole.single_value_subheading('Path ' + b.path)
    a = YDFileExtensionSearch(b.path, YDDepth.LIGHT)
#    CheckBinary(a.exec_path)

    c = YDjtool()