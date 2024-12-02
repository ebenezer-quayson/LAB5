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





# DE Taxi Demo Solution

## Project Overview
This project demonstrates the integration of **Power Apps**, **Power Automate**, and **Dataverse** to create an end-to-end solution for processing and visualizing taxi location data. The solution includes data extraction from email attachments, transformation, storage in Dataverse, and visualization on a map through a Power Apps Canvas App.

## Features
- **Email Integration**: Automatically processes emails with specific keywords to extract and save data files.
- **Data Transformation**: Cleans and formats data using Power Query.
- **Dataverse Integration**: Stores data in Dataverse tables for analysis and visualization.
- **Data Profiling**: Provides insights into the data quality and transformation results.
- **User Interface**: A clean and intuitive Canvas App to visualize taxi locations on a map.

---

## Technologies Used
- **Microsoft Power Apps**
- **Microsoft Power Automate**
- **Dataverse**
- **Power Query**

---

## Setup Instructions

### 1. Create Power Apps Environment
1. Log in to [Power Apps](https://make.powerapps.com/).
2. Create an environment:
   - **Name**: `DE Lecture`
3. Within this environment, create a solution:
   - **Name**: `DE Taxi Demo`

### 2. Power Automate Flow Configuration
1. Create a new Power Automate flow in the `DE Taxi Demo` solution.
2. Configure the flow as follows:
   - **Trigger**: On receiving an email containing "YellowTaxi" in the body or subject.
   - **Steps**:
     1. Save the email attachment to a OneDrive folder named `DE PowerAutomate`.
     2. Load the file into Power Query for transformation:
        - Remove unnecessary columns.
        - Filter rows where the drop-off coordinate is `0`.
        - Parse coordinates as text.
     3. Load the transformed data into a Dataverse table:
        - Table Name: `TaxiData`.
     4. Perform data profiling and load results into a new Dataverse table:
        - Table Name: `TaxiDataProfile`.
        - Include:
          - Count of unique records.
          - Number of errors.
          - Summary of transformations.
     5. Send an email notification with an HTML table of the `TaxiDataProfile` to your mentor and instructor.

### 3. Create Power Apps Canvas App
1. Within the `DE Taxi Demo` solution, create a Canvas App.
2. Connect the app to the `TaxiData` Dataverse table.
3. Add features:
   - **Map Visualization**: Display taxi locations on a map.
   - **Additional Details**: Include relevant information about each taxi.
4. Ensure the interface is user-friendly and visually appealing.

---

## Deliverables

### Git Repository
Include the following files:
- Power Automate Flow export.
- Power Apps Canvas App configuration.
- Dataverse schema documentation.

### Images
Provide screenshots of:
1. The Power Automate Flow setup.
2. The Power Apps Canvas App, including the map visualization and interface.

---



