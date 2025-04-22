import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Configure page layout
st.set_page_config(page_title="Korelasi")
st.title("Korelasi")
st.sidebar.success("Pilih materi di atas.")

# Generate sample data
size = 100
n = np.random.randint(low=0.1, high=20)

# Data with different correlations
data = {
    'Korelasi positif': pd.DataFrame({
        'X': np.arange(size),
        'Y': n+5+np.arange(size) + np.random.normal(0, n, size)
    }),
    'Korelasi Negatif': pd.DataFrame({
        'X': np.arange(size),
        'Y': 100+n+5-np.arange(size) + np.random.normal(0, n, size)
    }),
    'Tidak berkorelasi': pd.DataFrame({
        'X': np.arange(size),
        'Y': np.random.rand(size)*10
    })
}


# Dropdown to select correlation type
correlation_type = st.selectbox('Pilih jenis korelasi:', list(data.keys()))

# Plotting the selected correlation type
df = data[correlation_type]
fig, ax = plt.subplots()
ax.scatter(df['X'], df['Y'], label=f'{correlation_type}', alpha=0.6)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title(f'{correlation_type}')

# Display the plot in Streamlit
st.pyplot(fig)
