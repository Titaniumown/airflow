from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.empty import EmptyOperator
from airflow.utils.edgemodifier import Label

with DAG(
    dag_id="dags_python_operator",
    schedule=None,
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    empty_1 = EmptyOperator(
        task_id='empty_1'
    )

    empty_2 = EmptyOperator(
        task_id='empty_2'
    )

    empty_1 >> Label('1과 2사이') >> empty_2

    empty_3 = EmptyOperator(
        task_id='empty_3'
    )

    empty_4 = EmptyOperator(
        task_id='empty_4'
    )

    empty_5 = EmptyOperator(
        task_id='empty_5'
    )

    empty_6 = EmptyOperator(
        task_id='empty_6'
    )

    empty_2 >> Label('start branch') >> [empty_3, empty_4, empty_5] >> Label('end branch') >> empty_6