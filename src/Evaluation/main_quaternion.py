# System (Default)
import sys
# Platform (Platform identification data)
import platform
# System (Default)
import sys
if platform.system() == 'Windows':
    # Windows Path.
    sys.path.append('..')
else:
    # Linux / macOS Path.
    sys.path.append('..') 
# Custom Library:
#   ../Lib/Transformation
import Lib.Transformation as Transformation

def main():
    """
    Description:
        ...
    """
    
    pass

if __name__ == '__main__':
    sys.exit(main())