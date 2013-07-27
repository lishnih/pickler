#!/usr/bin/env python
# coding=utf-8
# Stan 2013-07-26

from __future__ import ( division, absolute_import,
                         print_function, unicode_literals )

import os, pickle, fnmatch, logging

try:
    from .lib.backwardcompat import *
    from .lib.dump import *
    from .lib.tkprop import propertyDialog, rootDialog
except:
    from lib.backwardcompat import *
    from lib.dump import *
    from lib.tkprop import propertyDialog, rootDialog


def load_entry(filename):
    entry = {}
    if os.path.exists(filename):
        if os.path.isfile(filename):
            with open(filename, 'rb') as f:
                try:
                    entry = pickle.load(f)
                except Exception as e:
                    logging.error("Unable read/parse file: {0} [{1}]".format(filename, e))
        else:
            logging.error("{0} must be a file!".format(filename))
    return entry


def main(args=None):
    s = {}
    nogui = False

    if args:
        filename = args.file
        nogui = args.nogui

        if filename:
            s = load_entry(filename)

    if nogui:
        print(plain(s))
    else:
        root = rootDialog(s)
        root.update_idletasks()
        root.minsize(root.winfo_reqwidth(), root.winfo_reqheight())
        root.mainloop()


if __name__ == '__main__':
    import sys, argparse

    parser = argparse.ArgumentParser(description='Simple tool for view file.pickle')
    parser.add_argument('file', nargs='?',
                        help='file to view')
    parser.add_argument('--nogui', action='store_true',
                        help='no gui')

    if sys.version_info >= (3,):
        argv = sys.argv
    else:
        fse = sys.getfilesystemencoding()
        argv = [i.decode(fse) for i in sys.argv]

    args = parser.parse_args(argv[1:])

    sys.exit(main(args))
