from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",
    schedule=None,
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    # [START howto_operator_bash]
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="df -h",
    )

    # bash_t2 = BashOperator(
    #     task_id="bash_t2",
    #     bash_command="echo $HOSTNAME",
    # )

    bash_t1
    # [END howto_operator_bash]
