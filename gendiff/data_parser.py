#!/usr/bin/env python

import json


def parse(data, format_):
    if format_ == 'json':
        return json.loads(data)
