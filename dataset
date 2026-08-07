import numpy as np
import pandas as pd
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
def create_dataset(size = 2000):
    t1_values = np.random.uniform(0, 2, size)
    t2_values = np.random.uniform(0, 2, size)
    labels = np.zeros(size)
    for i in range(size):
        labels[i] = round(winding_number(t1_values[i], t2_values[i]))
    df = pd.DataFrame({"t1": t1_values, "t2": t2_values, "label": labels})
    return df
df = create_dataset()
df.to_csv('ssh_dataset.csv', index=False)
plt.scatter(df['t1'], df['t2'], c=df['label'], cmap='coolwarm', s=8)
plt.colorbar(label='label')
plt.xlabel('t1')
plt.ylabel('t2')
plt.title('2000 samples labeled by winding number')
plt.savefig('dataset_scatter.png', dpi=150)
