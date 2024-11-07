import streamlit as st
import json
from json2html import json2html

# Load JSON data from file
with open('inspirations.json', 'r') as file:
    inspirations_data = json.load(file)

# Extract the relevant data
inspirations = inspirations_data['inspirations']['inspiration']

# Streamlit app
st.title("Design Co-pilot Results Viewer")

# Sidebar to select JSON object
selected_index = st.sidebar.selectbox(
    "Select an inspiration to view:", 
    range(len(inspirations)), 
    format_func=lambda x: inspirations[x]['title']
)

# Display the selected JSON object
selected_inspiration = inspirations[selected_index]

st.header(selected_inspiration['title'])

# Function to display each section
def display_section(section_title, section_data):
    st.subheader(section_title)
    if isinstance(section_data, dict):
        for sub_key, sub_value in section_data.items():
            st.markdown(f"### {sub_key.replace('_', ' ').title()}")
            if isinstance(sub_value, list):
                for item in sub_value:
                    styled_html = json2html.convert(json=item)
                    st.markdown(styled_html, unsafe_allow_html=True)
            else:
                styled_html = json2html.convert(json=sub_value)
                st.markdown(styled_html, unsafe_allow_html=True)
    elif isinstance(section_data, list):
        for item in section_data:
            styled_html = json2html.convert(json=item)
            st.markdown(styled_html, unsafe_allow_html=True)
    else:
        styled_html = json2html.convert(json=section_data)
        st.markdown(styled_html, unsafe_allow_html=True)

# Iterate through each key in the selected inspiration
for key, value in selected_inspiration.items():
    if key != 'title':
        display_section(key.replace('_', ' ').title(), value)

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
