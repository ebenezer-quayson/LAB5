from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
#from airflow.utils.dates import days_ago
from pendulum import datetime
import requests
import json
from datetime import datetime, timezone
#from airflow.operators.email import EmailOperator
from airflow.models import Variable
#from airflow.utils.trigger_rule import TriggerRule

#Get airflow variable
api_key = Variable.get("openweather_api_key")


smtp_host = Variable.get("smtp_host")
smtp_user = Variable.get("smtp_user")
smtp_password = Variable.get("smtp_password")
smtp_mail_from = Variable.get("smtp_mail_from")


# Default arguments for the DAG
default_args = {
    "owner": "Ebenezer Quayson",
    "retries": 1,
    "retry_delay": 5,  # Retry after 5 minutes
    "email": [smtp_host],
    "email_on_failure": True,
    "email_on_failure": True,
    "smtp_user": smtp_mail_from
}

# Define the DAG
with DAG(
    dag_id="weather_data_pipeline",
    description="A DAG to fetch, transform, and store weather data",
    schedule_interval=None,
    start_date=datetime(2024, 11, 29),
    catchup=False,
    default_args=default_args,
    tags=["weather", "ETL"],
) as dag:

    # Task 1: Check if the weather API is available
    check_weather_api = HttpSensor(
        task_id="check_weather_api",
        http_conn_id="weather_api",
        endpoint=f"data/2.5/weather?q=Portland&appid={api_key}",
        poke_interval=5,
        timeout=20,
    )

    # Task 2: Fetch weather data from the API
    def fetch_weather_data(ti):
        """
        Fetch weather data from the OpenWeather API.
        """
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q=Portland&appid={api_key}"
        )
        response.raise_for_status()  # Raise an error if the request fails
        ti.xcom_push(key="weather_data", value=response.text)

    fetch_weather_data_task = PythonOperator(
        task_id="fetch_weather_data",
        python_callable=fetch_weather_data,
    )

    # Task 3: Transform the weather data
        
    def transform_weather_data(ti):
        """
        Transform raw weather data into a structured format.
        """
        raw_data = ti.xcom_pull(task_ids="fetch_weather_data", key="weather_data")
        data = json.loads(raw_data)

        # Extract and transform relevant fields
        city = data["name"]
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15  # Convert Kelvin to Celsius
        temperature_f = (temperature_c * 9 / 5) + 32  # Convert Celsius to Fahrenheit
        wind_speed = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        timestamp = datetime.fromtimestamp(data['dt'], timezone.utc)    

        transformed_data = {
            "city": city,
            "temperature_c": temperature_c,
            "temperature_f": temperature_f,
            "wind_speed": wind_speed,
            "humidity": humidity,
            "timestamp": timestamp,
        }

        ti.xcom_push(key="transformed_data", value=transformed_data)

    transform_weather_data_task = PythonOperator(
        task_id="transform_weather_data",
        python_callable=transform_weather_data,
    )

    # Task 4: Load transformed data into PostgreSQL
    load_weather_data = PostgresOperator(
        task_id="load_weather_data",
        postgres_conn_id="postgres_default",
        sql="""
        CREATE TABLE IF NOT EXISTS daily_weather (
        sid SERIAL PRIMARY KEY,
        city VARCHAR(100),
        temperature_c FLOAT,
        temperature_f FLOAT,
        wind_speed FLOAT,
        humidity INTEGER,
        timestamp TIMESTAMP WITH TIME ZONE);                                                    
    
        INSERT INTO daily_weather (city, temperature_c, temperature_f, wind_speed, humidity, timestamp)
        VALUES (
            '{{ ti.xcom_pull(task_ids="transform_weather_data", key="transformed_data")["city"] }}',
            {{ ti.xcom_pull(task_ids="transform_weather_data", key="transformed_data")["temperature_c"] }},
            {{ ti.xcom_pull(task_ids="transform_weather_data", key="transformed_data")["temperature_f"] }},
            {{ ti.xcom_pull(task_ids="transform_weather_data", key="transformed_data")["wind_speed"] }},
            {{ ti.xcom_pull(task_ids="transform_weather_data", key="transformed_data")["humidity"] }},
            '{{ ti.xcom_pull(task_ids="transform_weather_data", key="transformed_data")["timestamp"] }}'
        );
        """,
    )
   
    '''email_failure = EmailOperator(
        task_id='send_failure_email',
        to='ebenezer.quayson@amalitech.com',  # Recipient email
        subject='Airflow Task Failure Alert',
        html_content="""<h3>Task {{ task_instance.task_id }} failed!</h3>
                       <p>DAG: {{ dag.dag_id }}<br>Task: {{ task_instance.task_id }}<br>Execution Date: {{ ds }}</p>""",
        trigger_rule=TriggerRule.ONE_FAILED,  # Triggered when the task fails
       
    )   
    
    


    email_success = EmailOperator(
        task_id="send_success_email",
        to=[smtp_mail_from],
        subject="Pipeline Success!",
        html_content="The pipeline ran successfully.",
        conn_id='connection_id',  # Use the connection ID you created
)
'''

    
    # Set task dependencies
    check_weather_api >> fetch_weather_data_task >> transform_weather_data_task >> load_weather_data
    #load_weather_data >> email_failure
    #load_weather_data >> email_success
   
