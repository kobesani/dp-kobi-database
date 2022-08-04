from alembic import config
from alembic import script
from google.cloud import bigquery
from pathlib import Path


PKG_DIR = Path(__file__).resolve().parents[1]
SQLS_PATH = PKG_DIR / "sql_migrations"
ALEMBIC_CFG_PATH = PKG_DIR / "alembic.ini"
MIGRATION_SCRIPTS_PATH = PKG_DIR / "dp_kobi_database" / "migrations"

alembic_cfg = config.Config(ALEMBIC_CFG_PATH)
project_id = alembic_cfg.get_main_option("gcp.project.id")
dataset = "dp_valorant"

current_revision = script.ScriptDirectory(MIGRATION_SCRIPTS_PATH).get_current_head()

# Construct a BigQuery client object.
client = bigquery.Client(project=project_id)

# Run SQL queries
version_sql_path = Path(list(SQLS_PATH.glob(f"{current_revision}.sql"))[0])
version_json_path = Path(list(SQLS_PATH.glob(f"{current_revision}.json"))[0])
bigquery_job = client.query(version_sql_path.read_text())
bigquery_job.result()

table_id = f"{project_id}.{dataset}.alembic_version"
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    schema=[bigquery.SchemaField("version_num", "STRING", mode="REQUIRED")],
    autodetect=True,
)

with version_json_path.open(mode="rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)

job.result()  # Waits for the job to complete.

table = client.get_table(table_id)  # Make an API request.
print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
    )
)
