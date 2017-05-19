#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request
from pathlib import Path

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    hostname = filename

    with open(filename, 'r') as logfile:
        path_to_jpg = logfile.read()

    # /edu/languages/google-python-class/images/puzzle/a-babf.jpg animal
    # /edu/languages/google-python-class/images/puzzle/p-bjhh-bbdh.jpg place
    regex = re.compile(r'/edu/languages/google-python-class/images/puzzle/\w-\w{4}-{0,1}\w{0,4}.jpg')
    url = list(set(re.findall(regex, path_to_jpg)))
    url.sort()
    full_url =[]
    filename = re.sub(r'/.*/', '',filename)
    for path in url:
        full_url.append('http://code.google.com' + path)

    return full_url
    # +++your code here+++


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    img_dir = Path(dest_dir)
    if img_dir.exists():
        pass
    else:
        os.mkdir(dest_dir)
    x = 0
    img_file = dest_dir + '/img'
    for url in img_urls:
        chck_file = Path(img_file + str(x))
        if chck_file.is_file():
            pass
        else:
            urllib.request.urlretrieve(url, img_file + str(x))
        x += 1

    # create a index.html file and put <img src=>
    # inside the created dir above


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
