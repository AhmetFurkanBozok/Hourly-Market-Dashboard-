# 📊 Hourly Market Analysis Dashboard

This repository contains a Python-based interactive web dashboard built with **Streamlit**. It retrieves, stores, and visualizes 1-month hourly (1h) stock market data for major aerospace and automotive companies.

## 🚀 Features & Extra Efforts
* **Automated Data Retrieval:** Fetches the latest 1-month/1-hour interval data using `yfinance` and stores it locally.
* **Technical Indicator (Extra 10p):** Calculates and displays a 20-period Simple Moving Average (SMA 20) alongside the closing price.
* **Interactive UI (Extra 10p):** Features a sidebar for dynamic ticker selection (e.g., Airbus, Boeing, Ford, Tesla) and an option to toggle the SMA indicator on/off.
* **Advanced Visualizations:** Uses `plotly` for interactive line charts (Price Trend) and bar charts (Trading Volume).
* **Performance Optimization:** Utilizes Streamlit's `@st.cache_data` to cache the downloaded dataset for faster subsequent loads.

## 📂 Project Structure
* `Dashboard.py`: The main application script containing the UI and logic.
* `requirements.txt`: The list of dependencies required to run the project.
* `README.md`: Project documentation.
* `hourly_data.csv`: Automatically generated dataset upon the first run.

## ⚙️ Installation and Usage

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
