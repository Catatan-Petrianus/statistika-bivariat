import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from scipy.stats import linregress

# Configure page layout
st.set_page_config(page_title="Koefisien Determinasi")
st.title("Koefisien Determinasi")
st.sidebar.success("Pilih materi di atas.")


s_strong = random.uniform(0.5, 1)
s_moderate = random.uniform(2, 2.3)
s_weak = random.uniform(3.5, 4)

# Function to generate data with different correlations
def generate_data(correlation_type, size=100):
    # np.random.seed(42)
    x = np.random.rand(size) * 10 
    if correlation_type == 'Positif kuat':
        y = 2 +x + np.random.normal(0, s_strong, size)
    elif correlation_type == 'Positif sedang':
        y = 4 + x + np.random.normal(0, s_moderate, size)
    elif correlation_type == 'Positif lemah':
        y = 8 + x + np.random.normal(0, s_weak , size)
    elif correlation_type == 'Negatif kuat':
        y = 12 - x - np.random.normal(0, s_strong, size)
    elif correlation_type == 'Negatif sedang':
        y = 14 - x - np.random.normal(0, s_moderate, size)
    elif correlation_type == 'Negatif lemah':
        y = 18 - x - np.random.normal(0, s_weak , size)
    elif correlation_type == 'Tidak berkorelasi':
        y = np.random.rand(size)*10
    else:
        y = np.random.rand(size)*10
    #y = np.abs(y)  # Ensure non-negative values
    return x, y


# Sidebar options
correlation_type = st.selectbox(
    "Pilih jenis korelasi",
    ["Positif kuat", "Positif sedang", "Positif lemah", 
     "Negatif kuat", "Negatif sedang", "Negatif lemah", 
     "Tidak berkorelasi"]
)


# Generate data
x, y = generate_data(correlation_type)

# Calculate correlation coefficient
r_value = np.corrcoef(x, y)[0, 1]

# Plotting
fig, ax = plt.subplots()
ax.scatter(x, y, label=f'{correlation_type}', alpha=0.6)
ax.set_xlabel('X')
ax.set_ylabel('Y')
if (correlation_type == 'Tidak berkorelasi') :
    r_squared = 0
else:
    r_squared = (r_value)*(r_value)
ax.set_title(f"Koefisien determinasi ($r^2$) = {r_squared:.5f}")

# Display plot
st.pyplot(fig)

