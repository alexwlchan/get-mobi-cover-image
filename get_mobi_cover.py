#!/usr/bin/env python
# -*- encoding: utf-8

import imghdr
import random
import string
import sys

from File import MOBIFile


def slug():
    return "".join(random.choice(string.hexdigits) for _ in range(5))


if __name__ == "__main__":

    try:
        path = sys.argv[1]
    except IndexError:
        sys.exit("Usage: %s <PATH_TO_MOBI>" % __file__)

    mobi_file = MOBIFile(path=sys.argv[1])
    cover_data = mobi_file.get_cover_image()

    img_format = imghdr.what(None, h=cover_data)

    path = "cover-%s.%s" % (slug(), img_format)
    open(path, "wb").write(cover_data)
    print(path)
