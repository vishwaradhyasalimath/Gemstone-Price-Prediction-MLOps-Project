from __future__ import annotations
import json
from textwrap import dedent
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from src.pipeline.training_pipeline import TrainingPipeline

training_pipeline = TrainingPipeline()

with DAG(
    "gemstone_training_pipeline",
    default_args = {'retries':2},
    description="it is my training pipeline",
    schedule="@weekly",
    start_date=pendulum.datetime(2025,4,11,t2='UTC'),
    catchup=False,
    tags=['machine_learning','classification','gemstome-prediction'],
) as dag:
    
    dag.doc_md = __doc__

    '''whenever we excetue the dag it pass the dict as argument by default, the dict will have a
    called ti(task instance) '''
    def data_ingestion(**kwargs):
        ti = kwargs["ti"]
        train_data_path,test_data_path=training_pipeline.start_data-data_ingestion()
        ti.xcom_push("data_transformation_artifact",{"tain_data_path":train_data_path,"test_data_path":test_data_path})
        
         #xcom is the cross communication between two components

    def data_transformations(**kwargs):
        ti = kwargs['ti']
        data_ingestion_artifact=ti.xcom_pull(task_ids="data_ingestion",key="data_ingestion")
        train_arr,test_arr=training_pipeline.start_data_transformation(data_ingestion)
        train_arr=train_arr.tolist()
        test_arr=test_arr.tolist()
        ti.xcom_push("data_transformation_artifact",{"train_arr":train_arr,'test_arr':test_arr})

    def model_trainer(**kwargs):
        import numpy as np
        ti = kwargs["ti"]
        data_transformations_artifact = ti.xcom_pull(task_ids="data_transformation",key="data_transformation_artifact")
        train_arr=np.array(data_transformations_artifact["train_arr"])
        test_arr=np.array(data_transformations_artifact["test_arr"])
        training_pipeline.start_model_training(train_arr,test_arr)


    def push_data_to_s3(**kwargs):
        import os
        bucket_name=os.getenv("BUCKET_NAME")
        artifact_folder="/app/artifacts"
        os.system(f"aws s3 sync {artifact_folder} s3:/{bucket_name}/artifact")


    data_ingestion_task=PythonOperator(
        task_id = "data_ingestion",
        python_callable=data_ingestion,
    )
    data_ingestion_task.doc_md=dedent(
        """ingestion task : this task creates a train and test file"""
    )

    data_transform_task=PythonOperator(
        task_id = "data_transformation",
        python_callable=data_transformations,
    )
    data_transform_task.doc_md=dedent(
        """transformation task : this task creates a train and test file"""
    )


    model_trainer_task=PythonOperator(
        task_id = "model_trainer",
        python_callable=model_trainer,
    )
    model_trainer_task.doc_md=dedent(
        """transformation task : this task creates a train and test file"""
    )

    push_data_to_s3_task=PythonOperator(
        task_id="push_data_to_s3",
        python_callable=push_data_to_s3
    )



data_ingestion_task >> data_transform_task >> model_trainer_task >> push_data_to_s3_task


    
