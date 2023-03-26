import csv

from structures import Respondent, Respondents


def read_csv(filename: str) -> Respondents:
    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        read_in: list[Respondent] = []
        for row in reader:
            respondent = Respondent(row[0], float(row[1]))
            read_in.append(respondent)
        return Respondents(read_in)
