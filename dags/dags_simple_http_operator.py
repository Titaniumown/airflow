from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.decorators import task

with DAG(
    dag_id="dags_simple_http_operator",
    schedule=None,
    start_date=pendulum.datetime(2024, 6, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    '''서울시 우수 중소기업 정보'''
    excellent_sme_info = SimpleHttpOperator(
        task_id='excellent_sme_info',
        http_conn_id='openapi.seoul.go.kr',
        endpoint='{{var.value.apikey_openapi_seoul_go_kr}}/json/TnSmepReqOpen/1/100/',
        method='GET',
        headers={'Content-Type': 'application/json',
                            'charset': 'utf-8',
                            'Accept': '*/*'
                            }

    )

    @task(task_id='python_2')
    def python_2(**kwargs):
        ti = kwargs['ti']
        rslt = ti.xcom_pull(task_ids='excellent_sme_info')
        import json
        from pprint import pprint

        pprint(json.loads(rslt))

        excellent_sme_info >> python_2()
