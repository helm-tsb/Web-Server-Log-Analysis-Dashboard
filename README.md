# Web-Server-Log-Analysis-Dashboard

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-blue)](https://webserverlog-analysis-dashboard.streamlit.app/)

## Overview

The **Web-Server-Log-Analysis-Dashboard** is a powerful tool built using Streamlit for visualizing and analyzing web server logs. It offers an interactive and user-friendly interface to explore various metrics and trends in web server logs, such as the distribution of visits by country, viewer types, device types, and more.

## Features

- **Generate Web Server Logs**: Create synthetic web server logs with customizable number of records.
- **View and Filter Data**: Explore default or uploaded web server log data with various filters.
- **Statistical Summary**: Get quick insights into the total number of countries, visits, and unique interests.
- **Interactive Visualizations**: Analyze data with interactive charts and graphs.
- **Export Data and Visualizations**: Download filtered data as CSV or Excel files and export visualizations as PDF.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/Web-Server-Log-Analysis-Dashboard.git
    cd Web-Server-Log-Analysis-Dashboard
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app**:
    ```bash
    streamlit run dashboard.py
    ```

## Usage

### Generate Web Server Logs
- Input the desired number of records.
- Choose the export format (CSV or Excel).
- Click on "Generate Webserver Log" to create and download the log file.

### View and Filter Data
- Use the sidebar filters to select specific countries, interests, date ranges, times, device types, viewer sentiments, and status codes.
- Click on "View Data" to display the default or uploaded web server log data.

### Interactive Visualizations
- Analyze data through various charts and graphs like top country-wise visits, viewer interests, viewer types, device types, and more.

### Export Data and Visualizations
- Download filtered data as CSV or Excel files.
- Export visualizations as a PDF document.

## Example Data

The project includes an example dataset `Web server log data.xlsx` to demonstrate its capabilities. You can also upload your own dataset in Excel or CSV format for analysis.

## Screenshots

![Dashboard Screenshots to be uploaded](screenshot.png)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or suggestions, feel free to contact me at tsheboyagaeh@gmail.com.
