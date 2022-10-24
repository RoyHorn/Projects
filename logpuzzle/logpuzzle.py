#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import sys
import re
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename: str):
    """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
    # +++your code here+++
    urls_list = []
    with open(filename, 'r') as f:
        for line in f:
            if '/puzzle/' in line:
                path = re.search(r"GET (.*) HTTP", line).group(1)
                name = re.search(r"_(.*)", filename).group(1)
                url = f'http://{name}{path}'

                # checking whether the url is in the list or not, if not adding it
                if url not in urls_list:
                    urls_list.append(url)
        # a really nice way sorting the list according to -sorting-word.jpg
        return sorted(urls_list, key=lambda txt: re.search(r"-(.*).jpg", txt).group(1))


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directoryn
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
    # +++your code here+++

    # creating a new directory
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    # creating index.html in the direcotory created, downloading this pictures and embedding them inside of the html file
    with open(os.path.join(dest_dir, 'index.html'), 'w') as f:
        i = 1
        f.write('<html><body>\n')
        for img_url in img_urls:
            urllib.request.urlretrieve(img_url, os.path.join(dest_dir, f"img{i}.jpg"))
            print(f'downloaded img {i}')
            f.write(f'<img src="img{i}.jpg">')
            i += 1
        f.write('</body></html>')


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
