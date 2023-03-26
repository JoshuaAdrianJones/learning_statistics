from dataclasses import dataclass
from typing import List


@dataclass
class Respondent:
    respondent_id: str
    numerical_value: float


@dataclass
class Respondents:
    respondents: List[Respondent]
