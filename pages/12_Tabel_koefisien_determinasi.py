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

# Warna gradasi biru pastel → merah pastel
colors = [
    "#d0e7ff",  # biru sangat muda
    "#e2f0ff",
    "#f0f8ff",
    "#fff5f5",
    "#ffe5e5",
    "#ffd6d6",
    "#ffc2c2"   # merah pastel
]

# Apply style
def row_color(row):
    idx = row.name
    return [f"background-color: {colors[idx]}" for _ in row]

styled_df = (
    df.style
    .apply(row_color, axis=1)
    .set_properties(**{
        "text-align": "center",
        "font-weight": "500"
    })
    .set_table_styles([
        {
            "selector": "th",
            "props": [
                ("background-color", "#1f2a44"),  # gelap
                ("color", "white"),              # teks terang
                ("font-weight", "bold"),
                ("text-align", "center")
            ]
        }
    ])
)

st.dataframe(styled_df, use_container_width=True)
