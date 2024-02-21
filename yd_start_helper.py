import os.path
from yd_error_handling import YDErrorHandling
import __main__ as main
import sys
import os.path

class YDStartUpParameters:

    main_file = os.path.basename(main.__file__)
    path = sys.argv[1]
    count = len(sys.argv[1:])

    def __init__ (self):
        self.validate_count()
        self.validate_path()

    def validate_count ( self ):
        if self.count != 1:
            YDErrorHandling.exit_on_usage(self)

    def validate_path(self):
        if os.path.isdir(self.path) == False:
            YDErrorHandling.exit_on_usage('cannot find' + self.path)