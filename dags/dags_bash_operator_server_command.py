from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator


bash_script="""
pwd
touch `pwd`/test.txt
echo hello world >> test.txt
cat test.txt
"""

with DAG(
    dag_id="dags_bash_operator_server_command",
    schedule=None,
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["test", "server_command"],
) as dag:
    # [START howto_operator_bash]
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command=bash_script,
    )

    # bash_t2 = BashOperator(
    #     task_id="bash_t2",
    #     bash_command="echo $HOSTNAME",
    # )

    bash_t1
    # [END howto_operator_bash]
