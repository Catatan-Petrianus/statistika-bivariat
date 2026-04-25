import streamlit as st
import pandas as pd

st.title("Tabel Koefisien Determinasi")

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

# Highlight warna
def highlight(val):
    if "Tidak" in val:
        return "background-color: #ffcccc"
    elif "Sangat lemah" in val:
        return "background-color: #ffe0b3"
    elif "Lemah" in val:
        return "background-color: #fff2cc"
    elif "Sedang" in val:
        return "background-color: #d9ead3"
    elif "Kuat" in val:
        return "background-color: #b6d7a8"
    elif "Sangat kuat" in val:
        return "background-color: #93c47d"
    elif "Sempurna" in val:
        return "background-color: #6aa84f"
    return ""

st.dataframe(df.style.applymap(highlight, subset=["Kekuatan Korelasi"]))
