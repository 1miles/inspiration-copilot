import streamlit as st
import json
from json2html import json2html

# Example JSON data (this would be replaced by your app's output)
json_data = [
    {
        "title": "Shared Experience Savings for Social Connection",
        "behavioral_patterns": [
            {"behavior": "Desire for connection", "friction": "Trust issues"},
            {"behavior": "Seeking savings", "friction": "Lack of tools"}
        ],
        "scenarios": [
            {"scenario_title": "The Budget Dilemma", "description": "A group struggles to save together."},
            {"scenario_title": "The Town Hall Dilemma", "description": "Residents discuss pooling funds for community benefit."}
        ]
    },
    {
        "title": "Empowering Civic Engagement through Accessible Savings",
        "behavioral_patterns": [
            {"behavior": "Interest in civic participation", "friction": "Complex bureaucracy"}
        ],
        "scenarios": [
            {"scenario_title": "The Town Hall Dilemma", "description": "Residents discuss pooling funds for community benefit."}
        ]
    }
]

# Streamlit app
st.title("AI Agent Results Viewer")

# Sidebar to select JSON object
selected_index = st.sidebar.selectbox("Select an inspiration to view:", range(len(json_data)), format_func=lambda x: json_data[x]['title'])

# Display the selected JSON object
selected_data = json_data[selected_index]

st.header(selected_data['title'])

# Option to view JSON data as raw or styled
view_option = st.radio("View JSON as:", ("Pretty JSON", "Styled HTML"))

if view_option == "Pretty JSON":
    st.json(selected_data)
else:
    # Convert JSON to styled HTML using json2html
    styled_html = json2html.convert(json=selected_data)
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
