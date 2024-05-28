from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.decorators import dag, task


with DAG(
    dag_id="dags_python_show_templates",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2024, 5, 1, tz="Asia/Seoul"),
    catchup=True,
) as dag:

    @task(task_id="python_task")
    def show_templates(**kwargs1):
        from pprint import pprint
        pprint(kwargs1)

    show_templates()