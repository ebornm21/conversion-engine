#A simple program illustrating an imported library.

import sys

from Libraries.sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])