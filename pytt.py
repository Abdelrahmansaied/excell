import streamlit as st
import pandas as pd

# Title of the app
st.title("Excel Column Extractor")

# File uploader for the source Excel file
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Read the uploaded Excel file
    df = pd.read_excel(uploaded_file)

    # Check if the required columns exist
    if 'uploaded_part' in df.columns and 'SE_MAN' in df.columns:
        # Create a new DataFrame with the desired structure
        result_df = pd.DataFrame({
            'PN': df['uploaded_part'],
            'MAN': df['SE_MAN'],
            'IP': 'arw_136861'  # Constant value for IP
        })

        # Save the result to a new Excel file
        output_file = "contact2.xlsx"
        result_df.to_excel(output_file, index=False)

        # Provide download link for the new file
        st.success("Data processed successfully!")
        st.download_button("Download the result", data=open(output_file, 'rb'), file_name=output_file)

    else:
        st.error("Columns 'uploaded_part' or 'SE_MAN' not found in the uploaded file.")
