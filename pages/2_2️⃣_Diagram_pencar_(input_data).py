import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configure page layout
st.set_page_config(page_title="Diagram Pencar (Input Data)")
st.title("Diagram Pencar (Input Data)")
st.sidebar.success("Pilih materi di atas.")

st.markdown("""
    <style>
    div.stButton > button {
        background-color: #F8F9FB;
    }
    </style>
    """, unsafe_allow_html=True)

x_name = st.text_input("Nama variabel x: ")
y_name = st.text_input("Nama variabel y: ")

# --- 1) Input form -------------------------------------------------
with st.form("coord_form"):
    st.write("Masukkan data (satu setiap baris) dengan format `x,y`:")
    coords_input = st.text_area(
        label="Data",
        placeholder="1,2\n3,4\n5,6",
        height=150
    )

    submit_button = st.form_submit_button("📤 Submit")

# --- 2) Parse & store ------------------------------------------------
if submit_button:
    if (not x_name or not y_name or not coords_input.strip()):
        st.error("Semua field harus diisi!")
    else:
        coords = []
        for i, line in enumerate(coords_input.splitlines(), start=1):
            line = line.strip()
            if not line:
                continue
            try:
                x_str, y_str = line.split(",")
                coords.append((float(x_str), float(y_str)))
            except Exception:
                st.error(f"Baris {i!r} tidak valid. Gunakan format `x,y` (contoh: `3.5, -1.2`).")
                coords = None
                break

        if coords:
            df2 = pd.DataFrame(coords, columns=[x_name, y_name])
            # store in session state so the Plot button can access it
            st.session_state.df2 = df2

        # --- 3) Show table and plot button -----------------------------------
        if "df2" in st.session_state:
            # Create two columns: one for the table, one for the animation
            col1, col2 = st.columns([1, 2])

            with col1:
                st.markdown(
                    """
                    <div style="text-align: center;">
                        <h4>Tabel Data</h4>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.dataframe(st.session_state.df2, hide_index=True)

            with col2:
                st.markdown(
                    """
                    <div style="text-align: center;">
                        <h3>Diagram Pencar</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                fig, ax = plt.subplots()
                ax.scatter(st.session_state.df2[x_name], st.session_state.df2[y_name])
                ax.grid(True, linestyle='dashed', linewidth=0.5)
                ax.set_axisbelow(True)
                ax.set_xlim(left=0)
                ax.set_ylim(bottom=0)            
                ax.set_xlabel(x_name)
                ax.set_ylabel(y_name)
                st.pyplot(fig)
