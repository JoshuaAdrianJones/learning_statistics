import csv
import random
import uuid


def generate_csv(filename: str, num_rows: int) -> None:
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["respondent", "numerical_value"])
        for _ in range(num_rows):
            writer.writerow([str(uuid.uuid4()), random.randint(0, 1000)])


if __name__ == "__main__":
    generate_csv("data.csv", 1000)
