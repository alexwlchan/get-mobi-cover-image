#!/usr/bin/env python
# -*- encoding: utf-8

from File import MOBIFile

import random, string
import sys

def slug():
    return "".join(random.choice(string.hexdigits) for _ in range(5))

f = MOBIFile(path=sys.argv[1])
cover = f.get_cover_image()
path = "cover-%s" % slug()
cover.save(path, format=cover.format)
print(path)
