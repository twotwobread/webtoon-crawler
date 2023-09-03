import os
import shutil
from pathlib import Path


def get_root_path():
    root = Path(__file__).parent.parent.parent
    return os.path.abspath(root)


def join_with_root(path):
    root_path = get_root_path()
    return os.path.join(root_path, path)


def make_directory(path, delete=False):
    if delete:
        shutil.rmtree(path, ignore_errors=True)
    os.makedirs(path, exist_ok=True)
    return path
