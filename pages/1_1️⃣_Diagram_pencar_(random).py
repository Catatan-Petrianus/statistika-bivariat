import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import random

# Configure page layout
st.set_page_config(page_title="Diagram Pencar (Random)")
st.title("Diagram Pencar (Random)")
st.sidebar.success("Pilih materi di atas.")


# Initialize or retrieve DataFrame from session state
if 'df' not in st.session_state:
    # Function to generate unique pairs of random integers
    def generate_unique_pairs(n, lower_bound, upper_bound):
        pairs = set()
        while len(pairs) < n:
            x = random.randint(lower_bound, upper_bound)
            y = random.randint(lower_bound, upper_bound)
            pairs.add((x, y))
        return list(pairs)

    # Generate 10 unique pairs of random integers between 1 and 9
    unique_pairs = generate_unique_pairs(10, 1, 9)

    # Create a DataFrame from the unique pairs
    st.session_state.df = pd.DataFrame(unique_pairs, columns=['X', 'Y'])

# Use the stored DataFrame
df = st.session_state.df
num_points = len(df)

# Function to style the DataFrame and highlight the current row
def get_styled_df(current_index):
    # Highlight the row if its index matches current_index
    def highlight_row(row):
        return ['background-color: lightyellow' if row.name == current_index else '' for _ in row]

    styled = (
        df.style
          .apply(highlight_row, axis=1)
          .set_properties(**{'text-align': 'center'})
          .set_table_styles([dict(selector='th', props=[('text-align', 'center')])])
    )
    return styled

# Create two columns: one for the table, one for the animation
col1, col2 = st.columns([1, 2])

# Placeholder for the styled table
with col1:
    st.markdown(
        """
        <style>
        /* hide the index column (first <th> and first <td> in each row) */
        div[data-testid="stTable"] table th:first-child,
        div[data-testid="stTable"] table td:first-child {
            display: none;
        }
        /* centre‑align all visible headers & cells */
        div[data-testid="stTable"] table th,
        div[data-testid="stTable"] table td {
            text-align: center !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # Button to regenerate the table values
    if st.button("🎲 Buatkan tabel baru"):
        # Function to generate unique pairs of random integers
        def generate_unique_pairs(n, lower_bound, upper_bound):
            pairs = set()
            while len(pairs) < n:
                x = random.randint(lower_bound, upper_bound)
                y = random.randint(lower_bound, upper_bound)
                pairs.add((x, y))
            return list(pairs)

        # Generate 10 unique pairs of random integers between 1 and 9
        unique_pairs = generate_unique_pairs(10, 1, 9)

        # Create a DataFrame from the unique pairs
        st.session_state.df = pd.DataFrame(unique_pairs, columns=['X', 'Y'])
        df = st.session_state.df  # update local copy
    
    st.markdown(
        """
        <div style="text-align: center;">
        <h6>Tabel</h6>
        </div>
        """,
        unsafe_allow_html=True
    )
    # Static table display (will only update on regeneration)
    table_placeholder = st.empty()
    table_placeholder.dataframe(get_styled_df(-1), use_container_width=True, hide_index=True,)



# Controls and placeholders for the animation
with col2:
    start_button = st.button("✏️ Gambarkan diagram pencar")
    plot_placeholder = st.empty()
    progress_placeholder = st.empty()

    if start_button:
        for i in range(num_points):
            # Draw scatter plot up to the current point
            fig, ax = plt.subplots()
            # Plot all previous points in blue
            if i > 0:
                ax.scatter(df['X'][:i], df['Y'][:i], color='blue', alpha=0.6, label='Drawn')

            # Plot current point in red
            ax.scatter(df.loc[i, 'X'], df.loc[i, 'Y'], color='red', s=80, label='Current')

            # Set axes limits and grid
            ax.set_axisbelow(True)
            ax.set_xlim(0, 10)
            ax.set_ylim(0, 10)
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_xticks(np.arange(0, 11, 1))
            ax.set_yticks(np.arange(0, 11, 1))
            ax.grid(True, linestyle='dashed', linewidth=0.5)
            ax.set_title(f"Gambar titik ({df.loc[i, 'X']:.0f}, {df.loc[i, 'Y']:.0f})", color='red')

            # Update plot and table
            plot_placeholder.pyplot(fig)
            table_placeholder.dataframe(get_styled_df(i), use_container_width=True, hide_index=True)

            # Update progress bar
            progress = int((i+1) / num_points * 100)
            progress_placeholder.progress(progress, text=f"{progress}% complete")

            # Pause for animation effect
            time.sleep(1)

        # After animation, redraw all points in blue
        fig, ax = plt.subplots()
        ax.scatter(df['X'], df['Y'], color='blue', alpha=0.6)
        ax.set_axisbelow(True)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_xticks(np.arange(0, 11, 1))
        ax.set_yticks(np.arange(0, 11, 1))
        ax.grid(True, linestyle='dashed', linewidth=0.5)
        ax.set_title("Diagram Pencar")
        plot_placeholder.pyplot(fig)

        # Reset table highlight
        table_placeholder.dataframe(get_styled_df(-1), use_container_width=True, hide_index=True)

        # Clear progress bar and show completion message
        progress_placeholder.empty()
        st.success("Gambar selesai! 🎉")

