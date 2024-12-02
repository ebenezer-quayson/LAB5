# DE Taxi Demo Solution

## Overview
The DE Taxi Demo Solution demonstrates the integration of **Power Apps**, **Power Automate**, and **Dataverse** to create a streamlined system for processing and visualizing taxi location data. The solution includes automated email processing, data transformation, storage, and visualization on an interactive map.

---

## Features
- **Email Integration**: Automatically processes emails with specific keywords to extract and save data files.
- **Data Transformation**: Cleans and formats data using Power Query.
- **Dataverse Integration**: Stores and organizes transformed data in Dataverse tables for analysis and visualization.
- **Data Profiling**: Generates insights on data quality and transformation results.
- **Interactive Visualization**: A user-friendly Canvas App displaying taxi locations on a map.

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
2. Create a new environment:
   - **Name**: `DE Lecture`
3. Within this environment, create a solution:
   - **Name**: `DE Taxi Demo`

### 2. Configure Power Automate Flow
1. Create a new Power Automate flow in the `DE Taxi Demo` solution.
2. Configure the flow as follows:
   - **Trigger**: On receiving an email containing "YellowTaxi" in the body or subject.
   - **Steps**:
     1. Save email attachments to a OneDrive folder named `DE PowerAutomate`.
     2. Use Power Query to:
        - Remove unnecessary columns.
        - Filter rows where the drop-off coordinate is `0`.
        - Parse coordinates as text.
     3. Load the transformed data into a Dataverse table:
        - **Table Name**: `TaxiData`.
     4. Load data profiling results into a separate Dataverse table:
        - **Table Name**: `TaxiDataProfile`.
        - Include:
          - Count of unique records.
          - Number of errors.
          - Summary of transformations.
     5. Send an email notification with an HTML table of the `TaxiDataProfile` to your mentor and instructor.

### 3. Create Power Apps Canvas App
1. Within the `DE Taxi Demo` solution, create a Canvas App.
2. Connect the app to the `TaxiData` Dataverse table.
3. Add the following features:
   - **Map Visualization**: Display taxi locations on a map.
   - **Additional Details**: Include relevant information about each taxi.
4. Design a clean and intuitive user interface.

---

## Deliverables

### Git Repository
Ensure the repository includes:
- Power Automate Flow export.
- Power Apps Canvas App configuration file.
- Dataverse schema documentation.

### Screenshots
Provide images of:
1. Power Automate Flow setup.
2. Power Apps Canvas App interface, including the map visualization.

---

## How It Works
1. The flow is triggered when an email with specific keywords ("YellowTaxi") is received.
2. The attachment is saved and transformed using Power Query.
3. Transformed data is stored in Dataverse for further analysis.
4. Data profiling results are emailed to stakeholders for review.
5. Users can visualize taxi locations on a map within the Power Apps Canvas App.

---

## License
This project is for educational purposes. Feel free to reuse or modify it under the terms of the MIT License.

---

