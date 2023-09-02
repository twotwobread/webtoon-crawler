import os
import shutil
import sys


def get_root_path():
    root = sys.argv[0]
    root_dir = os.path.dirname(root)
    return os.path.abspath(root_dir)


def join_with_root(path):
    root_path = get_root_path()
    return os.path.join(root_path, path)


def make_directory(path, delete=False):
    if delete and os.path.exists(path):
        shutil.rmtree(path, ignore_errors=False)
    if not os.path.exists(path):
        os.makedirs(path)
    return path
