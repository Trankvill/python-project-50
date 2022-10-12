from gendiff.formatters.json import format_json
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.formats import JSON, STYLISH


def format_diff(diff, formatter):
    if formatter == STYLISH:
        return format_stylish(diff)
    if formatter == JSON:
        return format_json(diff)
