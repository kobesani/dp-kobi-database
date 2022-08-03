import sqlalchemy

from alembic import config
from alembic import script
from alembic.runtime import migration
from google.cloud import bigquery
from pathlib import Path

# TODO - set up subsections of alembic.ini for each schema / project whatever that is maintained for the data platform

alembic_cfg_path = Path(__file__).parent / "alembic.ini"
alembic_cfg = config.Config(alembic_cfg_path)
url = alembic_cfg.get_main_option('sqlalchemy.url')
engine = sqlalchemy.engine.create_engine(url=url)
# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
table_id = "your-project.your_dataset.your_table_name"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=True,
)

with open(file_path, "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)

job.result()  # Waits for the job to complete.

table = client.get_table(table_id)  # Make an API request.
print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
    )
)