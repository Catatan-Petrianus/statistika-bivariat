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
    ["Positif sempurna",
     "Positif sangat kuat", "Positif kuat", "Positif sedang", "Positif lemah", "Positif sangat lemah",
     "Negatif kuat", "Negatif sedang", "Negatif lemah", 
     "Tidak berkorelasi"]
)


# Function to generate data with different correlations
def generate_data(correlation_type, size=100):
    while True:
        x = np.random.rand(size) * 10 
        s_perfect = random.uniform(1, 1)
        s_very_strong = random.uniform(0.91, 0.99)
        s_strong = random.uniform(0.5, 0.9)
        s_moderate = random.uniform(2, 2.3)
        s_weak = random.uniform(3.75, 4)
        s_very_weak = random.uniform(4.1, 5)

        if correlation_type == 'Positif sempurna':
            y = x + np.random.normal(0, s_perfect, size)
        elif correlation_type == 'Positif sangat kuat':
            y = x + np.random.normal(0, s_very_strong, size)
        elif correlation_type == 'Positif kuat':
            y = 2 +x + np.random.normal(0, s_strong, size)
        elif correlation_type == 'Positif sedang':
            y = 4 + x + np.random.normal(0, s_moderate, size)
        elif correlation_type == 'Positif lemah':
            y = 8 + x + np.random.normal(0, s_weak , size)
        elif correlation_type == 'Positif sangat lemah':
            y = 10 + x + np.random.normal(0, s_very_weak , size)
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
        if correlation_type in ['Positif sempurna'] and r_squared = 1:
            return x, y, r_squared
        elif correlation_type in ['Positif sangat kuat'] and 0.0.9 <= r_squared < 1:
            return x, y, r_squared
        elif correlation_type in ['Positif kuat', 'Negatif kuat'] and 0.75 <= r_squared < 0.9:
            return x, y, r_squared
        elif correlation_type in ['Positif sedang', 'Negatif sedang'] and 0.5 <= r_squared < 0.75:
            return x, y, r_squared
        elif correlation_type in ['Positif lemah', 'Negatif lemah'] and 0.25 <= r_squared < 0.5:
            return x, y, r_squared
        elif correlation_type in ['Positif sangat lemah'] and r_squared < 0.25:
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

