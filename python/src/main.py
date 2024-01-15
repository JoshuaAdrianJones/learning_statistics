import math
import random
from typing import List

import matplotlib.pyplot as plt

from parse_data import read_csv
from stats import (
    compute_25th_percentile,
    mean,
    median,
    mode,
    quartiles,
    sample_range,
    stdev,
    variance,
)
from structures import Respondent


def numerical_values_generator(respondents: List[Respondent]) -> float:
    for respondent in respondents:
        yield respondent.numerical_value


def distance(point1: float, point2: float) -> float:
    return math.sqrt((point1 - point2) ** 2)


def k_means_clustering(data: list[float], k: int, max_iterations: int = 100):
    centroids = random.sample(data, k)
    clusters = [[] for _ in range(k)]

    for _ in range(max_iterations):
        for point in data:
            distances = [distance(point, c) for c in centroids]
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append(point)

        new_centroids = []
        for i in range(k):
            if clusters[i]:
                new_centroid = sum(clusters[i]) / len(clusters[i])
                new_centroids.append(new_centroid)
            else:
                new_centroids.append(centroids[i])

        if centroids == new_centroids:
            break
        else:
            centroids = new_centroids
            clusters = [[] for _ in range(k)]

    return clusters, centroids


def within_cluster_sum_of_squares(clusters, centroids):
    wcss = 0
    for i in range(len(clusters)):
        cluster_sum = 0
        for point in clusters[i]:
            cluster_sum += distance(point, centroids[i]) ** 2
        wcss += cluster_sum
    return wcss


if __name__ == "__main__":
    data_from_file = read_csv("data.csv")
    numbers = list(numerical_values_generator(data_from_file.respondents))
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

    data = numbers
    # Determine optimal number of clusters using WCSS
    wcss_values = []
    for k in range(1, 11):
        clusters, centroids = k_means_clustering(data, k)
        wcss = within_cluster_sum_of_squares(clusters, centroids)
        wcss_values.append(wcss)

    # Plot WCSS vs number of clusters and data vs index in the same window
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].plot(range(1, 11), wcss_values)
    axs[0].set_title("WCSS vs Number of Clusters")
    axs[0].set_xlabel("Number of Clusters")
    axs[0].set_ylabel("WCSS")

    axs[1].plot(data)
    axs[1].set_title("Data vs Index")
    axs[1].set_xlabel("Index")
    axs[1].set_ylabel("Data")

    plt.tight_layout()
    plt.show()

    # Determine number of clusters
    optimal_k = wcss_values.index(min(wcss_values)) + 1
    # optimal_k = 5
    print(f"Optimal number of clusters: {optimal_k}")

    # Cluster data
    clusters, centroids = k_means_clustering(data, optimal_k)

    # Sort data and create scatter plot with different colors for each cluster
    sorted_data = sorted(data)
    colors = [
        "r",
        "g",
        "b",
        "y",
        "m",
    ]  # Add more colors as needed
    for i in range(optimal_k):
        plt.scatter(
            [j for j in range(len(clusters[i]))],
            clusters[i],
            c=colors[i % len(colors)],
            label=f"Cluster {i+1}",
        )
    plt.plot(sorted_data, [0] * len(sorted_data), "k-", lw=3)
    plt.title("Sorted Data and Clusters")
    plt.xlabel("Index")
    plt.ylabel("Data")
    plt.legend()
    plt.show()
