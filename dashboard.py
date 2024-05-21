import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio
import os
import io
import tempfile
from datetime import datetime
import requests
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from io import BytesIO
import base64
import random
import string
from datetime import datetime, timedelta
import xlsxwriter


# Page configuration
st.set_page_config(page_title="Web Server Log Analysis Dashboard", page_icon="📈", layout="wide")

#Main Page title
st.title("Payris Fun Olympic Games 2024")

def generate_ip_address():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def generate_country():
    countries = ["United States", "Canada", "United Kingdom", "Germany", "France", "Spain", "Italy", "Australia", "Japan", "China"]
    return random.choice(countries)

def generate_city(country):
    cities = {
        "United States": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"],
        "Canada": ["Toronto", "Montreal", "Vancouver", "Calgary", "Edmonton", "Ottawa", "Winnipeg", "Quebec City", "Hamilton", "Kitchener"],
        "United Kingdom": ["London", "Birmingham", "Manchester", "Leeds", "Glasgow", "Liverpool", "Newcastle upon Tyne", "Nottingham", "Sheffield", "Bristol"],
        "Germany": ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt", "Stuttgart", "Düsseldorf", "Leipzig", "Dortmund", "Essen"],
        "France": ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg", "Montpellier", "Bordeaux", "Lille"],
        "Spain": ["Madrid", "Barcelona", "Valencia", "Seville", "Zaragoza", "Malaga", "Murcia", "Las Palmas", "Bilbao", "Alicante"],
        "Italy": ["Rome", "Milan", "Naples", "Turin", "Palermo", "Genoa", "Bologna", "Florence", "Bari", "Catania"],
        "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Gold Coast", "Newcastle", "Canberra", "Wollongong", "Logan City"],
        "Japan": ["Tokyo", "Yokohama", "Osaka", "Nagoya", "Sapporo", "Kobe", "Kyoto", "Fukuoka", "Kawasaki", "Saitama"],
        "China": ["Shanghai", "Beijing", "Chongqing", "Tianjin", "Guangzhou", "Shenzhen", "Wuhan", "Dongguan", "Foshan", "Chengdu"]
    }

    if country in cities:
        return random.choice(cities[country])
    else:
        return None

def generate_request_method():
    methods = ["GET", "POST", "PUT", "DELETE"]
    return random.choice(methods)

def generate_request_url():
    urls = [
        "/sports/archery", "/live-stream?event=archery", "/schedule?sport=archery", "/results?sport=archery", "/medals?sport=archery",
        "/sports/athletics", "/live-stream?event=athletics", "/schedule?sport=athletics", "/results?sport=athletics", "/medals?sport=athletics",
        # Add more URLs based on the data dictionary
    ]
    return random.choice(urls)

def generate_referrer():
    referrers = [
        "https://funolympic-games.com/", "https://funolympic-games.com/sports", "https://funolympic-games.com/live-stream",
        "https://funolympic-games.com/schedule", "https://funolympic-games.com/results", "https://funolympic-games.com/medals",
        # Add more referrers based on the data dictionary
    ]
    return random.choice(referrers)

def generate_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
    ]
    return random.choice(user_agents)

def generate_device_type():
    device_types = ["desktop", "mobile", "tablet", "smartphone", "laptop", "smartwatch"]
    return random.choice(device_types)

def generate_operating_system():
    operating_systems = ["Windows 10", "macOS Catalina", "iOS 14", "Android 11", "Ubuntu 20.04"]
    return random.choice(operating_systems)

def generate_response_status_code():
    status_codes = [200, 404]
    return random.choice(status_codes)

def generate_viewer_type():
    viewer_types = ["regular viewer", "new viewer", "returning viewer"]
    return random.choice(viewer_types)

def generate_viewer_sentiment():
    viewer_sentiments = ["positive", "negative", "neutral"]
    return random.choice(viewer_sentiments)

def generate_main_interest():
    interests = ["Archery", "Athletics (Track and Field)", "Badminton", "Basketball", "Boxing", "Canoe Sprint", "Cricket", "Cycling", "Diving", "Fencing", "Field Hockey", "Football (Soccer)", "Golf", "Gymnastics", "Handball", "Judo", "Karate", "Rugby", "Sailing", "Shooting", "Skateboarding", "Sport Climbing", "Surfing", "Swimming", "Table Tennis", "Taekwondo", "Tennis", "Volleyball (Indoor, Beach)", "Water Polo", "Weightlifting", "Wrestling"]
    return random.choice(interests)

def generate_webserver_log(num_records):
    log_data = []
    for _ in range(num_records):
        country = generate_country()
        city = generate_city(country)
        # Generate current date in m/d/yyyy format
        date_str = datetime.now().strftime("%m/%d/%Y")
        # Generate current time in 24-hour format with seconds
        time_str = datetime.now().strftime("%H:%M:%S")
        server_response_time = random.randint(1, 500)
        advertising_impressions = random.randint(1, 500)
        num_visits = random.randint(1, 500)
        record = {
            "Date": date_str,
            "Time": time_str,
            "IP Address": generate_ip_address(),
            "Country": country,
            "City": city if city else "Unknown",
            "Request Method": generate_request_method(),
            "Request URL": generate_request_url(),
            "Referrer": generate_referrer(),
            "User Agent": generate_user_agent(),
            "Device Type": generate_device_type(),
            "Operating System": generate_operating_system(),
            "Response Status Code": generate_response_status_code(),
            "Server Response Time": server_response_time,
            "Viewer Type": generate_viewer_type(),
            "Viewer Sentiment": generate_viewer_sentiment(),
            "Advertising Impressions": advertising_impressions,
            "Number of Visits": num_visits,
            "Main Interest": generate_main_interest()
        }
        log_data.append(record)
    return pd.DataFrame(log_data)

# Generate Webserver Log
st.subheader("Generate Webserver Log")
num_records = st.number_input("Number of Records", min_value=1, value=100)
export_format = st.radio("Export Format", ["CSV", "Excel"])

if st.button("Generate Webserver Log", key="generate_log"):
    webserver_log = generate_webserver_log(num_records)
    st.write(webserver_log)

    # Provide the export button only after log is generated
    if webserver_log is not None:
        if export_format == "CSV":
            csv_data = webserver_log.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download CSV",
                data=csv_data,
                file_name='webserverlog.csv',
                mime='text/csv',
            )
        elif export_format == "Excel":
            with io.BytesIO() as buffer:
                with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                    webserver_log.to_excel(writer, index=False)
                excel_data = buffer.getvalue()
            st.download_button(
                label="Download Excel",
                data=excel_data,
                file_name='webserverlog.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            )


# Load default data
file_path = "Web server log data.xlsx"
default_data = pd.read_excel(file_path)

# Display statistical summary
st.subheader("Statistical Summary📊")
with st.expander("Click to view"):
    total_countries = default_data["Country"].nunique()
    total_visits = default_data["Number of Visits"].sum()
    total_interests = default_data["Main Interest"].nunique()
    st.markdown(f"""
    <div style='padding: 10px; border-radius: 10px; border: 1px solid #ccc; background-color: #f0f0f0;'>
        <h3 style='margin-bottom: 10px;'>Statistical Summary📊</h3>
        <ul style='list-style-type: none; padding-left: 0;'>
            <li>🌍 Total Number of Countries: <b>{total_countries}</b></li>
            <li>👥 Total Number of Visits: <b>{total_visits}</b></li>
            <li>💡 Total Number of Unique Interests: <b>{total_interests}</b></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


# Initialize a boolean flag to control the visibility of the dataset
show_data = False

# Add a button to view data at the top of the page
st.subheader("View default Data")
if st.button("View Data"):
    show_data = True
    st.write(default_data)

# Add a Close button to hide the dataset section, visible only when show_data is True
if show_data and st.button("Close"):
    show_data = False

# Convert "Date" and "Time" columns to datetime
default_data["Date"] = pd.to_datetime(default_data["Date"])
default_data["Time"] = pd.to_datetime(default_data["Time"], format="%H:%M:%S").dt.time

# Sidebar filters
with st.sidebar:
    st.title("Filters🔍")
    countries = st.multiselect("Select Countries", default_data["Country"].unique())
    interests = st.multiselect("Select Main Interests", default_data["Main Interest"].unique())
    date_range = st.date_input("Select Date Range", value=[default_data["Date"].min(), default_data["Date"].max()])
    start_time = st.time_input("Select Start Time", value=datetime.strptime("00:00:00", "%H:%M:%S").time())
    end_time = st.time_input("Select End Time", value=datetime.strptime("23:59:59", "%H:%M:%S").time())
    device_types = st.multiselect("Select Device Types", default_data["Device Type"].unique())
    viewer_sentiments = st.multiselect("Select Viewer Sentiments", default_data["Viewer Sentiment"].unique())
    status_codes = st.multiselect("Select Status Codes", default_data["Response Status Code"].unique())

    # File uploader
    st.title("Upload your own Excel file")
    uploaded_file = st.file_uploader("Choose an Excel file", type=['xlsx', 'xls', 'csv'])

# Load data based on uploaded file or default data
if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file)
    data["Date"] = pd.to_datetime(data["Date"])
    data["Time"] = pd.to_datetime(data["Time"], format="%H:%M:%S").dt.time
else:
    data = default_data

# Ensure filters are properly set before applying them
if not countries:
    countries = data["Country"].unique()
if not interests:
    interests = data["Main Interest"].unique()
if not date_range:
    date_range = [data["Date"].min(), data["Date"].max()]
if not device_types:
    device_types = data["Device Type"].unique()
if not viewer_sentiments:
    viewer_sentiments = data["Viewer Sentiment"].unique()
if not status_codes:
    status_codes = data["Response Status Code"].unique()

# Filter data based on selections
filtered_data = data[
    (data["Country"].isin(countries)) &
    (data["Main Interest"].isin(interests)) &
    (data["Date"].between(pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1]))) &
    (data["Time"].between(start_time, end_time)) &
    (data["Device Type"].isin(device_types)) &
    (data["Viewer Sentiment"].isin(viewer_sentiments)) &
    (data["Response Status Code"].isin(status_codes))
]

# Main content
st.title("Web Server Log Analysis Dashboard📈")



# Function to style chart titles
def style_chart(fig, title):
    fig.update_layout(title={'text': title, 'x': 0.5, 'y': 0.95, 'xanchor': 'center', 'yanchor': 'top'})

# Create visualizations
charts = []
with st.container():
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    # Column 1: Top 10 Country-wise Distribution of Visits & Viewer Interest Analysis
    with col1:
        top_countries = filtered_data.groupby("Country")["Number of Visits"].sum().reset_index()
        top_countries = top_countries.sort_values(by="Number of Visits", ascending=False).head(10)
        fig1 = px.bar(top_countries, x="Country", y="Number of Visits")
        style_chart(fig1, "Top 10 Country-wise Visits")
        st.plotly_chart(fig1, use_container_width=True)
        charts.append(fig1)

        interest_count = filtered_data["Main Interest"].value_counts().reset_index()
        interest_count.columns = ["Interest", "Viewers"]
        fig2 = px.bar(interest_count, x="Interest", y="Viewers")
        style_chart(fig2, "Viewer Interests")
        st.plotly_chart(fig2, use_container_width=True)
        charts.append(fig2)

    # Column 2: Viewer Type Analysis & Viewer Sentiment Analysis
    with col2:
        viewer_type_count = filtered_data["Viewer Type"].value_counts().reset_index()
        viewer_type_count.columns = ["Viewer Type", "Count"]
        fig3 = px.pie(viewer_type_count, values="Count", names="Viewer Type")
        style_chart(fig3, "Viewer Types")
        st.plotly_chart(fig3, use_container_width=True)
        charts.append(fig3)

        sentiment_count = filtered_data["Viewer Sentiment"].value_counts().reset_index()
        sentiment_count.columns = ["Sentiment", "Count"]
        fig4 = px.bar(sentiment_count, x="Sentiment", y="Count")
        style_chart(fig4, "Viewer Sentiments")
        st.plotly_chart(fig4, use_container_width=True)
        charts.append(fig4)

    # Column 3: Device Type Analysis & Operating System Analysis
    with col3:
        device_count = filtered_data["Device Type"].value_counts().reset_index()
        device_count.columns = ["Device Type", "Count"]
        fig5 = px.pie(device_count, values="Count", names="Device Type")
        style_chart(fig5, "Device Types")
        st.plotly_chart(fig5, use_container_width=True)
        charts.append(fig5)

        os_count = filtered_data["Operating System"].value_counts().reset_index()
        os_count.columns = ["Operating System", "Count"]
        fig6 = px.bar(os_count, x="Operating System", y="Count")
        style_chart(fig6, "Operating Systems")
        st.plotly_chart(fig6, use_container_width=True)
        charts.append(fig6)

    # Column 4: Response Status Code Analysis & Time vs Visits
    with col4:
        status_count = filtered_data["Response Status Code"].value_counts().reset_index()
        status_count.columns = ["Status Code", "Count"]
        fig7 = px.pie(status_count, values="Count", names="Status Code")
        style_chart(fig7, "Response Status Codes")
        st.plotly_chart(fig7, use_container_width=True)
        charts.append(fig7)

        time_visits = filtered_data.groupby("Time")["Number of Visits"].sum().reset_index()
        fig8 = px.line(time_visits, x="Time", y="Number of Visits")
        style_chart(fig8, "Visits Over Time")
        st.plotly_chart(fig8, use_container_width=True)
        charts.append(fig8)

# Export options for Data
st.sidebar.title("Export Data")
export_data_format = st.sidebar.selectbox("Select Export Format", ["CSV", "Excel"])

if st.sidebar.button("Export"):
    if export_data_format == "CSV":
        csv_data = filtered_data.to_csv(index=False)
        st.sidebar.download_button("Download CSV", data=csv_data, file_name="web_server_log.csv", mime="text/csv")
    elif export_data_format == "Excel":
        excel_file_path = "web_server_log.xlsx"
        filtered_data.to_excel(excel_file_path, index=False)
        st.sidebar.download_button("Download Excel", data=open(excel_file_path, 'rb'), file_name=excel_file_path, mime="application/vnd.ms-excel")

# Export options for Visualizations
st.sidebar.title("Export Visualizations")
if st.sidebar.button("Export Visuals as PDF"):
    # Create a temporary directory to save images
    with tempfile.TemporaryDirectory() as tmpdirname:
        # Create a PDF document
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        elements = []

        # Add a title
        styles = getSampleStyleSheet()
        elements.append(Paragraph("Web Server Log Analysis Dashboard", styles['Title']))
        elements.append(Spacer(1, 12))

        # Save each chart as an image and add to PDF
        for i, fig in enumerate(charts):
            img_path = os.path.join(tmpdirname, f"chart_{i}.png")
            fig.write_image(img_path)
            img = Image(img_path)
            img.drawHeight = 4 * inch
            img.drawWidth = 6 * inch
            elements.append(img)
            elements.append(Spacer(1, 12))

        doc.build(elements)
        buffer.seek(0)
        st.sidebar.download_button("Download PDF", data=buffer, file_name="web_server_log_analysis.pdf", mime="application/pdf")

# Footer
st.markdown("""
<style>
footer {
    visibility: hidden;
}
</style>
<footer style="visibility:visible;position:fixed;bottom:0;width:100%;background-color:#f0f0f0;text-align:center;padding:10px 0;">
    Web Server Log Analysis Dashboard © 2024 | Created with ❤️ by Helman Tsheboyagae
</footer>
""", unsafe_allow_html=True)
