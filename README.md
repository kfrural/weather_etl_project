# Weather ETL Pipeline Project with Apache Airflow

This project contains an ETL (Extract, Transform, Load) pipeline using **Apache Airflow** for task automation. The pipeline collects meteorological data, performs some transformations, and stores the information for subsequent analysis.

## Prerequisites

Before starting, ensure you have the following installed on your environment:

- **Python 3.x** (recommended Python 3.7 or higher)
- **pip** (Python package manager)
- **Git** (for cloning the repository)
- **Apache Airflow** (for orchestrating tasks)

## Installation Steps

### 1. Clone the Repository

Clone the project repository to your local environment:

```bash
git clone https://github.com/your_username/your_repository.git
cd your_repository
```

### 2. Create a Virtual Environment (virtualenv)

It's recommended to use a virtual environment to isolate project dependencies. Run the following command to create and activate the environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### 3. Install Project Dependencies

With the virtual environment activated, install the project dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If you're having trouble installing Apache Airflow, use the command below to install a specific version with appropriate dependencies for Python 3.7 (or the version you're using):

```bash
pip install apache-airflow==2.7.0 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.0/constraints-3.7.txt"
```

### 4. Initialize Airflow Database

Airflow uses a database to store task states and other metadata. To initialize the database, run:

```bash
airflow db init
```

### 5. Create Airflow Admin User

To access the Airflow web interface, you need to create an administrator user. Run the following command to create a user with administrative privileges:

```bash
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --email admin@example.com \
    --role Admin \
    --password admin
```

### 6. Start Airflow Webserver

Now, start the web server to access the Airflow interface through your browser. The server will start on port `8080`:

```bash
airflow webserver --port 8080
```

Access the web interface at [http://localhost:8080](http://localhost:8080).

### 7. Start Airflow Scheduler

In a separate terminal, start the Airflow scheduler, responsible for executing DAGs according to scheduling:

```bash
airflow scheduler
```

### 8. Verify Airflow Interface

Now, open your browser and go to the Airflow web interface at [http://localhost:8080](http://localhost:8080). You should be able to view your DAGs and monitor task execution.

---

## Running the ETL Pipeline

### 1. Defining DAGs

DAGs (Directed Acyclic Graphs) are the workflows defined in Airflow. The DAG definition files are in the `dags/` directory.

### 2. Manually Triggering a DAG

To manually trigger a DAG, access the Airflow web interface, click on the desired DAG, and then click the "Trigger DAG" button.

### 3. Checking Logs

Airflow generates detailed logs for each executed task. To review logs for failed tasks or to check execution details, click on the desired DAG and task to view the corresponding log.

---

## Testing the System

To test the pipeline locally, follow these steps:

1. **Manually execute the pipeline** by clicking the "Trigger" button in the Airflow web interface.
2. **Check execution logs** to ensure that data extraction, transformation, and loading are working correctly.
3. **Monitor task progress** through the web interface.

---

## Project Structure

```
weather_etl_project/
│
├── dags/
│   └── weather_etl_dag.py        # Main file with the pipeline DAG
│
├── scripts/
│   ├── extract_weather.py        # Data extraction script
│   ├── transform_weather.py      # Data transformation script
│   └── load_weather.py           # Data loading script
│
├── config/
│   └── settings.py               # API and other parameters configuration
│
├── requirements.txt              # File with project dependencies
│
└── README.md                    # This file
```

---

## Contributing

If you'd like to contribute to this project:

1. Fork this repository.
2. Create a branch for your modification (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit (`git commit -am 'Adding a new feature'`).
4. Push to your fork (`git push origin feature/your-feature-name`).
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
