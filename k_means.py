"""Numpy implementation of kmeans."""

import time

import numpy as np
from sklearn import datasets


def _initialize_clusters(features: np.ndarray, k: int) -> np.ndarray:
    num_samples, _ = np.shape(features)
    # TODO(safa): enforce unique sampling.
    return features[np.random.randint(0, num_samples, size=k), :]


def _get_closest_cluster_indices(features: np.ndarray,
                                 clusters: np.ndarray) -> np.ndarray:
    num_features, _ = features.shape
    k, _ = clusters.shape
    features = np.repeat(
        np.expand_dims(features, 0), repeats=k, axis=0)
    clusters = np.repeat(
        np.expand_dims(clusters, 1), repeats=num_features, axis=1)
    distances = np.sum(((features - clusters) ** 2), -1) ** 0.5
    return np.argmin(distances, axis=0)  # [num_features, k]


def _get_features_for_given_cluster(features, cluster_indices, i):
    if i > np.max(cluster_indices):
        raise ValueError(f'i={i} should not be larger than '
                         f'np.max(cluster_indices)={np.max(cluster_indices)}.')
    return features[cluster_indices == i]


def _update_clusters(cluster_indices: np.ndarray,
                     features: np.ndarray, k: int) -> np.ndarray:
    clusters = np.zeros((k, features.shape[1]))

    # TODO(safa): vectorize.
    for i in range(k):
        features_i = _get_features_for_given_cluster(
            features, cluster_indices, i)
        clusters[i] = np.mean(features_i, axis=0)
    return clusters


def run_kmeans(features: np.ndarray,
               k: int,
               max_iter: int = 500,
               plot_period: int = 100,
               ):
    num_samples, feat_len = np.shape(features)
    if num_samples < k:
        raise ValueError(
            f'num_samples={num_samples} should not be smaller than k={k}.')

    print(f'num_samples = {num_samples}')
    print(f'feat_len = {feat_len}')

    previous_clusters = _initialize_clusters(features, k)

    for i in range(max_iter):
        cluster_indices = _get_closest_cluster_indices(
            clusters=previous_clusters, features=features)
        clusters = _update_clusters(
            cluster_indices=cluster_indices, features=features, k=k)
        print(f'pre={previous_clusters}')
        print(f'clusters={clusters}')
        diff = np.min(np.abs(previous_clusters - clusters))
        import copy
        previous_clusters = copy.deepcopy(clusters)
        print(f'diff={diff : .2f}')
        if np.min(diff) < 1e-3:
            return clusters

        if i % plot_period == 0:
            # TODO(safa): plot here.
            pass

    return clusters


if __name__ == '__main__':
    x, y = datasets.make_blobs()
    st_time = time.time()
    y_preds = run_kmeans(features=x, k=3)
    print(f'Time it took = {time.time()-st_time : .2f}')
