from typing import List

from parse_data import read_csv
from stats import (
    compute_25th_percentile,
    k_means,
    mean,
    median,
    mode,
    quartiles,
    sample_range,
    stdev,
    variance,
)
from structures import Respondent


def numerical_values_generator(respondents: List[Respondent]):
    for respondent in respondents:
        yield respondent.numerical_value


if __name__ == "__main__":
    data = read_csv("data.csv")
    numbers = list(numerical_values_generator(data.respondents))
    print(numbers)

    analysis_types = [
        mean,
        median,
        mode,
        sample_range,
        variance,
        stdev,
        quartiles,
        compute_25th_percentile,
    ]
    for analysis_type in analysis_types:
        print(f"{analysis_type.__name__} : {analysis_type(numbers)}")


# Correlation and regression analysis and kmeans clustering

# Hypothesis testing
