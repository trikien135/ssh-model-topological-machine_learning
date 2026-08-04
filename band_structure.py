"""SSH model — Bloch Hamiltonian and band structure"""
import numpy as np
import matplotlib.pyplot as plt
"""2x2 Bloch Hamiltonian matrix"""
def H_k (t1, t2, k):
    f_k = t1+t2*np.exp(-1j*k)
    H = np.array([
                 [0, f_k],
                 [np.conj(f_k), 0]
    ])
    return H
def band_structure(t1, t2, num_k = 200):
    """spread k accross -pi to pi"""
    k_values = np.linspace(-np.pi, np.pi, num_k)
    energies = np.zeros((num_k, 2))
    """np.linalg.eigvalsh: take all values of H and sort from low to high"""
    for i, k in enumerate(k_values):
        H = H_k(t1, t2, k)
        eigvals = np.linalg.eigvalsh(H)
        energies[i, :] = eigvals
    return k_values, energies
def plot_bands(t1, t2, label, ax):
    k_values, energies = band_structure(t1, t2)
    ax.plot(k_values, energies[:, 0], label="E_-(k)", color="tab:blue")
    ax.plot(k_values, energies[:, 1], label="E_+(k)", color="tab:red")
    ax.axhline(0, color="gray", linewidth=0.7, linestyle="--")
    ax.set_title(f"{label}\n(t1={t1}, t2={t2})")
    ax.set_xlabel("k")
    ax.set_ylabel("Energy")
    ax.legend()
def gap_size(t1, t2, num_k=400):
    """Minimum energy gap between the two bands, over all k."""
    _, energies = band_structure(t1, t2, num_k)
    gap = energies[:, 1] - energies[:, 0]
    return np.min(gap)
if __name__ == "__main__":
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    plot_bands(1.5, 0.5, label = "Trivial t1 > t2", ax = axes[0])
    plot_bands(0.5, 1.5, label = "Topologica t2 > t1", ax = axes[1])
    plt.tight_layout()
    plt.savefig("ssh_band_structure.png", dpi=150)
    # Confirm the gap closes exactly at the transition point t1 = t2
    for t1, t2 in [(1.5, 0.5), (1.0, 1.0), (0.5, 1.5)]:
        g = gap_size(t1, t2)
        print(f"  t1={t1}, t2={t2}  ->  minimum gap = {g:.4f}")
