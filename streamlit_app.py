import streamlit as st
import json
from json2html import json2html

# Load JSON data from file
with open('inspirations.json', 'r') as file:
    inspirations_data = json.load(file)

# Extract the relevant data
inspirations = inspirations_data['inspirations']['inspiration']

# Streamlit app
st.title("AI Agent Results Viewer")

# Sidebar to select JSON object
selected_index = st.sidebar.selectbox(
    "Select an inspiration to view:", 
    range(len(inspirations)), 
    format_func=lambda x: inspirations[x]['title']
)

# Display the selected JSON object
selected_inspiration = inspirations[selected_index]

st.header(selected_inspiration['title'])

# Option to view JSON data as raw or styled
view_option = st.radio("View JSON as:", ("Pretty JSON", "Styled HTML"))

if view_option == "Pretty JSON":
    st.json(selected_inspiration)
else:
    # Convert JSON to styled HTML using json2html
    styled_html = json2html.convert(json=selected_inspiration)
    st.markdown(styled_html, unsafe_allow_html=True)

# Additional styling
st.markdown(
    """
    <style>
    .json2html { font-family: Arial, sans-serif; font-size: 14px; }
    .json2html-table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
    .json2html-table th, .json2html-table td { border: 1px solid #ddd; padding: 8px; text-align: left; }
    .json2html-table th { background-color: #f2f2f2; }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer message
st.write("Select different inspirations from the sidebar to explore their details.")
