#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special


import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise

"""


def cp_to_dir(p_file_n, todir):
    if os.path.exists(todir):
        pass
    else:
        os.mkdir(todir)

    shutil.copy(p_file_n, todir)


def search_file_to_zip(this_script, args, tozip):
    files_to_zip = []
    for rest_of_args in args:
        if os.path.isdir(rest_of_args):
            for name in get_special_paths(this_script, rest_of_args):
                files_to_zip.append(name)
        elif os.path.isfile(rest_of_args):
            files_to_zip.append(rest_of_args)

    do_zip_file(files_to_zip, tozip)


def do_zip_file(file_to_zip, tozip):
    #for f in file_to_zip:
    zip_cmd = ["zip", "-j", tozip,] + file_to_zip
    run_zip = subprocess.Popen(zip_cmd, stdout=subprocess.PIPE)
    output = run_zip.communicate()[0]
    print(output.decode())
    #if 'error' in output.decode():
    #     break


def get_special_paths(this_script, dir_ch):
    if os.path.isdir(dir_ch):
        path_to_files = os.path.abspath(dir_ch)
        #for root, _, special_file in os.listdir(dir_ch):
        for f in os.listdir(dir_ch):
            #for f in special_file:
            if f not in this_script:
                yield os.path.join(path_to_files, f)


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    this_script = sys.argv[0]
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    # todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]
        for name in get_special_paths(this_script, args[0]):
            cp_to_dir(name, todir)
    # tozip = ''
    elif args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]
        search_file_to_zip(this_script, args, tozip)
    else:
        for name in get_special_paths(this_script, args[0]):
            print(name)

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)


if __name__ == "__main__":
    main()
