import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Configure page layout
st.set_page_config(page_title="Regresi Linear (Random)")
st.title("Regresi Linear (Random)")
st.sidebar.success("Pilih materi di atas.")

# Number of points
n_points = st.number_input("Banyaknya data (maksimum 200 data)", min_value=10, max_value=200, value=100, step=10)


def init_data():
    # Generate x > 0
    x = np.random.uniform(0.1, 10, size=n_points)
    # Random slope between -10 and 10
    slope = np.random.uniform(-5, 5)
    # Random positive intercept
    intercept = np.random.uniform(0, 10)
    # Positive noise
    noise = np.random.normal(size=n_points)
    # Compute y ensuring y > 0
    y = slope * x + intercept + noise + np.abs(slope)*11
    return pd.DataFrame({'x': x, 'y': y})


# Initialize or load data
if 'df4' not in st.session_state:
    st.session_state.df4 = init_data()

df4 = st.session_state.df4

# Fit linear regression
model = LinearRegression()
model.fit(df4[['x']], df4['y'])
y_pred = model.predict(df4[['x']])

# Regression formula
slope_fit = model.coef_[0]
intercept_fit = model.intercept_
formula = f"y = {slope_fit:.2f}x + {intercept_fit:.2f}"

# Exact axis limits
x_lim = (df4['x'].min()-0.2, df4['x'].max()+0.2)
y_lim = (df4['y'].min()-1, df4['y'].max()+1)

# Toggle for regression line
show_reg = st.checkbox("Gambarkan regresi linear", value=True)

# Plot
fig, ax = plt.subplots()
ax.scatter(df4['x'], df4['y'], alpha=0.6)
if show_reg:
    ax.plot(df4['x'], y_pred, label='Regresi Linear', color='red')
ax.set_xlim(x_lim)
ax.set_ylim(y_lim)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Persamaan regresi linear: ' + formula, color='red')
ax.legend()

# Display plot
st.pyplot(fig)

# Button at bottom to generate new data and rerun
if st.button('🎲 Gambar yang baru'):
    st.session_state.df4 = init_data()
    st.rerun()
