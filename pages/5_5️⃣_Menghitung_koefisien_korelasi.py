import streamlit as st
import pandas as pd
import numpy as np

# Configure page layout
st.set_page_config(page_title="Menghitung Koefisien Korelasi")
st.title("Menghitung Koefisien Korelasi")
st.sidebar.success("Pilih Materi di atas.")

# Button at bottom to generate new data and rerun
if st.button('🎲 Buatkan tabel baru'):
    st.session_state.step = 1
    st.session_state.df_r = pd.DataFrame({
    "X": np.random.randint(1, 11, 5),
    "Y": np.random.randint(1, 11, 5)
    })
    st.rerun()

# --- Session State Init ---
if 'step' not in st.session_state:
    st.session_state.step = 1
    st.session_state.df_r = pd.DataFrame({
        "X": np.random.randint(1, 11, 5),
        "Y": np.random.randint(1, 11, 5)
    })
    

# --- Helper to render Tables 1–4 ---
def render_standard(df, width, highlight_col=None):
    html = df.to_html(index=False)
    highlight_css = (
        f".custom td:nth-child({highlight_col}){{background:#ffe599;}}"
        if highlight_col else ""
    )
    st.markdown(f"""
    <style>
      .custom {{ 
        width: {width}; table-layout: fixed; border-collapse: collapse; 
        margin-left: 0; 
      }}
      .custom th, .custom td {{
        width: 20%; text-align: center; padding: 8px; border:1px solid #ccc;
      }}
      .custom th {{ background: #f8f9fb; font-weight: bold; }}
      {highlight_css}
    </style>
    <table class="custom">
      {''.join(html.splitlines()[1:-1])}
    </table>
    """, unsafe_allow_html=True)

# --- Main Logic ---
df = st.session_state.df_r

if st.session_state.step == 1:
    # Table 1
    st.markdown("#### Tabel")
    render_standard(df, width="40%")
    st.button("▶️ Next", on_click=lambda: st.session_state.update(step=2))
elif st.session_state.step == 2:
    # Table 2: + XY
    df2 = df.copy()
    df2["XY"] = df2["X"] * df2["Y"]
    st.markdown("#### Langkah 1: Kalikan nilai X dan nilai Y")
    render_standard(df2, width="60%", highlight_col=3)
    if st.button("▶️ Next"):
        st.session_state.step = 3

elif st.session_state.step == 3:
    # Table 3: + X^2
    df3 = df.copy()
    df3["XY"] = df3["X"] * df3["Y"]
    df3["X²"] = df3["X"] ** 2
    st.markdown("#### Langkah 2: Kuadratkan nilai X")
    render_standard(df3, width="80%", highlight_col=4)
    if st.button("▶️ Next"):
        st.session_state.step = 4

elif st.session_state.step == 4:
    # Table 4: + Y^2
    df4 = df.copy()
    df4["XY"] = df4["X"] * df4["Y"]
    df4["X²"] = df4["X"] ** 2
    df4["Y²"] = df4["Y"] ** 2
    st.markdown("#### Langkah 3: Kuadratkan nilai Y")
    render_standard(df4, width="100%", highlight_col=5)
    if st.button("▶️ Next"):
        st.session_state.step = 5

elif st.session_state.step == 5:
    # Table 5: add Total row, merge col1+2 in last row, highlight it
    df5 = df.copy()
    df5["XY"] = df5["X"] * df5["Y"]
    df5["X²"] = df5["X"] ** 2
    df5["Y²"] = df5["Y"] ** 2

    sum_x = df5["X"].sum()
    sum_y = df5["Y"].sum()
    sum_xy = df5["XY"].sum()
    sum_x2 = df5["X²"].sum()
    sum_y2 = df5["Y²"].sum()

    # Build HTML manually
    headers = "".join(f"<th>{c}</th>" for c in df5.columns)
    rows = ""
    for _, r in df5.iterrows():
        rows += "<tr>" + "".join(f"<td>{r[c]}</td>" for c in df5.columns) + "</tr>"

    total_row = (
        "<tr>"
        f"<td><b>{sum_x}</b></td>"
        f"<td><b>{sum_y}</b></td>"
        f"<td><b>{sum_xy}</b></td>"
        f"<td><b>{sum_x2}</b></td>"
        f"<td><b>{sum_y2}</b></td>"
        "</tr>"
    )
    st.markdown("#### Langkah 4: Hitung total nilai setiap kolom")
    st.markdown(f"""
    <style>
      .custom {{
        width: 100%; table-layout: fixed; border-collapse: collapse; 
        margin-left: 0;
      }}
      .custom th, .custom td {{
        width: 20%; text-align: center; padding: 8px; border:1px solid #ccc;
      }}
      .custom th {{ background: #f8f9fb; font-weight: bold; }}
      /* highlight only the last row */
      .custom tr:last-child td {{ background: #ffe599; }}
    </style>
    <table class="custom">
      <tr>{headers}</tr>
      {rows}
      {total_row}
    </table>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    **Dari tabel di atas didapatkan:**
    
    - $\Sigma x$ = {df5['X'].sum()} 
    - $\Sigma y$ = {df5['Y'].sum()} 
    - $\Sigma xy$ = {df5['XY'].sum()}  
    - $\Sigma x^2$ = {df5['X²'].sum()}  
    - $\Sigma y^2$ = {df5['Y²'].sum()}
    """)

    if st.button("▶️ Next"):
        st.session_state.step = 6
else:
    df6 = df.copy()
    n = len(df6)
    df6["XY"] = df6["X"] * df6["Y"]
    df6["X²"] = df6["X"] ** 2
    df6["Y²"] = df6["Y"] ** 2

    sum_x = df6["X"].sum()
    sum_y = df6["Y"].sum()
    sum_xy = df6["XY"].sum()
    sum_x2 = df6["X²"].sum()
    sum_y2 = df6["Y²"].sum()

    koef_korelasi = ((n * sum_xy) - (sum_x * sum_y)) / np.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))

    # Table 5: add Total row, merge col1+2 in last row, highlight it
    df5 = df.copy()
    df5["XY"] = df5["X"] * df5["Y"]
    df5["X²"] = df5["X"] ** 2
    df5["Y²"] = df5["Y"] ** 2

    sum_x = df5["X"].sum()
    sum_y = df5["Y"].sum()
    sum_xy = df5["XY"].sum()
    sum_x2 = df5["X²"].sum()
    sum_y2 = df5["Y²"].sum()

    # Build HTML manually
    headers = "".join(f"<th>{c}</th>" for c in df5.columns)
    rows = ""
    for _, r in df5.iterrows():
        rows += "<tr>" + "".join(f"<td>{r[c]}</td>" for c in df5.columns) + "</tr>"

    total_row = (
        "<tr>"
        f"<td><b>{sum_x}</b></td>"
        f"<td><b>{sum_y}</b></td>"
        f"<td><b>{sum_xy}</b></td>"
        f"<td><b>{sum_x2}</b></td>"
        f"<td><b>{sum_y2}</b></td>"
        "</tr>"
    )
    st.markdown("#### Langkah 4: Hitung total nilai setiap kolom")
    st.markdown(f"""
    <style>
      .custom {{
        width: 100%; table-layout: fixed; border-collapse: collapse; 
        margin-left: 0;
      }}
      .custom th, .custom td {{
        width: 20%; text-align: center; padding: 8px; border:1px solid #ccc;
      }}
      .custom th {{ background: #f8f9fb; font-weight: bold; }}
      /* highlight only the last row */
      .custom tr:last-child td {{ background: #ffe599; }}
    </style>
    <table class="custom">
      <tr>{headers}</tr>
      {rows}
      {total_row}
    </table>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    **Dari tabel di atas didapatkan:**
    
    - $\Sigma x$ = {df5['X'].sum()} 
    - $\Sigma y$ = {df5['Y'].sum()} 
    - $\Sigma xy$ = {df5['XY'].sum()}  
    - $\Sigma x^2$ = {df5['X²'].sum()}  
    - $\Sigma y^2$ = {df5['Y²'].sum()}
    """)

    st.markdown("#### Hitung koefisien korelasi r")
    st.latex(r"r = \frac{n\sum xy - \sum x \sum y}{\sqrt{(n\sum x^2 - (\sum x)^2)(n\sum y^2 - (\sum y)^2)}}")
    st.latex(
        fr"r = \frac{{{n} \times {sum_xy} - {sum_x} \times {sum_y}}}"
        fr"{{\sqrt{{({n} \times {sum_x2} - {sum_x}^2)({n} \times {sum_y2} - {sum_y}^2)}}}}"
    )
    
    st.latex(fr"\boxed{{r = {koef_korelasi:.3f}}}")


