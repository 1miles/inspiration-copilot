import streamlit as st
import json
from json2html import json2html

# Load JSON data from file
with open('inspirations.json', 'r') as file:
    inspirations_data = json.load(file)

# Extract the list of Inspirations
inspirations_list = inspirations_data['Inspirations']

# Streamlit app
st.title("Design Co-pilot Results Viewer")

# Create a list of inspiration titles or identifiers
inspiration_titles = [f"Inspiration {i+1}" for i in range(len(inspirations_list))]

# Sidebar to select an Inspiration to view
selected_inspiration_index = st.sidebar.selectbox(
    "Select an inspiration to view:",
    range(len(inspiration_titles)),
    format_func=lambda x: inspiration_titles[x]
)

# Get the selected Inspiration
selected_inspiration = inspirations_list[selected_inspiration_index]

st.header(f"Inspiration {selected_inspiration_index + 1}")

# Get the list of sections in the selected Inspiration
sections = list(selected_inspiration.keys())

# Sidebar to select a section to view
selected_section = st.sidebar.selectbox(
    "Select a section to view:",
    sections
)

# Display the selected section
section_data = selected_inspiration[selected_section]

st.subheader(selected_section.replace('_', ' ').title())

# Function to display the content
def display_section(section_data):
    if isinstance(section_data, dict):
        for key, value in section_data.items():
            st.markdown(f"### {key.replace('_', ' ').title()}")
            if isinstance(value, (dict, list)):
                styled_html = json2html.convert(json=value)
                st.markdown(styled_html, unsafe_allow_html=True)
            else:
                st.write(value)
    elif isinstance(section_data, list):
        for index, item in enumerate(section_data):
            st.markdown(f"### Item {index + 1}")
            if isinstance(item, (dict, list)):
                styled_html = json2html.convert(json=item)
                st.markdown(styled_html, unsafe_allow_html=True)
            else:
                st.write(item)
    else:
        st.write(section_data)

# Display the content of the selected section
display_section(section_data)

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
st.write("Select different inspirations and sections from the sidebar to explore their details.")
