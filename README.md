# ETL & ELT Automation Projects: Weather Data Pipeline & DE Taxi Demo Solution

## Overview
This repository showcases two ETL & ELT projects that automate data workflows using Apache Airflow and Microsoft Power Platform tools.

---

## Project 1: Weather Data Pipeline Using Apache Airflow
This project implements an automated pipeline to fetch, transform, and store weather data for daily analysis. It uses Apache Airflow to orchestrate the following tasks:
- **API Readiness Check**: Verifies the availability of the OpenWeatherMap API.
- **Data Extraction**: Retrieves weather data for a specified city (e.g., Portland).
- **Data Transformation**: Converts temperature to Fahrenheit and adjusts timestamps.
- **Data Loading**: Stores transformed data in a PostgreSQL database.

### Deliverables
- Airflow DAG file with defined tasks.
- PostgreSQL schema for weather data storage.
- Screenshots of Airflow execution logs and sample data.

---

## Project 2: DE Taxi Demo Solution Using Power Apps and Power Automate
This project demonstrates a Power Platform solution to process email-based taxi data and visualize it on a map. It integrates Power Automate, Power Apps, and Dataverse:
- **Email Processing**: Extracts attachments from emails with "YellowTaxi" in the subject or body.
- **Data Transformation**: Cleans and structures data in Power Query.
- **Dataverse Integration**: Stores transformed data in Dataverse tables.
- **Visualization**: Displays taxi locations on a map in a Power Apps Canvas App.
- **Notifications**: Sends data profiles via email upon data refresh.

### Deliverables
- Power Automate flow file and screenshots.
- Power Apps Canvas App screenshots.
- Dataverse schema details.

---
