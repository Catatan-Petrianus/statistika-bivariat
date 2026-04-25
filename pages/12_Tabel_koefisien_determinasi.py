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

# Warna gradasi
colors = [
    "#d0e7ff",
    "#e2f0ff",
    "#f0f8ff",
    "#fff5f5",
    "#ffe5e5",
    "#ffd6d6",
    "#ffc2c2"
]

# Build HTML table manual
headers = "".join(f"<th>{col}</th>" for col in df.columns)

rows = ""
for i, row in df.iterrows():
    bg = colors[i]
    rows += "<tr>"
    for val in row:
        rows += f'<td style="background-color:{bg};">{val}</td>'
    rows += "</tr>"

html_table = f"""
<style>
.table-custom {{
    width: 100%;
    border-collapse: collapse;
    table-layout: fixed;
}}

.table-custom th {{
    background-color: black;
    color: yellow;
    font-weight: bold;
    text-align: center;
    padding: 10px;
    border: 1px solid #ccc;
}}

.table-custom td {{
    text-align: center;
    padding: 10px;
    border: 1px solid #ccc;
}}
</style>

<table class="table-custom">
    <tr>{headers}</tr>
    {rows}
</table>
"""

st.markdown(html_table, unsafe_allow_html=True)
