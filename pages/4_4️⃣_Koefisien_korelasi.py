import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Configure page layout
st.set_page_config(page_title="Koefisien Korelasi")
st.title("Koefisien Korelasi")
st.sidebar.success("Pilih materi di atas.")

m = np.random.randint(low=1, high=20)

# Custom CSS to hide the slider handle value
hide_slider_value_css = """
    <style>
    .stSlider > div > div > div > div > div {
        display: none;
    }
    </style>
    """

# Inject the custom CSS into the Streamlit app
st.markdown(hide_slider_value_css, unsafe_allow_html=True)

# 1. Correlation slider: choose target correlation between X and Y
r_target = st.slider(
    label="Target nilai korelasi (r)",
    min_value=-1.0, max_value=1.0, value=0.5, step=0.01,
)

# 2. Number of points
n_points = st.number_input("Banyaknya data (maksimum 1000 data)", min_value=10, max_value=1000, value=200, step=10)


# 3. Generate synthetic data with approximate correlation r_target
@st.cache_data
def make_correlated_data(n, r):
    x = np.random.rand(n) * 10 
    noise = np.random.normal(size=n)
    y = (-5*r+5+r * x + np.sqrt(max(0, 1 - r**2)) * noise) *m
    return x, y

x, y = make_correlated_data(n_points, r_target)
df = pd.DataFrame({"X": x, "Y": y})

# 5. Plot
fig, ax = plt.subplots()
ax.scatter(df["X"], df["Y"], alpha=0.6)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title(f"Koefisien korelasi (r = {np.corrcoef(x,y)[0,1]:.5f})")

st.pyplot(fig)
