import streamlit as st
import pandas as pd

# Define the file paths
source_file_path = r"C:\New_EmailSys\DDTS_Files\DDTS_Reports\Reportarw_136861.xlsx"
destination_file_path = r"C:\D\robotcontact\contact2.xlsx"

# Title of the app
st.title("Excel Column Extractor")

# Button to run the processing
if st.button("Run"):
    try:
        # Read the source Excel file
        df = pd.read_excel(source_file_path)

        # Check if the required columns exist
        if 'uploaded_part' in df.columns and 'SE_MAN' in df.columns:
            # Create a new DataFrame with the desired structure
            result_df = pd.DataFrame({
                'PN': df['uploaded_part'],
                'MAN': df['SE_MAN'],
                'IP': 'arw_136861'  # Constant value for IP
            })

            # Save the result to a new Excel file
            result_df.to_excel(destination_file_path, index=False)

            st.success("Data processed successfully! Saved to: " + destination_file_path)
        else:
            st.error("Columns 'uploaded_part' or 'SE_MAN' not found in the source file.")
    except Exception as e:
        st.error(f"Error: {e}")
