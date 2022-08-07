import pendulum

from plugins.defaults import DagDefaults

project = DagDefaults.gcp_bq_project
dataset = DagDefaults.gcp_bq_dataset
table = "test_table"
gcs_prefix = f'{pendulum.now().strftime("%Y/%m/%d")}/test.json.gz'
