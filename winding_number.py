import numpy as np
import matplotlib.pyplot as plt

def d_vector(t1, t2, k):
    d_x = t1+t2*np.cos(k)
    d_y = t2*np.sin(k)
    return d_x, d_y
def winding(t1, t2, num_k=200):
    """spread k accross -pi to pi"""
    k_values = np.linspace(-np.pi, np.pi, num_k)
    d_x_values = np.zeros(num_k)
    d_y_values = np.zeros(num_k)
    for i, k in enumerate(k_values):
        d_x_values[i], d_y_values[i] = d_vector(t1, t2, k)
    return d_x_values, d_y_values
def winding_number(t1, t2, num_k=200):
    """
    Compute the winding number: total accumulated angle change of (d_x, d_y)
    around the origin, divided by 2*pi. Should come out to (near) 0 or 1.
    """
    dx, dy = winding(t1, t2, num_k)
    theta = np.arctan2(dy, dx)           # angle at each point, range (-pi, pi]
    theta_unwrapped = np.unwrap(theta)   # fixes the artificial -pi/pi jump
    total_change = theta_unwrapped[-1] - theta_unwrapped[0]
    return total_change / (2 * np.pi)
def plot_loop(t1, t2, label, ax):
    dx, dy = winding(t1, t2)
    ax.plot(dx, dy)
    ax.scatter(0, 0, color="red")
    ax.set_aspect("equal")
    ax.set_xlabel("d_x")
    ax.set_ylabel("d_y")
    W = winding_number(t1, t2)
    ax.set_title(f"{label}\n(t1={t1}, t2={t2}), W = {W:.2f}")
if __name__ == "__main__":
    fig, axes = plt.subplots(1, 2, figsize=(11, 5))
    plot_loop(1.5, 0.5, "Trivial (t1 > t2)", axes[0])
    plot_loop(0.5, 1.5, "Topological (t1 < t2)", axes[1])
    plt.tight_layout()
    plt.savefig("winding_loops.png", dpi=150)
    print("Saved plot to winding_loops.png")
    print("\nWinding numbers:")
    for t1, t2 in [(1.5, 0.5), (1.0, 1.0), (0.5, 1.5)]:
        print(f"  t1={t1}, t2={t2}  ->  W = {winding_number(t1, t2):.4f}")
