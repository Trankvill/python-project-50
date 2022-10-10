import pytest
from gendiff.gendiff import generate_diff
from gendiff.file_reader import read_file
from gendiff.formatters.formats import JSON


FLAT_JSON_FILE1 = 'tests/fixtures/file1.json'
FLAT_JSON_FILE2 = 'tests/fixtures/file2.json'

ANSWER_JSON_FLAT = 'tests/fixtures/answer_json_flat'


def get_answer(answer_path):
    return read_file(answer_path)


@pytest.mark.parametrize('filepath1, filepath2, format_name, answer', [
    (FLAT_JSON_FILE1, FLAT_JSON_FILE2, JSON, ANSWER_JSON_FLAT),
])
def test_generate_diff(filepath1, filepath2, format_name, answer):
    assert generate_diff(filepath1, filepath2, format_name) == get_answer(answer)
