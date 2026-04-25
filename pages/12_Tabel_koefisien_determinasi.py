import streamlit as st
import pandas as pd

st.title("Tabel Koefisien Determinasi")

# Data tabel
data = {
    "Koefisien Determinasi (r²)": [
        "r² = 0",
        "0 < r² < 0.25",
        "0.25 ≤ r² < 0.5",
        "0.5 ≤ r² < 0.75",
        "0.75 ≤ r² < 0.9",
        "0.9 ≤ r² < 1",
        "r² = 1"
    ],
    "Kekuatan Korelasi": [
        "Tidak ada korelasi",
        "Sangat lemah",
        "Lemah",
        "Sedang",
        "Kuat",
        "Sangat kuat",
        "Sempurna"
    ]
}

df = pd.DataFrame(data)

st.table(df)
