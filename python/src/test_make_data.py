import csv
import os

import pytest

from make_data import generate_csv
from structures import Respondent, Respondents


@pytest.fixture
def data() -> Respondents:
    read_in = []
    for i in range(10):
        respondent = Respondent(str(i), i * 100)
        read_in.append(respondent)
    return Respondents(read_in)


def test_generate_csv():
    filename = "test_data.csv"
    num_rows = 10
    generate_csv(filename, num_rows)
    assert os.path.isfile(filename)

    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)
        assert header == ["respondent", "numerical_value"]

        rows = [row for row in reader]
        assert len(rows) == 10

    os.remove(filename)


def test_read_csv(data: Respondents):
    respondents = data
    assert isinstance(respondents, Respondents)
    assert len(respondents.respondents) == 10

    for i, respondent in enumerate(respondents.respondents):
        assert respondent.respondent_id == str(i)
        assert respondent.numerical_value == i * 100
