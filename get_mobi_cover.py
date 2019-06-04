#!/usr/bin/env python
# -*- encoding: utf-8

from File import MOBIFile

import sys

f = MOBIFile(path=sys.argv[1])
print(f.get_cover_image())