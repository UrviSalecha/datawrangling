from airflow.sdk import dag,task
# Two Mistakes find 
@dag(dag_id="daily_report", schedule=None)
def report_dag():
    @task.python
    def extract():
        return [1,2,3]
    @task.python
    def total(numbers):
        print(sum(numbers))

    extract >> total()
report_dag

# The two mistakes in the code are: 
# instead of report_dag in the last line the function should be called as report_dag()
# The second mistake is extract >> total() should be extract() >> total()