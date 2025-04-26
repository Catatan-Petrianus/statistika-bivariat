import streamlit as st
import pandas as pd
import numpy as np

# Configure page layout
st.set_page_config(page_title="Menghitung Koefisien Korelasi")
st.title("Menghitung Koefisien Korelasi")
st.sidebar.success("Pilih materi di atas.")

# Initialize 'df_r' in session state if it does not exist
if 'df_r' not in st.session_state:
    st.session_state.df_r = pd.DataFrame({
        "x": np.random.randint(1, 11, 5),
        "y": np.random.randint(1, 11, 5)
    })


# --- Session State Init ---
if 'step_korelasi' not in st.session_state:
    st.session_state.step_korelasi = 1
    st.session_state.df_r = pd.DataFrame({
        "x": np.random.randint(1, 11, 5),
        "y": np.random.randint(1, 11, 5)
    })
    
# Button at bottom to generate new data and rerun
if st.button('🎲 Buatkan tabel baru'):
    st.session_state.step_korelasi = 1
    st.session_state.df_r = pd.DataFrame({
    "x": np.random.randint(1, 11, 5),
    "y": np.random.randint(1, 11, 5)
    })
    st.rerun()
    

df = st.session_state.df_r


    

# --- Helper to render Tables 1–4 ---
def render_standard(df, width, highlight_col=None):
    html = df.to_html(index=False)
    highlight_css = (
        f".custom td:nth-child({highlight_col}){{background:#ffe599; color: #000}}"
        if highlight_col else ""
    )
    st.markdown(f"""
    <style>
      .custom {{ 
        width: {width}; table-layout: fixed; border-collapse: collapse; 
        margin-left: 0; 
      }}
      .custom th, .custom td {{
        width: 20%; text-align: center; padding: 8px; border:1px solid #ccc; color: #000;
      }}
      .custom th {{ background: #f8f9fb; color: #000; font-weight: bold; }}
      {highlight_css}
    </style>
    <table class="custom">
      {''.join(html.splitlines()[1:-1])}
    </table>
    """, unsafe_allow_html=True)

# --- Main Logic ---
df = st.session_state.df_r

if st.session_state.step_korelasi == 1:
    # Table 1
    st.markdown("#### Tabel")
    render_standard(df, width="40%")
    st.button("▶️ Langkah berikutnya", on_click=lambda: st.session_state.update(step_korelasi=2))
elif st.session_state.step_korelasi == 2:
    # Table 2: + xy
    df2 = df.copy()
    df2["xy"] = df2["x"] * df2["y"]
    st.markdown("#### Langkah 1: Kalikan nilai $x$ dan nilai $y$")
    render_standard(df2, width="60%", highlight_col=3)
    if st.button("▶️ Langkah berikutnya"):
        st.session_state.step_korelasi = 3

elif st.session_state.step_korelasi == 3:
    # Table 3: + x^2
    df3 = df.copy()
    df3["xy"] = df3["x"] * df3["y"]
    df3["x²"] = df3["x"] ** 2
    st.markdown("#### Langkah 2: Kuadratkan nilai $x$")
    render_standard(df3, width="80%", highlight_col=4)
    if st.button("▶️ Langkah berikutnya"):
        st.session_state.step_korelasi = 4

elif st.session_state.step_korelasi == 4:
    # Table 4: + y^2
    df4 = df.copy()
    df4["xy"] = df4["x"] * df4["y"]
    df4["x²"] = df4["x"] ** 2
    df4["y²"] = df4["y"] ** 2
    st.markdown("#### Langkah 3: Kuadratkan nilai $y$")
    render_standard(df4, width="100%", highlight_col=5)
    if st.button("▶️ Langkah berikutnya"):
        st.session_state.step_korelasi = 5

elif st.session_state.step_korelasi == 5:
    # Table 5: add Total row, merge col1+2 in last row, highlight it
    df5 = df.copy()
    df5["xy"] = df5["x"] * df5["y"]
    df5["x²"] = df5["x"] ** 2
    df5["y²"] = df5["y"] ** 2

    sum_x = df5["x"].sum()
    sum_y = df5["y"].sum()
    sum_xy = df5["xy"].sum()
    sum_x2 = df5["x²"].sum()
    sum_y2 = df5["y²"].sum()

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
        width: 20%; text-align: center; padding: 8px; border:1px solid #ccc; color: #000;
      }}
      .custom th {{ background: #f8f9fb; color: #000; font-weight: bold; }}
      /* highlight only the last row */
      .custom tr:last-child td {{ background: #ffe599; color: #000}}
    </style>
    <table class="custom">
      <tr>{headers}</tr>
      {rows}
      {total_row}
    </table>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    **Dari tabel di atas didapatkan:**
    
    - $\Sigma x$ = {df5['x'].sum()} 
    - $\Sigma y$ = {df5['y'].sum()} 
    - $\Sigma xy$ = {df5['xy'].sum()}  
    - $\Sigma x^2$ = {df5['x²'].sum()}  
    - $\Sigma y^2$ = {df5['y²'].sum()}
    """)

    if st.button("▶️ Langkah berikutnya"):
        st.session_state.step_korelasi = 6
else:
    df6 = df.copy()
    n = len(df6)
    df6["xy"] = df6["x"] * df6["y"]
    df6["x²"] = df6["x"] ** 2
    df6["y²"] = df6["y"] ** 2

    sum_x = df6["x"].sum()
    sum_y = df6["y"].sum()
    sum_xy = df6["xy"].sum()
    sum_x2 = df6["x²"].sum()
    sum_y2 = df6["y²"].sum()

    koef_korelasi = ((n * sum_xy) - (sum_x * sum_y)) / np.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))

    # Table 5: add Total row, merge col1+2 in last row, highlight it
    df5 = df.copy()
    df5["xy"] = df5["x"] * df5["y"]
    df5["x²"] = df5["x"] ** 2
    df5["y²"] = df5["y"] ** 2

    sum_x = df5["x"].sum()
    sum_y = df5["y"].sum()
    sum_xy = df5["xy"].sum()
    sum_x2 = df5["x²"].sum()
    sum_y2 = df5["y²"].sum()

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
    st.markdown("#### Langkah 5: Hitung koefisien korelasi")
    st.markdown(f"""
    <style>
      .custom {{
        width: 100%; table-layout: fixed; border-collapse: collapse; 
        margin-left: 0;
      }}
      .custom th, .custom td {{
        width: 20%; text-align: center; padding: 8px; border:1px solid #ccc;
      }}
      .custom th {{ background: #f8f9fb; color: #000; font-weight: bold; }}
      /* highlight only the last row */
      .custom tr:last-child td {{ background: #ffe599; color: #000}}
    </style>
    <table class="custom">
      <tr>{headers}</tr>
      {rows}
      {total_row}
    </table>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    **Dari tabel di atas didapatkan:**
    
    - $\Sigma x$ = {df5['x'].sum()} 
    - $\Sigma y$ = {df5['y'].sum()} 
    - $\Sigma xy$ = {df5['xy'].sum()}  
    - $\Sigma x^2$ = {df5['x²'].sum()}  
    - $\Sigma y^2$ = {df5['y²'].sum()}
    """)

    st.markdown("#### Hitung koefisien korelasi")
    st.latex(r"r = \frac{n\sum xy - \sum x \sum y}{\sqrt{(n\sum x^2 - (\sum x)^2)(n\sum y^2 - (\sum y)^2)}}")
    st.latex(
        fr"r = \frac{{{n} \times {sum_xy} - {sum_x} \times {sum_y}}}"
        fr"{{\sqrt{{({n} \times {sum_x2} - {sum_x}^2)({n} \times {sum_y2} - {sum_y}^2)}}}}"
    )
    
    st.latex(fr"\boxed{{r = {koef_korelasi:.3f}}}")


