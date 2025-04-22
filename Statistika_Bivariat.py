import streamlit as st

# Configure page layout
st.set_page_config(page_title="Regresi Linear")
st.title("Regresi Linear")
st.sidebar.success("Pilih Materi di atas.")

st.markdown(
    """
    ### Materi yang dipelajari:
    - ##### Diagram Pencar
    - ##### Koefisien korelasi
    - ##### Koefisien determinasi
    - ##### Regresi Linear
    """
)

# --- Footer ---
st.markdown("""<hr style="margin-top: 50px;">""", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: right; font-size: 14px; color: gray;'>Author: Petrianus Suwardi</p>",
    unsafe_allow_html=True
)
