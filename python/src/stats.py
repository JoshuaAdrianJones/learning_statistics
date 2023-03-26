import random


def mean(data: list[float]) -> float:
    return sum(data) / len(data)


def median(data: list[float]) -> float:
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return sorted_data[n // 2]


def mode(data: list[float]) -> float:
    freq = {}
    for value in data:
        freq[value] = freq.get(value, 0) + 1
    mode_value = max(freq, key=freq.get)
    return mode_value


def sample_range(data: list[float]) -> float:
    return max(data) - min(data)


def variance(data: list[float]) -> float:
    n = len(data)
    mean_val = mean(data)
    return sum((x - mean_val) ** 2 for x in data) / (n - 1)


def stdev(data: list[float]) -> float:
    return variance(data) ** 0.5


def k_means(data: list[float], k: int) -> list[list[float]]:
    centroids = random.sample(data, k)
    while True:
        clusters = [[] for _ in range(k)]
        for value in data:
            distances = [abs(value - c) for c in centroids]
            clusters[distances.index(min(distances))].append(value)
        new_centroids = [mean(cluster) for cluster in clusters]
        if new_centroids == centroids:
            break
        centroids = new_centroids
    return clusters


def find_median(data: list[float]) -> float:  # finds the median of a sorted_list
    number_of_data = len(data)
    data = sorted(data)
    if number_of_data % 2 == 0:
        median = (data[(number_of_data // 2)] + data[(number_of_data // 2 - 1)]) / 2
    else:
        median = data[(number_of_data // 2)]
    return median


def lower_quartile(data: list[float]) -> float:  # finds the median of a sorted_list
    middle = len(data) // 2
    data = sorted(data)[:middle]
    number_of_data = len(data)
    if number_of_data % 2 == 0:
        q1 = (data[(number_of_data // 2)] + data[(number_of_data // 2 - 1)]) / 2
    else:
        q1 = data[(number_of_data // 2)]
    return q1


def upper_quartile(data: list[float]) -> float:  # finds the median of a sorted_list
    middle = len(data) // 2
    data = sorted(data)[middle:]
    number_of_data = len(data)
    if number_of_data % 2 == 0:
        q3 = (data[(number_of_data // 2)] + data[(number_of_data // 2 - 1)]) / 2
    else:
        q3 = data[(number_of_data // 2)]
    return q3


def quartiles(data: list[float]) -> dict[str, float]:
    q1 = lower_quartile(data)
    q2 = find_median(data)
    q3 = upper_quartile(data)
    return {"q1": q1, "q2": q2, "q3": q3}


def compute_25th_percentile(data: list[float]) -> float:
    """
    Computes the 25th percentile of a list of numerical values.

    Parameters:
        data (list): A list of numerical values.

    Returns:
        The 25th percentile of the input data.
    """
    data = sorted(data)
    n = len(data)
    index = int(n * 0.25)
    if n % 4 == 0:
        result = (data[index - 1] + data[index]) / 2
    else:
        result = data[index]
    return result


def calculate_iqr(data: list[float]) -> float:
    q1, q3 = lower_quartile(data), upper_quartile(data)
    return q3 - q1


def find_outliers(data: list[float]) -> list[float]:
    iqr = calculate_iqr(data)
    q1 = lower_quartile(data)
    q3 = upper_quartile(data)
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    outliers = [x for x in data if x < lower_bound or x > upper_bound]
    return outliers
