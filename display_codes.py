import matplotlib.pyplot as plt
import numpy as np
import os

def display(dataset_name, similarity_measure, true_eigvals, dataset_size, search_rank, \
            sample_eigenvalues_scaled, sample_eigenvalues_scaled_std, max_samples):
    true_eigvals.sort()
    true_min_eig = true_eigvals[search_rank]

    x_axis = np.array(list(range(10, max_samples, 10))) / dataset_size
    true_min_eig_vec = true_min_eig*np.ones_like(x_axis)

    estimate_min_eig_vec = np.array(sample_eigenvalues_scaled)
    estimate_std = np.array(sample_eigenvalues_scaled_std)

    plt.plot(x_axis, true_min_eig_vec, label="True", alpha=0.7)
    plt.plot(x_axis, estimate_min_eig_vec, label="Scaled estimate", alpha=0.7)
    plt.fill_between(x_axis, estimate_min_eig_vec-estimate_std, estimate_min_eig_vec+estimate_std, alpha=0.3)
    plt.xlabel("Proportion of dataset chosen as landmark samples")
    plt.ylabel("Eigenvalue estimates")
    plt.legend(loc="upper right")
    plt.title(similarity_measure+": "+str(search_rank)+"th eigenvalue")
    filename = "./figures/dataset_name/eigenvalues/"
    if not os.path.isdir(filename):
        os.makedirs(filename)
    filename = filename+similarity_measure+"_"+str(search_rank)+".pdf"
    plt.savefig(filename)
    return None


def display_precomputed_error(dataset_name, similarity_measure, error, error_std, dataset_size, \
                              search_rank, max_samples):
    x_axis = np.array(list(range(10, max_samples, 10))) / dataset_size
    plt.plot(x_axis, error, label="log of squared error", alpha=0.7)
    plt.fill_between(x_axis, error-error_std, error+error_std, alpha=0.3)
    plt.xlabel("Proportion of dataset chosen as landmark samples")
    plt.ylabel("Error of eigenvalue estimates")
    plt.legend(loc="upper right")
    plt.title(similarity_measure+": "+str(search_rank)+"th eigenvalue")
    filename = "./figures/dataset_name/errors/"
    if not os.path.isdir(filename):
        os.makedirs(filename)
    filename = filename+similarity_measure+"_"+str(search_rank)+".pdf"
    plt.savefig(filename)
    return None
