# LAB5

# Weather Data Pipeline Using Apache Airflow

## Project Overview
This project involves developing an automated data pipeline using Apache Airflow to fetch, transform, and load weather data into a PostgreSQL database. The pipeline processes data for a specific city (e.g., Portland), making it accessible for analysis and reporting.

## Features
- **API Readiness Check**: Ensures the weather API is online before fetching data.
- **Weather Data Extraction**: Retrieves current weather data from the OpenWeatherMap API.
- **Data Transformation**: Converts temperatures from Kelvin to Fahrenheit and adjusts timestamps to the local timezone.
- **Data Loading**: Stores transformed data in a PostgreSQL database.
- **Logging and Monitoring**: Utilizes Airflow's logging for debugging and performance tracking.

## Technologies Used
- **Apache Airflow**: For orchestrating the ETL pipeline.
- **PostgreSQL**: As the database for storing weather data.
- **OpenWeatherMap API**: For retrieving weather information.
- **Python**: For data transformation and task scripting.

---

## Prerequisites
1. **Software Requirements**:
   - Python (>= 3.8)
   - Apache Airflow
   - PostgreSQL
2. **Environment Setup**:
   - Install Airflow and its dependencies.
   - Set up a local PostgreSQL database with the name `weather_data`.
   - Generate an API key from [OpenWeatherMap](https://openweathermap.org/api).

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/weather-data-pipeline.git
cd weather-data-pipeline





