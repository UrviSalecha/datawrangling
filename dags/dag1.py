from airflow.sdk import dag,task

@dag(dag_id="stock_check",schedule=None)
def conditional_branch():
    @task.python
    def check_stock(): #check_Stock returns item : qty: in dictionary format
        return {"item":"rice","qty":12}
    @task.branch # if qty is less 
    def decide(item_qty):
        if item_qty["qty"] < 20:
            return "place_order"
        else:
            return "skip_order"
    # Bash task to place order
    @task.bash
    def place_order():
        return "echo 'Placing order for item'"
    @task.bash
    def skip_order():
        return "echo 'Skipping order for item'"
    @task.python
    def notify():
        print("Stock check done")
        # run whichever path was chosen
    check=check_stock()
    decision=decide(check)
    order=place_order()
    skip=skip_order()
    notify_task=notify()

    check >> decision >> [order,skip] >> notify_task

conditional_branch()

# Draw the DAG and state which task will be skipped
# The DAG will have the following structure:
# check_stock -> decide -> [place_order, skip_order] -> notify 