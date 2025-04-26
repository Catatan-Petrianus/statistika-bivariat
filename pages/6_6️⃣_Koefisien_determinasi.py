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

# Sidebar options
correlation_type = st.selectbox(
    "Pilih jenis korelasi",
    ["Positif kuat", "Positif sedang", "Positif lemah", 
     "Negatif kuat", "Negatif sedang", "Negatif lemah", 
     "Tidak berkorelasi"]
)


# Function to generate data with different correlations
def generate_data(correlation_type, size=100):
    while True:
        x = np.random.rand(size) * 10 
        s_strong = random.uniform(0.5, 1)
        s_moderate = random.uniform(2, 2.3)
        s_weak = random.uniform(3.75, 4)

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
        
        # Calculate r_squared
        if correlation_type == 'Tidak berkorelasi':
            r_squared = 0
        else:
            slope, intercept, r_value, p_value, std_err = linregress(x, y)
            r_squared = r_value ** 2

        # Check conditions
        if correlation_type in ['Positif kuat', 'Negatif kuat'] and r_squared > 0.75:
            return x, y, r_squared
        elif correlation_type in ['Positif sedang', 'Negatif sedang'] and 0.5 < r_squared <= 0.75:
            return x, y, r_squared
        elif correlation_type in ['Positif lemah', 'Negatif lemah'] and r_squared <= 0.5:
            return x, y, r_squared
        elif correlation_type == 'Tidak berkorelasi':
            return x, y, r_squared





# Generate data
x, y, r_squared= generate_data(correlation_type)

# Plotting
fig, ax = plt.subplots()
ax.scatter(x, y, label=f'{correlation_type}', alpha=0.6)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title(f"Koefisien determinasi ($r^2$) = {r_squared:.5f}")

# Display plot
st.pyplot(fig)

