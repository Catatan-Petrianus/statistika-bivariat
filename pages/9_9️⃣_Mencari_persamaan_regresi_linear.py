import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Mencari Persamaan Regresi Linear")
st.title("Mencari persamaan regresi linear")
st.sidebar.success("Pilih materi di atas.")

# --- Always initialize session state before any logic ---
if 'step' not in st.session_state:
    st.session_state.step = 1

if 'df_rl' not in st.session_state:
    st.session_state.df_rl = pd.DataFrame({
        "x": np.random.randint(1, 11, 5),
        "y": np.random.randint(1, 11, 5)
    })
    
  
if st.button('🎲 Buatkan tabel baru'):
    st.session_state.step = 1
    st.session_state.df_rl = pd.DataFrame({
        "x": np.random.randint(1, 11, 5),
        "y": np.random.randint(1, 11, 5)
    })
    st.rerun()
    

df = st.session_state.df_rl



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
        width: 20%; text-align: center; padding: 8px; border:1px solid #ccc;
      }}
      .custom th {{ background: #f8f9fb; font-weight: bold; color: #000 }}
      {highlight_css}
    </style>
    <table class="custom">
      {''.join(html.splitlines()[1:-1])}
    </table>
    """, unsafe_allow_html=True)

df = st.session_state.df_rl

if st.session_state.step == 1:
    st.markdown("#### Tabel")
    render_standard(df, width="40%")
    st.button("▶️ Langkah berikutnya", on_click=lambda: st.session_state.update(step=2))

elif st.session_state.step == 2:
    df2 = df.copy()
    df2["xy"] = df2["x"] * df2["y"]
    st.markdown("#### Langkah 1: Kalikan nilai $x$ dan nilai $y$")
    render_standard(df2, width="60%", highlight_col=3)
    if st.button("▶️ Langkah berikutnya"):
        st.session_state.step = 3

elif st.session_state.step == 3:
    df3 = df.copy()
    df3["xy"] = df3["x"] * df3["y"]
    df3["x²"] = df3["x"] ** 2
    st.markdown("#### Langkah 2: Kuadratkan nilai $x$")
    render_standard(df3, width="80%", highlight_col=4)
    if st.button("▶️ Langkah berikutnya"):
        st.session_state.step = 4

elif st.session_state.step == 4:
    df4 = df.copy()
    df4["xy"] = df4["x"] * df4["y"]
    df4["x²"] = df4["x"] ** 2

    sum_x = df4["x"].sum()
    sum_y = df4["y"].sum()
    sum_xy = df4["xy"].sum()
    sum_x2 = df4["x²"].sum()

    headers = "".join(f"<th>{c}</th>" for c in df4.columns)
    rows = ""
    for _, r in df4.iterrows():
        rows += "<tr>" + "".join(f"<td>{r[c]}</td>" for c in df4.columns) + "</tr>"

    total_row = (
        "<tr>"
        f"<td><b>{sum_x}</b></td>"
        f"<td><b>{sum_y}</b></td>"
        f"<td><b>{sum_xy}</b></td>"
        f"<td><b>{sum_x2}</b></td>"
        "</tr>"
    )

    st.markdown("#### Langkah 3: Hitung total nilai setiap kolom")
    st.markdown(f"""
    <style>
      .custom {{
        width: 80%; table-layout: fixed; border-collapse: collapse;
        margin-left: 0;
      }}
      .custom th, .custom td {{
        width: 20%; text-align: center; padding: 8px; border:1px solid #ccc;
      }}
      .custom th {{ background: #f8f9fb; font-weight: bold; color: #000 }}
      .custom tr:last-child td {{ background: #ffe599; color: #000 }}
    </style>
    <table class="custom">
      <tr>{headers}</tr>
      {rows}
      {total_row}
    </table>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    **Dari tabel di atas didapatkan:**

    - $\Sigma x$ = {sum_x}
    - $\Sigma y$ = {sum_y}
    - $\Sigma xy$ = {sum_xy}
    - $\Sigma x^2$ = {sum_x2}
    """)

    if st.button("▶️ Langkah berikutnya"):
        st.session_state.step = 5

elif st.session_state.step == 5:
    df5 = df.copy()
    df5["xy"] = df5["x"] * df5["y"]
    df5["x²"] = df5["x"] ** 2

    n = len(df5)
    sum_x = df5["x"].sum()
    sum_y = df5["y"].sum()
    sum_xy = df5["xy"].sum()
    sum_x2 = df5["x²"].sum()

    a = ((n * sum_xy) - (sum_x * sum_y)) / (n * sum_x2 - sum_x**2)
    b = (sum_y - a*sum_x)/n

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
        "</tr>"
    )

    st.markdown("#### Langkah 4: Carilah persamaan regresi linear")
    st.markdown(f"""
    <style>
      .custom {{
        width: 80%; table-layout: fixed; border-collapse: collapse;
        margin-left: 0;
      }}
      .custom th, .custom td {{
        width: 20%; text-align: center; padding: 8px; border:1px solid #ccc;
      }}
      .custom th {{ background: #f8f9fb; font-weight: bold; }}
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

    - $\Sigma x$ = {sum_x}
    - $\Sigma y$ = {sum_y}
    - $\Sigma xy$ = {sum_xy}
    - $\Sigma x^2$ = {sum_x2}
    """)

    st.markdown("#### Bentuk umum persamaan regresi linear:")
    st.latex(r'y = ax + b')
    
    st.markdown("#### Hitung nilai a (gradien)")
    st.latex(r"a = \frac{n\sum xy - \sum x \sum y}{n\sum x^2 - (\sum x)^2}")
    st.latex(
        fr"a = \frac{{{n} \times {sum_xy} - {sum_x} \times {sum_y}}}"
        fr"{{{n} \times {sum_x2} - {sum_x}^2}}"
    )
    st.latex(fr"\boxed{{a = {a:.3f}}}")

    st.markdown("#### Hitung nilai b (perpotongan dengan sumbu $y$)")
    st.latex(r"b = \frac{\sum y - a \sum x}{n}")
    if a>=0:
        st.latex(
            fr"b = \frac{{{sum_y} - {a:.3f} \times {sum_x}}}"
            fr"{{{n}}}"
        )
    else:
        st.latex(
            fr"b = \frac{{{sum_y} - ({a:.3f}) \times {sum_x}}}"
            fr"{{{n}}}"
        )
    st.latex(fr"\boxed{{b = {b:.3f}}}")

    st.markdown("#### Jadi persamaan regresi linearnya:")
    if b>0:
        st.latex(fr"\boxed{{y = {a:.3f} x + {b:.3f}}}")
    elif b<0:
        st.latex(fr"\boxed{{y = {a:.3f} X - {abs(b):.3f}}}")
    else:
        st.latex(fr"\boxed{{y = {a:.3f} x}}")
