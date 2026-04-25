import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import linregress

# Configure page layout
st.set_page_config(page_title="Koefisien Determinasi")
st.title("Koefisien Determinasi")
st.sidebar.success("Pilih materi di atas.")

# Sidebar options
correlation_type = st.selectbox(
    "Pilih jenis korelasi",
    [
        "Positif sempurna",
        "Positif sangat kuat", "Positif kuat", "Positif sedang", "Positif lemah", "Positif sangat lemah",
        "Negatif kuat", "Negatif sedang", "Negatif lemah",
        "Tidak berkorelasi"
    ]
)

# ----------------------------
# Generate data (FIXED VERSION)
# ----------------------------
def generate_data(correlation_type, size=100):
    x = np.random.rand(size) * 10

    noise_map = {
        "Positif sempurna": 0,
        "Positif sangat kuat": 0.3,
        "Positif kuat": 0.8,
        "Positif sedang": 1.5,
        "Positif lemah": 2.5,
        "Positif sangat lemah": 3.5,
        "Negatif kuat": 0.8,
        "Negatif sedang": 1.5,
        "Negatif lemah": 2.5,
        "Tidak berkorelasi": 5.0
    }

    noise = noise_map.get(correlation_type, 1)

    if correlation_type == "Positif sempurna":
        y = x * 1.5
    elif "Positif" in correlation_type:
        y = 2 + x + np.random.normal(0, noise, size)
    elif "Negatif" in correlation_type:
        y = 20 - x + np.random.normal(0, noise, size)
    else:
        y = np.random.rand(size) * 10

    # r^2
    if correlation_type == "Tidak berkorelasi":
        r_squared = 0
    else:
        slope, intercept, r_value, p_value, std_err = linregress(x, y)
        r_squared = r_value ** 2

    return x, y, r_squared


# Generate data
x, y, r_squared = generate_data(correlation_type)

# Plot
fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.6)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title(f"Koefisien determinasi (r²) = {r_squared:.5f}")

st.pyplot(fig)

# Display value
st.markdown(f"### Nilai r² = {r_squared:.5f}")
