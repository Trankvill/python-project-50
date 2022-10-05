from gendiff.formatters.json import format_json
from gendiff.formatters.formats import JSON


def format_diff(diff, formatter):
    if formatter == JSON:
        return format_json(diff)
