#!/usr/bin/env python
import os


def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def get_format(filepath):
    root, ext = os.path.splitext(filepath)
    if ext == '.yaml' or ext == '.yml':
        return 'yaml'
    elif ext == '.json':
        return 'json'
